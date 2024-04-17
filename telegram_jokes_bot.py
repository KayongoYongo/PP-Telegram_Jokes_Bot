import os
from dotenv import load_dotenv
import telebot
from jokes import get_jokes

# load environmental variables from .env file
load_dotenv()

# Access the variables
BOT_TOKEN = os.getenv("API_TOKEN")
username = os.getenv("USERNAME")

# Create an instance of the bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    This function will handle welcoming the user

    Args:
        message: This will be the text that will trigger the function
    """
    # This messsage loads when the bot is started
    bot.reply_to(message, "Hello! Wanna hear a Joke?")

@bot.message_handler(commands=['category'])
def category_handler(message):
    """
    This function will handle the sign of the horoscopes

    Args:
        message: This will be the text that will trigger the function
    """
        
    text = "What category do you like?\nChoose one: *Programming*, *Pun*, *Spooky* and *Christmas*."

    # sends a message from the bot to the chat
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

    # review the syntax of the register_next_step_handler
    bot.register_next_step_handler(sent_msg, fetch_jokes)

def fetch_jokes(message):
    """
    This function will handle the day of the horoscopes

    Args:
        category: This will be the text that will trigger the function
    """
    category = message.text
    data = get_jokes(category)
    print(data)
    setup = data["setup"]
    delivery = data["delivery"]
    joke_message = f"*Setup:* {setup}\n*Delivery:* {delivery}"
    bot.send_message(message.chat.id, "Here's your joke")
    bot.send_message(message.chat.id, joke_message, parse_mode="Markdown")

# starts the bot and continuously polls for new messages from users.
bot.infinity_polling()