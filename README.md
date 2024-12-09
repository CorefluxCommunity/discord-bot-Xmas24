# **Coreflux X-Mas MQTT to Discord Bot**

🎄 **Coreflux X-Mas Bot** is a Python-based application that connects to an MQTT broker, retrieves messages, and sends them to a Discord channel in a clear and organized format. Celebrate the holiday season while keeping your MQTT topics and payloads seamlessly integrated into Discord.

---

## **How It Works**

1. **MQTT Connection**:
   - The bot connects to an MQTT broker (e.g., `xmas.coreflux.cloud`) using TLS for secure communication.
   - It subscribes to all topics (`#`) and listens for incoming messages.

2. **Message Processing**:
   - Each message (topic and payload) is checked to ensure it hasn't already been sent to the Discord channel.
   - If a message is new, it formats the content as:
     ```
     topic -> <topic>
     message -> <payload>
     ```

3. **Discord Integration**:
   - The bot uses the Discord API to send the formatted messages to a specific Discord channel.
   - It posts each unique MQTT message to the channel in real-time.

4. **Persistent Message Tracking**:
   - Processed topics are stored in a `processed_topics.json` file to avoid duplicate messages being sent to Discord.

---

## **Features**

- Secure MQTT connection using **TLS** with optional insecure mode for self-signed certificates.
- Real-time forwarding of MQTT messages to a Discord channel.
- Persistent tracking of processed topics to prevent duplicate messages.
- Clean and readable message formatting in Discord:
  ```
  **topic ->** `<topic>`
  **message ->** `<payload>`
  ```

---

## **How to Use**

### **1. Prerequisites**
- Python 3.8 or later.
- A Discord server with a bot token and a specific channel for the bot.
- Access to an MQTT broker (e.g., `xmas.coreflux.cloud`).

### **2. Clone the Repository**
```bash
git clone https://github.com/<your-repo-name>/coreflux-xmas-bot.git
cd coreflux-xmas-bot
```

### **3. Set Up the Environment**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file in the project root and add the following:
```env
DISCORD_TOKEN=your_discord_bot_token
MQTT_BROKER=your_mqtt_broker_address
MQTT_PORT=8883  # Use 1883 for non-TLS connections
DISCORD_CHANNEL_ID=your_discord_channel_id
```

### **5. Run the Bot**
Start the bot with:
```bash
python app.py
```

### **6. Publish MQTT Messages**
Use an MQTT client to publish messages to your broker. For example:
```bash
mosquitto_pub -h xmas.coreflux.cloud -t "home/sensors/temperature" -m "25.6°C"
```

The bot will send the following message to your Discord channel:
```
**topic ->** `home/sensors/temperature`
**message ->** `25.6°C`
```

---

## **Configuration Options**

### **MQTT Broker**
- You can use any MQTT broker that supports TLS. For insecure connections (e.g., self-signed certificates), the bot is configured to allow insecure TLS connections.

### **Discord Channel**
- Replace `DISCORD_CHANNEL_ID` in your `.env` file with the numeric ID of the Discord channel you want the bot to use.  
  To find the channel ID:
  1. Enable Developer Mode in Discord settings.
  2. Right-click the channel and select **Copy ID**.

---

## **Project Structure**

```
coreflux-xmas-bot/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── processed_topics.json # Tracks processed MQTT topics
├── .env                  # Environment variables (user-created)
└── README.md             # Project documentation
```

---

## **Contributing**

We welcome contributions to improve this project! Feel free to:
- Add new features or improve existing functionality.
- Enhance the user experience (e.g., add more message formats).
- Report bugs or submit suggestions via issues or pull requests.

---

## **License**

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

---

## **Acknowledgments**

🎅 Big thanks to everyone who made this project possible:
- The **Coreflux Team** for their support and vision.
- Our amazing clients and partners, including **Grafana Labs**, **DigitalOcean**, **RisingWave**, and **CrateDB**.
- The open-source community for providing the tools we love!

Wishing you a Merry Christmas and Happy Holidays! 🎁🎄

