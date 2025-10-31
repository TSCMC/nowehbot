from ast import Tuple
import discord
import asyncio
import os
import csv

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

token = os.getenv('NOWEHBOT_TOKEN')
keywordDict = dict()

if not token:
    with open('token.txt', 'r', encoding='utf8') as tokenFile:
        token = tokenFile.read().strip()

# keyword file reading
keywordFileString=''
try:
    keywordFile = open('keywords.csv', 'r', encoding='utf8')
except FileNotFoundError:
    with open('TEMPLATE_keywords.csv','r', encoding='utf8') as keywordFile:
        keywordFileString=keywordFile.read()
        with open('keywords.csv','w',encoding='utf8') as newKeywordFile:
            newKeywordFile.write(keywordFileString)
    keywordFile = open('keywords.csv', 'r', encoding='utf8')

# make dictionary
keywordFileDict = csv.DictReader(keywordFile)
for row in keywordFileDict:
    keywordDict[row['keyword']]=Tuple(row['emojiName'],row['emojiID'])
keywordFile.close()

async def handleMessage(message: discord.Message):
    c = []
    
    filter = '|*_ (){}[];:'
    sanitized_content = message.content.lower()
    for char in filter:
        sanitized_content = sanitized_content.replace(char,'')
    
    for keyword,reaction in keywordDict.items():
        if keyword in sanitized_content:
            c.append(message.add_reaction(f'<:{reaction[0]}:{reaction[1]}>'))
    
    await asyncio.gather(*c)

@bot.event
async def on_message(message: discord.Message):
    await handleMessage(message)

@bot.event
async def on_message_edit(before, after):
    await handleMessage(after)

bot.run(token)
