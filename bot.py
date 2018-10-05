import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random
import itertools
import json
import os
import random
from time import sleep
from discord.utils import get



__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname("bot.json")))
with open(__location__ + "\\bot.json") as cfg:
    config = json.load(cfg)

token = config["token"]
prefix = config["command_prefix"]


bot = commands.Bot(command_prefix=prefix)
client = discord.Client()

def getInsult():
    insultList = [
        "finger",
        "fatso",
        "diapyhead",
        "fingro",
        "diapy farty fingro brain idiot dumdum blaster",
        "poopoopeepeeface",
        "berny",
        "pipper",
        "ddosface",
        "cunt",
        "smoothbrain",
        "ddos victim"
    ]
    return random.choice(insultList)

def getEmojiByName(input):
    return get(bot.get_all_emojis(), name=input)

def getCoolEmoji(ears=False):
    emoji_list = [
    "frndus",
    "viper",
    "fuck12",
    "scEybbus",
    "vsauce",
    "samloka",
    "boomer",
    "bogpepe",
    "ultrafastparrot",
    "jeffu"
    ]
    if ears:
        return ":" + random.choice(emoji_list) + ":"
    else:
        return random.choice(emoji_list)

def niceTry():
    return "nice try, {}".format(getInsult())
    

@bot.event
async def on_ready():
    print("I am running on: " + bot.user.name)
    print("with the id: " + bot.user.id)
    sleep(0.5)
    print("fastening diaper")
    sleep(0.5)
    print("got my rice dude")
    sleep(0.5)
    print("my power supply", end='')
    for i in range(5):
        print('.', end='', flush=True)
        sleep(0.5)
    sleep(0.5)
    print()
    print("its gamer time my dude ")
    sleep(0.5)
    print ("----------------------------------------------")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")

@bot.command(pass_context=True)
async def fingers(ctx):
    await bot.say(":hand_splayed:")

@bot.command(pass_context=True)
async def bother(ctx, user: discord.Member):
    messages = [
        "eat fingers.....",
        "ÉTA BÖRN... mmmmMMmmmm",
        "BRAAAAAAAAAAAAAAAAP",
        "I EAT LITEL FINGROS LIKE U 4 BREKFIS",                
        "HAHAHAHAHAHA",
        "king ass ripper right here",
        "hormel chili and beans",
        "snnnnniiiiiiffffffffffff...oh yes my dear....sssnnnnnnnnnnnniiiiiiiiffffffff....quite pungent indeed...is that....dare I say....sssssssnniff...eggs I smell?......sniff sniff....hmmm...yes...quite so my darling....sniff....quite pungent eggs yes very much so .....ssssssssssssssnnnnnnnnnnnnnnniiiiiiiffffff....ah yes...and also....a hint of....sniff....cheese.....quite wet my dear....sniff...but of yes...this will do nicely....sniff.....please my dear....another if you please....nice a big now....",
        "beni borðar norgnafingures",
        "tybi xd",
        "fokkin",
        "haha....fyndið...",
        "fucking gamer",
        " https://pbs.twimg.com/profile_images/819461052136099840/ye_cF0Mi_400x400.jpg ",
        " https://i.pinimg.com/originals/cf/e6/21/cfe62168c7bc802e1dce030f23fa463b.jpg "


    ] # I do not approve of this
    rawEmoji = getCoolEmoji()
    emoji = getEmojiByName(rawEmoji)
    if(emoji):
        await bot.add_reaction(ctx.message, emoji)
    else:
        print("ERROR EMOJI: {} NOT FOUND REEEEEEEEEEEEEEEE".format(rawEmoji))
    message = random.choice(messages)
    message = ":fire:" + message + ":fire:"
    await bot.send_message(user, message)
    await bot.say("bothered {} with the message: {}".format(user.name, message))


@bot.command(pass_context=True)
async def insult(ctx): 
    await bot.say("{} you {}".format(ctx.message.author.mention, getInsult()))
    
@bot.command(pass_context=True)
async def pizza(ctx):

    message = ctx.message.content.split()
    if len(message) != 2:
        await bot.say(niceTry())
        return
    else:
        message = message[-1]
        if message == "0":
            await bot.say("nice try idiot")
            return
        elif message.isdigit():
            numpizza = random.randint(1, int(message))
            await bot.say("how about a large number " + str(numpizza) + " with extra cheese you fat fuck")
        else:
            await bot.say("enter a number, {}".format(getInsult()))


@bot.command(pass_context=True)
async def rare(ctx):

    dir =__location__ + "\\rare"

    await bot.send_file(ctx.message.channel, dir + "\\" + random.choice(os.listdir(dir)))


bot.run(token)