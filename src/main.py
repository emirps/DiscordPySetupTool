import time as t
import pathlib
print('Welcome to Discord.py Bot Creator!')
print('Made with love by github.com/kjonaas')
tok=input("Let's start off. What's your Bot Token? ")
prefix=input("Alright! Let's move on. What do you want your prefix to be? ")
print('Setting up with basic moderator commands... ')
t.sleep(2)
file=pathlib.Path('bot.py')
if file.exists():
    f=open("bot.py",'w')
else:
    f=open('bot.py', 'x')
f.write(f"""
import discord
import discord.utils
from discord.ext import commands
bot=commands.Bot(command_prefix='{prefix}')
async def on_ready():
    print('Logged in')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguments')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, you don't have permissions.")
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed=discord.Embed(title='Banned a member')
    embed.add_field(name='Member Banned', value=f'⛔ Banned '+member.name)
    await ctx.send(embed=embed)
bot.run('{tok}')
""")
print('The bot has been set up with one command - it can only ban at the moment :).')
