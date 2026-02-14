# Discord Encouragement Bot 🤖

A friendly Discord bot that spreads positivity by detecting sad messages and responding with encouraging words. Users can also get inspirational quotes and manage custom encouragements.

## Features

- **Automatic Encouragement**: Detects sad words in messages and responds with uplifting encouragements
- **Inspirational Quotes**: Fetches random inspirational quotes from ZenQuotes API
- **Custom Encouragements**: Add, list, and delete custom encouragement messages
- **SQLite Database**: Persistent storage for user-added encouragements


## Setup & Installation

### Prerequisites

- Python 3.13 or higher
- Discord Bot Token
- UV package manager (recommended) or pip

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Discord Chatbot"
```

### 2. Install Dependencies

Using UV (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install discord.py python-dotenv requests
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
TOKEN=your_discord_bot_token_here
```

### 4. Configure Discord Bot Settings

> [!IMPORTANT]
> **Required Discord Bot Intents**
> 
> You must enable the following intents in the [Discord Developer Portal](https://discord.com/developers/applications):
> 
> 1. Navigate to your bot application
> 2. Go to the **Bot** section
> 3. Scroll down to **Privileged Gateway Intents**
> 4. Enable the following:
>    - ✅ **Presence Intent**
>    - ✅ **Server Members Intent**
>    - ✅ **Message Content Intent**
> 
> Without these intents, the bot will not function properly!

### 5. Run the Bot

```bash
python main.py
```

Or with UV:
```bash
uv run python main.py
```

## How It Works

### Automatic Encouragement Detection

The bot monitors all messages for sad words and responds with a random encouragement from the combined list of starter encouragements and user-added custom encouragements.

### Database Management

The bot uses SQLite to store custom encouragements persistently. The database is automatically created on first run with the following schema:

```sql
CREATE TABLE encouragements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    encouragement TEXT NOT NULL
)
```

## Dependencies

- **discord.py** (≥2.3.2): Discord API wrapper
- **python-dotenv** (≥0.9.9): Environment variable management
- **requests** (≥2.32.5): HTTP requests for quote API
- **sqlite3** (≥3.38.0): SQLite database operations

## Example Usage

```
User: I'm feeling sad today
Bot: Hang in there!

User: $inspire
Bot: The only way to do great work is to love what you do. - Steve Jobs

User: $new Keep pushing forward!
Bot: Encouragement added!

User: $list
Bot: ['Cheer up!', 'Hang in there!', ..., 'Keep pushing forward!']

User: $delete Keep pushing forward!
Bot: Encouragement deleted!
```

## Development

### Adding New Commands

Add new commands in `bot.py` using the `@bot.command()` decorator:

```python
@bot.command()
async def mycommand(ctx):
    await ctx.send("Response message")
```

## Reference

This project is based on the freeCodeCamp tutorial:
- **Tutorial**: [Code a Discord Bot with Python - Host for Free in the Cloud](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- **Video Tutorial**: [YouTube - freeCodeCamp.org](https://www.youtube.com/watch?v=SPTfmiYiuok)

---


