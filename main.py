import discord
from discord.utils import get
import time
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Niranth has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    messageContent = message.content.lower()
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message):
        await message.channel.send('bro what the FUCK do you want')

    if message.author.id == 223559283944587264:
        if random.randint(0,50) < 2:
            await message.channel.send("W")
        if messageContent == "bro can i have admin pls?":
            user = message.author
            role = get(user.guild.roles, name=".")
            await user.add_roles(role)
            

    if "real" in messageContent and "niranth" in messageContent:
        if "are" in messageContent and "you" in messageContent and "niranth" in messageContent:
            await message.channel.send("yes")
        else:
            await message.channel.send("awwwww...")

    if messageContent == "niranth":
        await message.channel.send("yea?")
    
    if messageContent == "not you":
        await message.channel.send("awwww...")

    if "game" in messageContent and "should" in messageContent and "i" in messageContent and "play" in messageContent:
        await message.channel.send('you should play fortnite')
    
    if "should" in messageContent and "play" in messageContent and "fortnite" in messageContent:
        await message.channel.send("yes")
    
    if "no " in messageContent:
        await message.channel.send("F")

    if "aw" in messageContent:
        await message.channel.send("L")
    
    if "fuck" in messageContent:
        await message.channel.send("LOL")

client.run('lol you thought I would put this here')