import discord
import os
#brings in https calls
import requests
import json
import random

from keep_alive import keep_alive

client = discord.Client()

# word scanner list
sad_words = [
  "sad", 
  "depressed", 
  "unhappy", 
  "angry", 
  "miserable", 
  "depressing"
]
# replies to encouragements
encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]


# http get
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  # translare json
  json_data = json.loads(response.text)
  quote =  json_data[0]['a'] + " just once said " + json_data[0]['q']
  return(quote)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # shorthandle 
  msg = message.content

  # random quotes by command
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  # word scanner
  if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(encouragements))



keep_alive()
client.run(os.getenv('TOKEN'))