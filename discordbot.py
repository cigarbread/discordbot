import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("샤방샤방")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("별나비 안녕"):
        await message.channel.send("안녕하세영~")
    if message.content.startswith("별나비 울룰루"):
        await message.channel.send("삥뽕빵")
    if message.content.startswith("별나비 잘자"):
        await message.channel.send("잘자영~")
    if message.content.startswith("별나비 잘가"):
        await message.channel.send("다음에 또 뵈여ㅠㅠ")
    if message.content.startswith("별나비 서버주소"):
        await message.channel.send("https://discord.gg/bNQd8Re")
    if message.content.startswith("별나비 FMS"):
        await message.channel.send("2020년 4월 1일에 시작한 서버로, 잔납님이 오너이십니다!!")


access_token = os.environ["BOT_TOKEN"]
client.run("access_token")




