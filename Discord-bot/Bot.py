import discord
from discord import app_commands
from discord.ext import commands
import os
import google.generativeai as genai

# Настройка Gemini 2.5 Flash
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Настройка бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Бот {bot.user} подключён и готов к работе!")

# Слэш-команда /c
@bot.tree.command(name="c", description="Задай вопрос ИИ")
@app_commands.describe(prompt="Текст для ИИ")
async def c_command(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    try:
        response = model.generate_content(prompt)
        await interaction.followup.send(response.text)
    except Exception as e:
        await interaction.followup.send(f"Ошибка при обращении к Gemini: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))
