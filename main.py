# This example requires the 'message_content' intent.

import discord
import os

intents = discord.Intents.default()
intents.message_content = True
token = os.getenv('token')
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#client.run('MTAxMTY1NzQ3MTgyMTA5OTE2OA.GhRUuU.fGroURMPPajT8T-dUMPowJ6FNe2wQi_VfbEq24')
#client.run('MTAxMTY1NzQ3MTgyMTA5OTE2OA.GSd7km.96bO2sbo3Zs8VLWW5RNqDXFhMliC5lpcQZbpAk')
client.run(token)
