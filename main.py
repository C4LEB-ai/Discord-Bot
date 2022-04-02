import os
import discord
import requests #to help us make a https requests API
import json #to ease the process of working with the returned data
client = discord.Client()
TOKEN = "OTU5NDQ4NDgyMzYyNTY4NzI0.YkcCBw.X7PLRcqJAKBkSpRXLy8IhFLY2vk"
def get_quote(): #this is a function we call to make request and get quot from the api
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] +"\n_" + json_data[0]['a'] # loading the json file you see that the ["q"] stands for the quot while ["a"] stands for the author..and[0]stands for the index of the first first quote returned
  return (quote)


@client.event
async  def on_ready():
    print("{0.user} is online".format(client))

@client.event
async  def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("hello") or message.content.startswith("Hello"):
        await message.channel.send("hello from the other side ")

    elif message.content.startswith("how are you") or message.content.startswith("how have you been?"):
        await message.channel.send(f"{client.user.name} is always good, how about you {message.author.name}?")

    elif message.content.startswith("hi") or message.content.startswith("Hi"):
        await message.channel.send(f"hello! {message.author.name} how are you doing today?")

    elif message.content.startswith("Inspired") or message.content.startswith("inspire"):
        quote = get_quote()
        await message.channel.send(quote)
    elif message.content.startswith("thank you") or message.content.startswith("Thank you"):
        quote = get_quote()
        await message.channel.send("Your Welcome")
    elif message.content.startswith("I am fine") or message.content.startswith("I'm fine"):
        quote = get_quote()
        await message.channel.send("Its nice to hear!")
    elif message.content.startswith("what is your name?") or message.content.startswith("What is your name ?"):
        quote = get_quote()
        await message.channel.send("I'm BOT")
client.run(TOKEN)