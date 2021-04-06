import discord
import os
from stay_awake import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello")


keep_alive()
client.run(os.getenv("TOKEN"))
