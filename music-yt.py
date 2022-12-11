import secrets
import discord
from discord.ext import commands
import wavelink
import os

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    client.loop.create_task(connect_nodes()) # HTTPS and websocket operations
    
async def connect_nodes():
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(
        bot=client,
        host='0.0.0.0',
        port=2333,
        password='youshallnotpass'
    )
    
@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node: <{node.identifier}> is ready')

client.run(os.environ['bot_token'])