import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("Ready")
    
@bot.command()
async def embed(ctx, title: str, description: str, image_url: str):
    embed = discord.Embed(title=title, description=description, color=0x00ff00)
    embed.set_image(url=image_url)
    # embed.add_field(name="링크", value=f"[여기를 클릭하세요]({link})", inline=False)
    await ctx.send(embed=embed)

# 이 부분에 디스코드 봇 토큰을 입력하세요.
bot.run('MTE1NzAzODAyNTE3NjUyNjg4OA.GMTZ1n.AgtPz926fege_ZhmbiFiJVd1mOOQe2v4ceXsWg')
