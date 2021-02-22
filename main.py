import discord
import os

client = discord.Client()

bad_words = ['word_1', 'word_2', 'word_3', 'word_4']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if any(word in msg for word in bad_words):
    await message.channel.send("Warning: do not use profanity.")

  if msg == "!meetingtime":
    await message.channel.send("The meeting is at 9:00 PM. The zoom link was sent via email")

client.run(os.getenv('TOKEN'))