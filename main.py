import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

with open('token.txt', 'r', encoding='utf8') as tokenFile:
    token = tokenFile.read().strip()

@bot.event
async def on_message(message: discord.Message):
    c = []
    if 'weh' in message.content.lower():
        c.append(message.add_reaction('<:noweh:1414871407493517332>'))
    
    if 'mizukicrying' in message.content.lower():
        c.append(message.add_reaction('<:mizukicrying:1397846161250979913>'))
    
    await asyncio.gather(*c)

@bot.event
async def on_message_edit(before, after):
    message = after
    c = []
    
    filter = '|*_ (){}[];:'
    sanitised_content = message.content.lower()
    for char in filter:
        sanitized_content = sanitized_content.replace(char,'')
    
    if ('weh' in sanitized_content) or ('ɥǝʍ' in sanitized_content):
        c.append(message.add_reaction('<:noweh:1414871407493517332>'))
    
    if 'mizukicrying' in sanitized_content:
        c.append(message.add_reaction('<:mizukicrying:1397846161250979913>'))
    
    await asyncio.gather(*c)

bot.run(token)
