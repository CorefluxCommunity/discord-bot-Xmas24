{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "mqtt-discord-bot-env";

  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.paho-mqtt
    pkgs.python3Packages.discordpy
    pkgs.python3Packages.python-dotenv
  ];

  shellHook = ''
    echo "Environment ready! Python, Paho-MQTT, Discord.py, and Python-dotenv are installed."
  '';
}

