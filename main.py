import discord
from discord.ext import commands, tasks
import time
import os
import json

from colorama import Fore 
import requests
import datetime
import asyncio
from asyncio import sleep
import re

import json
import os
import sys
import random



start = datetime.datetime.now()
with open ("rain.json") as f:
  rain = json.load(f)


TOKEN = rain.get("token")
PREFIX = rain.get("prefix")
SNIPER = rain.get("nitrosniper")
SLOT = rain.get("slotsniper")
EMBED = rain.get("embeds")
EMBEDC = rain.get("color")





intents = discord.Intents.all()

client = discord.Client()

client = commands.Bot(command_prefix = PREFIX, self_bot = True,intents=intents, case_insensitive=True)

client.copycat = None


client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed = discord.Embed(description = f"**❌ Command Not Found | Use either (y) or (n) while toggling embeds in config**", color=0x000000)

      await ctx.send(embed=embed)
    
    








@client.event
async def on_connect():
    
    

    if SNIPER == "y" or SNIPER == "Y":
        sniper = "Enabled"
    elif SNIPER == "n":
        sniper = "Disabled"
    else:
        sniper = "Error"

    if SLOT == "y" or SLOT == "Y":
        slot = "Enabled"
    elif SLOT == "n":
        slot = "Disabled"
    else:
        slot = "Error"
    
    if EMBED == "y" or EMBED == "Y":
      embeds = "Toggled"
    elif EMBED == "n":
      embeds = "Disabled"
    else:
      embeds = "Error"


    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    print(
        f"""  {Fore.CYAN}╔═╗┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔╗ ┬ ┬  ╦═╗┌─┐┬┌┐┌
  {Fore.YELLOW}╠═╝│ ││││├┤ ├┬┘ ││  ╠╩╗└┬┘  ╠╦╝├─┤││││
  {Fore.CYAN}╩  └─┘└┴┘└─┘┴└──┴┘  ╚═╝ ┴   ╩╚═┴ ┴┴┘└┘
  {Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {Fore.BLUE}Logged in as: {Fore.RED}[{client.user.name}#{client.user.discriminator}]
  {Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {Fore.BLUE}Servercount: {Fore.RED}[{len(client.guilds)}]
  {Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  {Fore.BLUE}Prefix: {Fore.RED}[{client.command_prefix}]
  {Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  {Fore.YELLOW}[+] Configuration [+]
  {Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Fore.CYAN}
  NitroSniper: {Fore.CYAN}[{sniper}]
  SlotSniper: {Fore.CYAN}[{slot}]
  Embeds: {Fore.CYAN}[{embeds}]

  {Fore.YELLOW}Usage: Snipers + Full Customizable Selfbot
  



"""
    )

#blue , red , cyan , green , orange, grey, yellow, gold, pink, navy, purple
cr = 0x000000

if EMBEDC == "blue" or EMBEDC == "Blue":
  cr = 0x3498DB
else:
  pass
if EMBEDC == "red" or EMBEDC == "RED":
  cr = 0xE74C3C
else:
  pass
if EMBEDC == "cyan" or EMBEDC == "Cyan":
  cr = 0x1ABC9C
else:
  pass
if EMBEDC == "green" or EMBEDC == "Green":
  cr = 0x2ECC71
else:
  pass
if EMBEDC == "orange" or EMBEDC == "Orange":
  cr = 0xE67E22
else:
  pass
if EMBEDC == "grey" or EMBEDC == "Grey":
  cr = 0x95A5A6
else:
  pass
if EMBEDC == "yellow" or EMBEDC == "Yellow":
  cr = 0xFFFF00
else:
  pass
if EMBEDC == "gold" or EMBEDC == "Gold":
  cr = 0xF1C40F
else:
  pass
if EMBEDC == "pink" or EMBEDC == "Pink":
  cr = 0xE91E63
else:
  pass
if EMBEDC == "navy" or EMBEDC == "Navy":
  cr = 0x34495E
else:
  pass
if EMBEDC == "purple" or EMBEDC == "Purple":
  cr = 0x9B59B6
else:
  pass




if EMBED == "y":
  try:
    @client.command()
    async def help(ctx):
      await ctx.message.delete()
      embed = discord.Embed(color=(cr))
      embed.set_author(name="🌧️ Rain Selfbot 🌧️")

      
      embed.add_field(name=f"☔ `Embeds - Toggled ✔️` ", value="\n\u200b", inline=False)
      embed.add_field(name="☔ `config - Customize The Selfbot` ", value="\n\u200b", inline=False)
      embed.add_field(name="☔ `utility - Useful Commands` ", value="\n\u200b", inline=False)
      embed.add_field(name="☔ `fun - Fun Commands` ", value="\n\u200b", inline=False)
      embed.add_field(name="☔ `mod - Server Commands` ", value="\n\u200b", inline=False)
      embed.add_field(name="☔ `rain - Shows Regular Commands` ", value="\n\u200b", inline=False)
      
      
      embed.set_footer(text=f'Powered By Rain™')
      await ctx.send(embed=embed)
  except:
    pass


if EMBED == "n":
  try:
    @client.command()
    async def help(ctx):
      await ctx.message.delete()
      await ctx.send(f"""```fix
☔ Embeds - Disabled ❌

☔ config - Customize The Selfbot

☔ utility - Useful Commands

☔ fun - Fun Commands

☔ mod - Server Commands

☔ rain - Shows Regular Commands ```""")
  except:
    pass






######################################################
######################################################
######################################################
if EMBED == "y":
  try:
    @client.command()
    async def embed(ctx):
      await ctx.message.delete()
      embed = discord.Embed(color=(cr))
      embed.set_author(name="Embeds")

      embed.add_field(name="☔ `Embeds - Toggled ✔️` ", value=f"\n\u200b", inline=False)

      await ctx.send(embed=embed)
  except:
    pass

if EMBED == "n":
  try:
    @client.command()
    async def embed(ctx):
     await ctx.message.delete()
     await ctx.send(f"""```☔ Embeds - Disabled ❌```""")
  except:
    pass



    

######################################################
######################################################
######################################################




@client.command()
async def stealav(ctx, *,  avamember : discord.Member=None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)

    await ctx.send(f'**{member} Was Kicked.**')


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason)
    await ctx.channel.send(f"**{member} Was Banned.**")

@client.command()
async def unban(ctx, *, member):
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'** {user.mention} Is Unbanned !**')
            return

@client.command()
async def coinflip(ctx):
  await ctx.message.delete()
  choices = ["`Heads`","`Tails`"]
  rancoin = random.choice(choices)
  await ctx.send(rancoin)


@client.command()
async def rolldice(ctx):
    await ctx.message.delete()
    message = await ctx.send("`Choose a number:`\n**4**, **6**, **8**, **10**, **12**, **20** ")
    
    def check(m):
        return m.author == ctx.author

    try:
        message = await client.wait_for("message", check = check, timeout = 5.0)
        m = message.content

        if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
            await ctx.send("`Sorry, invalid choice.`")
            return
        
        coming = await ctx.send("`Rolling The Dice`")
        time.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.randint(1, int(m))}**")
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("`Procces has been canceled because you didn't respond in **30** seconds.`")


@client.command(aliases=['8ball'])
async def ball(ctx, *, question):
  responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
  await ctx.send(f'`Question: {question}`\n**Answer: {random.choice(responses)}**')

@client.command()
async def lock(ctx):
    await ctx.message.delete()
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now on lockdown.***")

@client.command()
async def unlock(ctx):
    await ctx.message.delete()
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")


@client.command(pass_context=True)
async def nickname(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)
    await ctx.send(f'***Nickname was changed for {member.mention} ***')



@client.command(pass_contex=True)
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
          pass 



#await client.process_commands(message)















client.run(TOKEN, bot=False)
