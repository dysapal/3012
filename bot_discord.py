import discord
import random
import os
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left + right)
@bot.command()
async def minus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left - right)
@bot.command()
async def multiplied(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left * right)
@bot.command()
async def divided(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left / right)
@bot.command()
async def powered(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left ** right)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("tu token")
