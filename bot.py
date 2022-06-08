import os
import random

import discord

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now Online!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    jokes = [
        "*insert joke here about school*" ,
        "*insert joke about sport*" ,
        "*insert joke about haha funny*"
        #etc etc
    ]
    when_to_tell_joke = [
        "Tell me a joke!" ,
        "tell me a joke" ,
        "I am bored" ,
        "Tell me a joke"

        #etc.
    ]

    if message.content in when_to_tell_joke:
        await message.channel.send(random.choice(jokes))
client.run(DISCORD_TOKEN)        
            