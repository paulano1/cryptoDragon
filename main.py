# This example requires the 'message_content' intent.

import discord
import markets
import os
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
token = os.getenv('token')
client = discord.Client(intents=intents)
now = datetime.now()
dt_hr = int(now.strftime("%H"))
newsChannelID = 1011652427365228682

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_ready():
    #if dt_hr == 10:
    print("bot:user ready == {0.user}".format(client))
    channel = client.get_channel(newsChannelID)
    await channel.send("checking news channel {dt_hr}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Roles
async def dm_about_roles(member):
    print(f"DMing {member.name}...")

    await member.send(
        f"""Hi {member.name}, welcome to {member.guild.name}! Drexel's own decentralised community
        
        A few things:
        - Please introduce yourself in the #introductions channel
        - Review the server rules on the rule-board 
        - Verify your Drexel email via bot-commands to get access to all the channels
        - Make sure you join us at https://dragonlink.drexel.edu/organization/drexelblockchain    
"""
    )



client.run(token)
