from bot import bot
import os
from dotenv import load_dotenv

load_dotenv()

# Run the server
bot.run(os.getenv('TOKEN'))
