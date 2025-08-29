import discord
from discord.ext import commands
import os

# Подключаем интенты
intents = discord.Intents.default()
intents.message_content = True

# Создаём бота
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} включен и готов к работе!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Запуск (токен хранится в GitHub Secrets)
bot.run(os.getenv("MTQxMDk0MzQyNzU0MTIwOTA4OA.Gr7HuW.AOLzOcwzUSYwbFu5jwLYQTMQ-NPpJDhjpdHOww"))
