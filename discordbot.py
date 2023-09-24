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

@bot.event
async def on_member_join(member):
    # 새로운 멤버가 입장했을 때 실행되는 이벤트 핸들러
    welcome_message = f'{member.mention}님이 입장했어요! 환영합니다!'
    
    join_time = datetime.now().strftime('%Y년 %m월 %d일 %H:%M:%S')
    join_message = f'서버 가입일: {member.joined_at.strftime("%Y년 %m월 %d일 %H:%M:%S")}'
    
    user = await bot.fetch_user(member.id)
    created_at = user.created_at.strftime('%Y년 %m월 %d일 %H:%M:%S')
    user_info = f'유저 정보: {user.name}#{user.discriminator} (ID: {user.id})\n가입일: {created_at}'

    # 이미지 생성
    image = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 20)
    draw.text((50, 80), welcome_message, fill='black', font=font)
    draw.text((50, 120), join_message, fill='black', font=font)
    draw.text((50, 160), user_info, fill='black', font=font)

    # 이미지 저장
    image_path = 'welcome_image.png'
    image.save(image_path)

    # 이미지 전송
    channel_id = 1145270730578206801  # 이미지를 전송할 채널의 ID로 변경해야 합니다.
    channel = bot.get_channel(channel_id)
    await channel.send(f'{member.mention}', file=discord.File(image_path))

@bot.event
async def on_member_remove(member):
    # 멤버가 퇴장했을 때 실행되는 이벤트 핸들러
    goodbye_message = f'{member}님이 퇴장했습니다.'

    leave_time = datetime.now().strftime('%Y년 %m월 %d일 %H:%M:%S')
    leave_message = f'퇴장 시간: {leave_time}'

    # 이미지 생성
    image = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 20)
    draw.text((50, 80), goodbye_message, fill='black', font=font)
    draw.text((50, 120), leave_message, fill='black', font=font)

    # 이미지 저장
    image_path = 'goodbye_image.png'
    image.save(image_path)

    # 이미지 전송
    channel_id = 1145270730301386792  # 이미지를 전송할 채널의 ID로 변경해야 합니다.
    channel = bot.get_channel(channel_id)
    await channel.send(file=discord.File(image_path))

bot.run('MTE1NTM5ODkwMTkxOTEzNzc5Mg.GBe_gw.i_T5BHrZF0K0hlT68xd2MCPA_642jTygd0eorU')
