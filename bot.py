import os

import  random

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord!!')
@bot.command(name="joke")
async def tell_a_joke(ctx):    
    jokes = [
        "*insert joke here about school*" ,
        "*insert joke about sport*" ,
        "*insert joke about haha funny*"
        #etc etc
    ]

    await ctx.send(random.choice(jokes))
bot.run(DISCORD_TOKEN)    
