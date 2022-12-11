import secrets
import discord
from discord.ext import commands
import wavelink
import os

client = discord.Client()

client.run(os.environ['bot_token'])