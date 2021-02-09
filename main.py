import pandas as pd

from programy.clients.embed.basic import EmbeddedBasicBot
import discord
from discord.ext import commands
import yfinance as yf
from datetime import datetime

client = commands.Bot(command_prefix='')

my_bot = EmbeddedBasicBot()

@client.event
async def on_ready():
    print('I am alive')
    channel = client.get_channel(500228562817908756)
    #await channel.send('Hello there im stock-bot and here is my Command List:')
    #await channel.send('``` q <question> for Question\n s <stock name> for Stock information\n r for random fact\n j for a joke from me```' )

@client.command()
async def q(ctx):
    question = ctx.message.clean_content[1:]
    answer = my_bot.ask_question(question)
    if(answer is None):
        answer = 'I dont know what you mean'

    await ctx.send(answer)

@client.command()
async def s(ctx):


    date_format = "%Y-%m-%d"
    today = datetime.today().strftime(date_format)
    start = datetime.date(pd.Timestamp(datetime.today())).strftime(date_format)
    df = yf.download('GC=F', start=start, end=today, progress=False)
    answer = str(df["Close"].tolist()[-1])

    await ctx.send(answer)

@client.command()
async def j(ctx):
    answer = my_bot.ask_question('Can you tell me a joke')
    await ctx.send(answer)


@client.command()
async def mention1(ctx, user : discord.Member):
  await ctx.send(user.mention + 'Kein CSGO zocken jetzt')

@client.listen('on_message')
async def talk(ctx):
    if ctx.author.bot:
        return

    answer = my_bot.ask_question(ctx.clean_content)
    if (answer is None):
        answer = 'I dont know what you mean'

    channel = client.get_channel(ctx.channel.id)
    await channel.send(answer)


client.run('ODA3OTEzNTk4NjEyNDA2Mjgy.YB-6LA.lbNpCx0UVwq4jOSPOkHnWfjG9Kg')


