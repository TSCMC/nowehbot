import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

with open('token.txt', 'r', encoding='utf8') as tokenFile:
    token = tokenFile.read().strip()

noweh = None
nomizukycrying = None

@bot.event
async def on_message(message: discord.Message):
    print(message.content)
    c = []
    if 'weh' in message.content.lower():
        c.append(message.add_reaction('<:noweh:1414871407493517332>'))
    
    if 'mizukicrying' in message.content.lower():
        c.append(message.add_reaction('<:mizukicrying:1397846161250979913>'))
    
    await asyncio.gather(*c)

bot.run(token)