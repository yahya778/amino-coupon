
import discord
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='!')


@bot.command()
async def open1(ctx):
	embed=discord.Embed(title="صفحة القران 1")
	embed.set_image(url="https://i.ibb.co/Jz77x4s/001.gif")
	embed.set_footer(text="بوت القران")
	await ctx.send(embed=embed)

@bot.command()
async def open3(ctx):
	embed=discord.Embed(title="صفحة القران3")
	embed.set_image(url="https://i.ibb.co/hf7cC1f/page-003.jpg")
	embed.set_footer(text="بوت القران")
	await ctx.send(embed=embed)



@bot.command()
async def open2(ctx):
	embed=discord.Embed(title="صفحة القران 2")
	embed.set_image(url="https://i.ibb.co/8BFt5ck/images-9.jpg")
	embed.set_footer(text="بوت القران")
	await ctx.send(embed=embed)


bot.run("ODI2ODc4NjMzMDcwNDI4MTkw.YGS4vA.a_QxXiSbizA_PG2PcvYyMjXt7mk")