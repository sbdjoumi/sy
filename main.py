from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord.ext import commands
import discord
from discord.ext import commands
import logging
import datetime 
import time
import random
from discord.ext import commands
import os
from dotenv import load_dotenv
import discord 

slash = SlashCommand
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('ses connecté ')

bot = commands.Bot(command_prefix='$', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name='ban', description='Bannir un utilisateur du serveur')
@commands.has_permissions(ban_members=True)
async def ban(ctx: SlashContext, user: discord.Member, reason: str = None):
    
    embed = Embed(
        title='Bannissement',
        description=f'Utilisateur banni : {user.name} ({user.id})',
        color=0xFF0000
    )
    embed.add_field(name='Raison', value=reason or 'Aucune raison spécifiée')
    embed.add_field(name='Modérateur', value=ctx.author.name)
    embed.add_field(name='Heure', value=ctx.message.created_at)

 
    channel = user.dm_channel
    if channel is None:
        channel = await user.create_dm()
    messages = await channel.history(limit=100).flatten()

    with open('last_messages.txt', 'w') as f:
        for message in messages:
            f.write(f'{message.author.name} : {message.content}\n')

    with open('last_messages.txt', 'rb') as f:
        last_messages = File(f, 'last_messages.txt')

    
    await ctx.send(file=last_messages, embed=embed)

    
    await user.ban(reason=reason)


bot.run('MTIwNzQxOTI1MTY0ODg4ODk0Mw.GPeHXt.sGVhAbPxzuycHVIXPJalxF4O0wby9eIw_thctU')
