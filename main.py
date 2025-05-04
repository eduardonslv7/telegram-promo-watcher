from telethon import TelegramClient, events
import requests
import json

# carregar configurações
with open("config.json") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
discord_webhook_url = config["discord_webhook"]
keywords = config["keywords"]
channels = config["channels"]

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    message = event.message.message.lower()
    for keyword in keywords:
        if keyword.lower() in message:
            requests.post(discord_webhook_url, json={"content": f"🔔 Mensagem relevante encontrada:\n{event.message.message}"})
            break

print("✅ Monitorando canais...")
client.start()
client.run_until_disconnected()
