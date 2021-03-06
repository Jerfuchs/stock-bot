from programy.clients.embed.datafile import EmbeddedDataFileBot

from apis.yfApi import *
from programy.clients.embed.basic import EmbeddedBasicBot
import discord
from discord.ext import commands
from config.config import *
import typing as t
from google_trans_new import google_translator
from sparql.dbpedia import DBpedia

# from optional import Optional

translator = google_translator()
bot = commands.Bot(command_prefix='-')  # Bot listening to @client.commands() / Currently not active due to on_message

stock_bot = EmbeddedDataFileBot(files, defaults=True)  # Bot initialised/ Extend to Stock Bot


@bot.event  # Start Signal if bot is online
async def on_ready():
    print('I am alive')
    # channel = bot.get_channel(500228562817908756) #general Channel Bachelor of Stupidity

    # await channel.send('Hello there im stock-bot')


@bot.listen('on_message')  # trigger on message (Where Bot talks with you)
async def talk(ctx):
    if ctx.author.bot:  # If statement so the bot doesn't message itself
        return

    db = DBpedia()
    flag = False
    command = ctx.clean_content
    answer = db.askDbpedia(command)
    command = translator.translate(ctx.clean_content, lang_src="de", lang_tgt="en")
    if answer == "Not Found":
        flag = True
        answer = stock_bot.ask_question(command)
        if answer is None:  # If bot doesn't understand language = ''/ Counter empty message send error
            answer = 'I dont know what you mean'

        if "get" in command:
            answer = get_api_answer(command, answer)
    if flag:
        answer = translator.translate(answer, lang_src="en", lang_tgt="de")
    channel = bot.get_channel(ctx.channel.id)
    await channel.send(answer)  # Text to speech is that the bot speaks out loud ,tts=True


bot.run(TOKEN)  # actually start the bot in discord
