# This example requires the 'message_content' intent.

import discord
import markets
import os
from datetime import datetime
import praw
import random

#Reddit
client_id = os.getenv('reddit_client_id') 
client_secret = os.getenv('reddit_client_secret')
user_id = os.getenv('reddit_username')
user_password = os.getenv('user_pass')
user_agent = os.getenv('reddit_useragent')
reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_id = user_id, user_password = user_password, user_agent = user_agent)
subreddit = reddit.subreddit("cryptocurrencymemes")

#discord.py
intents = discord.Intents.default()
intents.message_content = True
token = os.getenv('token')
client = discord.Client(intents=intents)
now = datetime.now()
dt_hr = int(now.strftime("%H"))
newsChannelID = 1011652427365228682
marketChannelID = 1011652427365228681

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_ready():
    if dt_hr == 12:
        print("bot:user ready == {0.user}".format(client))
        channel = client.get_channel(newsChannelID)
        await channel.send(f"checking news channel {dt_hr}")

@client.event
async def on_ready():
    if dt_hr == 12:
        print("bot:user ready == {0.user}".format(client))
        channel = client.get_channel(marketChannelID)
        await channel.send(f"checking market channel {dt_hr}")


#memes
@client.command()
async def meme(ctx):
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url = url)
    await ctx.send(embed = em)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    



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
