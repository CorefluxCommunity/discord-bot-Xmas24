import os
import ssl
import json
import discord
from paho.mqtt.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8883))  # Default MQTT TLS port
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# File to store processed topics
PROCESSED_TOPICS_FILE = "processed_topics.json"

# Initialize the list of processed topics
if not os.path.exists(PROCESSED_TOPICS_FILE):
    with open(PROCESSED_TOPICS_FILE, 'w') as file:
        json.dump([], file)

# Load processed topics
def load_processed_topics():
    with open(PROCESSED_TOPICS_FILE, 'r') as file:
        return json.load(file)

def save_processed_topics(topics):
    with open(PROCESSED_TOPICS_FILE, 'w') as file:
        json.dump(topics, file)

processed_topics = load_processed_topics()

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print("Connecting to MQTT broker...")

    # MQTT setup
    mqtt_client = Client()
    mqtt_client.tls_set_context(ssl.create_default_context())  # Set up TLS
    mqtt_client.tls_insecure_set(True)  # Allow insecure TLS connections
    mqtt_client.on_connect = on_mqtt_connect
    mqtt_client.on_message = on_mqtt_message
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
    mqtt_client.loop_start()

# MQTT callbacks
def on_mqtt_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe("#")  # Subscribe to all topics
    else:
        print(f"Failed to connect, return code {rc}")

async def send_message_to_discord(topic, payload):
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        # Format the message as: topic -> <topic> | message -> <payload>
        formatted_message = f"**topic ->** `{topic}`\n**message ->** `{payload}`"
        await channel.send(formatted_message)

def on_mqtt_message(client, userdata, msg):
    global processed_topics
    topic, payload = msg.topic, msg.payload.decode('utf-8')

    if topic not in processed_topics:
        processed_topics.append(topic)
        save_processed_topics(processed_topics)
        bot.loop.create_task(send_message_to_discord(topic, payload))

# Run the bot
bot.run(DISCORD_TOKEN)

