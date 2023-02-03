import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "MTA3MTEyMTMzMTY0MDM1MjgzOQ.GBbGQN.RZTp0wa3X-EHl9wbpOPLL9ylNeC2ZK4x5VMRok" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(MTA3MTEyMTMzMTY0MDM1MjgzOQ.GBbGQN.RZTp0wa3X-EHl9wbpOPLL9ylNeC2ZK4x5VMRok)
