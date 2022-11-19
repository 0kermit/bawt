import discord
import random
from discord.ext import commands
from webserver import keep_alive
import os
import asyncio
from time import sleep

client = discord.Client


activity = discord.Activity(type=discord.ActivityType.watching, name="you")
#bot = commands.Bot(command_prefix="!", activity=activity, status=discord.Status.idle, intents=discord.Intents.default())
bot = commands.Bot(intents=discord.Intents.all(),activity=activity,status=discord.Status.idle,command_prefix=".")
client = discord.Client

@bot.event
async def on_ready():
    print("your bawt is online")


@bot.event
async def on_message(message):
    msg = message.content
    send = message.channel.send
    author = message.author
    reply = message.reply
    react = message.add_reaction
    if author == bot.user:
        return




    if msg == 'ping':
        await send('pong')
    if msg == 'pong':
        await react('🏓')
    if msg == 'sleep':
        await reply('good night')
        sleep(10)
        await send('i have awoken')


    if msg.startswith('massping'):
        if message.author.id == 646878567652786196:
            try:
                await message.delete()
                masspinglist = msg.split(' ', 2)
                target = masspinglist[1]
                times = masspinglist[2]
                if int(times)<=50:
                    for i in range(0,int(times)):
                        await send(target)
                else:
                    await send('enter a number at most 50')
            except:
                await send('missing parameters')
        else:
            await send('sucks to suck')



    if msg == 'delete':
        await message.delete()

    if msg == 'slow':
        for i in range(0,random.randrange(5,15)):
            await send(f'<@{message.author.id}>')

    if msg == '!help':
        await send('no')

    if msg == '!servers':


    await bot.process_commands(message)




keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)
