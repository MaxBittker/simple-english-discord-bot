import discord
import re
import os
from common_words import common_words

wordSet = set(common_words)

bot = discord.Client()
prefix = "/"


@bot.event
async def on_ready():
    print("Online")


@bot.event
async def on_message(message):
    if "simple" not in message.channel.name.lower():
        return
    if message.author.name == "simple-english":
        return

    msg = re.sub(r'[^\w\s]', '', message.content)

    words = msg.split(" ")
    recon = ""
    passes = True
    for word in words:
        lw = word.lower();
        if word.isnumeric() or (lw in wordSet) or (lw[-1] == "s" and (lw[:-1] in wordSet)):
            recon += word + " "
        else:
            print(word + " was bad")
            recon += "#" * len(word) + " "
            passes = False

    if passes:
        return
    # if message.content.startswith(prefix + "say"):
    await message.delete()
    await message.channel.send('{0.name}: {1}'.format(message.author, recon))


bot.run(os.getenv("API_KEY"))
