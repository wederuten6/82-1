import discord
from discord.ext import commands
from api_handler import get_next_tournament_info

TOKEN = 'MTMzNzg0OTAwMzcxNDU0Nzg2NA.G0A6yS.q6hY5AbbmTHnrQmtaOjDyl_AGKhAKmTr3v1320'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} is now online!')

@bot.command()
async def next_tournament(ctx):
    """次回トーナメント情報を表示"""
    tournament_info = get_next_tournament_info()
    if tournament_info:
        await ctx.send(f"🏆 次回トーナメント情報:\n名前: {tournament_info['title']}\n開始時間: {tournament_info['start']}")
    else:
        await ctx.send("トーナメント情報が取得できませんでした。")

bot.run(TOKEN)
