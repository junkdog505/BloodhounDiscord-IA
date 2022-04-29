import discord 
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

import nltk
nltk.download('omw-1.4')
chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
print("Bot running ...")

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('bot'):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

client.run(TOKEN)