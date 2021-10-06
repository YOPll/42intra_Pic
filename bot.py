import discord
from discord import client
from discord.embeds import Embed
import requests
import creds
from discord.ext import commands


bot = commands.Bot(command_prefix='*', description='Your Description')
bot.remove_command('help')




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Future is loading ...')
    print('----------------------------------------------------------')
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(name='*help || YOPI'))



@bot.command()
async def intra42(ctx):
    content = ctx.message.content
    author = ctx.message.author.id
    arr = content.split(" ", 1)
    imgex = ".jpg"
    URL = "https://cdn.intra.42.fr/users/large_"
    x = len(content.split())
    if x > 1:
        y = 1
    else:
        y = 0
    msg = arr[y].strip(" ")
    r = requests.get(URL+msg+imgex)
    link = URL+msg+imgex
    if r.status_code  == 200:
        embed=discord.Embed()
        embed.set_image(url=link)
        await ctx.send(embed=embed)
    elif y == 0:
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter username, Example : *intra42 zyacoubi',color = ctx.author.color)
        await ctx.send(embed = yopi)
    elif r.status_code == 404:
        yopi = discord.Embed(title = 'User_Not_Found', description = f'Sorry <@{author}> we couldn\'t find {msg} picture.',color = ctx.author.color)
        await ctx.send(embed = yopi)

@bot.command()
async def whomadeu(ctx):
        yopi = discord.Embed(title = 'Syntax_error', description = f'Sorry <@{author}> Please enter username, Example : *intra42 zyacoubi',color = ctx.author.color)
    await ctx.send(f'<@254700247471751171>')

bot.run(creds.token)
