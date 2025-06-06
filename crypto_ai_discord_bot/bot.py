import discord
from discord.ext import commands
from data_fetcher import get_data
from ta_engine import compute_indicators, summarize_data
from ai_agent import analyze_chart
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def analyze(ctx, symbol: str):
    try:
        df = get_data(symbol)
        indicators = compute_indicators(df)
        summary = summarize_data(df, indicators)
        insights = analyze_chart(symbol, summary, indicators)
        await ctx.send(insights)
    except Exception as e:
        await ctx.send(f"Error: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))
