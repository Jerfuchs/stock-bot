from apis.yfApi import *
from programy.clients.embed.basic import EmbeddedBasicBot
import discord
from discord.ext import commands
from config.config import *
import typing as t
from optional import Optional

bot = commands.Bot(command_prefix='-') #Bot listening to @client.commands() / Currently not active due to on_message

stock_bot = EmbeddedBasicBot() #Bot initialised/ Extend to Stock Bot

@bot.event #Start Signal if bot is online
async def on_ready():
    print('I am alive')
    channel = bot.get_channel(500228562817908756) #general Channel Bachelor of Stupidity

    #await channel.send('Hello there im stock-bot and here is my Command List:')
    #await channel.send('```In developement\n Version 0.5```' )
    #await channel.send('Or just Chat with me')


@bot.command()   #Test command
async def q(ctx):
    question = ctx.message.clean_content[2:]
    answer = getLastPrice(question)
    if(answer is None):
        answer = 'I dont know what you mean'
    else:
        answer = answer +'Is the current stock price'

    await ctx.send(answer)


@bot.command()  #test for tagging user
async def mention1(ctx, user: discord.Member):
  await ctx.send(user.mention + 'Kein CSGO zocken jetzt')


@bot.listen('on_message') # trigger on message (Where Bot talks with you)
async def talk(ctx):
    if ctx.author.bot: #If statement so the bot doesn't message itself
        return

    if (ctx.clean_content == "join"):   #Bot join (channel you are in)
        await join(ctx)
        return

    if (ctx.clean_content == "leave"):  #Bot leave (channel you are in)
        await leave(ctx)
        return


    answer = stock_bot.ask_question(ctx.clean_content)
    if (answer is None): # If bot doesn't understand language = ''/ Counter empty message send error
        answer = 'I dont know what you mean'

    channel = bot.get_channel(ctx.channel.id)
    await channel.send(answer)



#Bot join and disconnect from server / works
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.guild.voice_client.disconnect()


bot.run(TOKEN) # actually start the bot in discord


