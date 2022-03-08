from discord.ext import commands
from myserver import server

TOKEN = "MASUKKAN TOKEN BOT DISINI" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

bot.run(TOKEN)