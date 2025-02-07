import discord
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルからトークンを読み込む

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # .envファイルに保存されたトークンを取得

intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'こんにちは {message.author.name}！')

client.run(TOKEN)
