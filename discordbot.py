import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@client.event
async def on_member_join(member):
    print(f'{member} joined at {datetime.now()}\n account created at {member.created_at}\n Profile picture: {member.avatar_url}')

@client.event
async def on_member_remove(member):
    print(f'{member} left at {datetime.now()}')

bot.run('MTE1NTM5ODkwMTkxOTEzNzc5Mg.GBe_gw.i_T5BHrZF0K0hlT68xd2MCPA_642jTygd0eorU')
