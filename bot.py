import discord
from discord.ext import commands
from database.sqlite_db import SQLiteDatabase
from services.encouragements import EncouragementService
from services.quotes import QuoteService
from dotenv import load_dotenv

load_dotenv()

SAD_WORDS = ['sad', 'depressed', 'unhappy', 'miserable', 'sorrowful', 
             'gloomy', 'melancholy', 'dejected', 'down', 'blue', 'heartbroken', 
             'lonely', 'hopeless', 'despairing', 'grief-stricken', 'mournful', 
             'wistful', 'somber', 'forlorn', 'crestfallen']

STARTER_ENCOURAGEMENTS = [
    "Cheer up!",
    "Hang in there!",
    "You've got this!",
    "Keep your head up!",
    "Stay strong!",
    "Don't give up!",
    "You're doing great!",
    "Keep going!",
    "You're capable of amazing things!",
    "Believe in yourself!"
]

db = SQLiteDatabase('database.db')
db.create_table()
encouragement_service = EncouragementService(db, STARTER_ENCOURAGEMENTS)
quote_service = QuoteService()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
            return
    if any(word in message.content.lower() for word in SAD_WORDS):
        await message.channel.send(encouragement_service.get_random_encouragement())

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    name = ctx.author.name
    await ctx.send(f"Hello {name}")

@bot.command()
async def inspire(ctx):
    await ctx.send(quote_service.get_quote())

@bot.command()
async def new(ctx, *, new_encouragement):
    encouragement_service.add_encouragements(new_encouragement)
    await ctx.send("Encouragement added!")

@bot.command()
async def list(ctx):
    await ctx.send(encouragement_service.get_encouragements())

@bot.command()
async def delete(ctx, *, encouragement):
    encouragement_service.delete_encouragement(encouragement)
    await ctx.send("Encouragement deleted!")

