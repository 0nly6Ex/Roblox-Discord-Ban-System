#Made by 6Ex.
from aiohttp import request
import requests
import discord
from discord.ext import commands
import requests
from discord.ext.commands import cooldown, BucketType

def getID(username):
    check = requests.get("https://api.roblox.com/users/get-by-username?username=" + username)
    checktwo = check.body
    return checktwo["Id"]

bot = commands.Bot(command_prefix='-')
@bot.command(aliases=['b'])
async def whitelist(ctx, arg):
   if str(ctx.message.author.id) == "DISCORDID":
        userid = getID(arg)
        requests.get("https://serverlinkhere/banplayer.php?userid="+str(userid))
        await ctx.send("Successfully banned the following user: \n" + arg)
   else:
        await ctx.send("You do not have permissions to run this command.")


@bot.command(aliases=['ub'])
async def unwhitelist(ctx, arg):
   if str(ctx.message.author.id) == "DISCORDID":
        userid = getID(arg)
        requests.get("https://serverlinkhere/unbanplayer.php?userid="+str(userid))
        
        await ctx.send("Successfully banned the following user: \n" + arg)
   else:
        await ctx.send("You do not have permissions to run this command.")
@bot.event
async def on_ready():    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="myself ban people!"))

    
    print("Bot is ready!")
bot.run('token here')
