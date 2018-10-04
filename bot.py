import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random
import itertools
import json
import os
from discord.utils import get


#open file
#TOKEN = get token from file
#close file?
with open("bot.json") as cfg:
    config = json.load(cfg)

token = config["token"]
prefix = config["command_prefix"]


#TOKEN = "NDk3MTk5OTk2NDI5NDAyMTEy.Dpbtng.fljZm4t1XatYnI826dnl5_G6vAE"
#PREFIX = "frndos "

bot = commands.Bot(command_prefix=prefix)
client = discord.Client()


def getEmojiByName(input):
    return get(bot.get_all_emojis(), name=input)

def getCoolEmoji(ears=False):
    emoji_list = [
    "frndus",
    "jew_basic",
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
    

 
@bot.event
async def on_ready():
    print("I am running on: " + bot.user.name)
    print("with the id: " + bot.user.id)
    #print("setting up...")
    #print("finished")
    print("its gamer time my dude ")
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
        print("ERROR EMOJI: " + rawEmoji + "NOT FOUND REEEEEEEEEEEEEEEE")
    message = random.choice(messages)
    message = ":fire:" + message + ":fire:"
    await bot.send_message(user, message)
    await bot.say("bothered "  + user.name + " with the message: " + message)


bot.run(token)
