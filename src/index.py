import discord

from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix=">", description="This is a helper bot")

@bot.command()
async def ping(ctx):
   await ctx.send('pong')


@bot.command()
async def love(ctx):
    await ctx.send('Love you, I currently developing here, dont forget that I love you!')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server of Skill pro for Call of Duty WarZone", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.created_owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://d1lss44hh2trtw.cloudfront.net/assets/article/2020/03/20/call-of-duty-warzone-crosses-30-million-player-milestone_feature.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def sum(ctx,numOne: int, numTwo: int):
   await ctx.send(numOne+numTwo)


#Events

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Call of Duty Warzone", url="https://www.twitch.tv/spunisher09/videos"))
    print("My Bot is Ready")

bot.run('NzAyNjkzMjMwMDk3MjAzMzEw.XqDwHA.WwWd1OiKrTD8WNkBZP6qc4WyX9Y')