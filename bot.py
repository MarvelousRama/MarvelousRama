# Importing the required modules
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import urllib.parse

# Function to extract the direct link after 'link=' from the long URL
def extract_direct_link(long_url):
    # Parse the long URL
    parsed_url = urllib.parse.urlparse(long_url)
    
    # Extract query parameters
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    # Check if 'link' is present in the query parameters
    if 'link' in query_params:
        # Extract the value of 'link'
        direct_link = query_params['link'][0]
        return direct_link
    else:
        return "No 'link=' found in the URL."

# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Hi! Send me a URL containing 'link=', and I'll extract the direct link for you.")

# Function to handle incoming messages
def handle_message(update, context):
    user_message = update.message.text
    direct_link = extract_direct_link(user_message)
    update.message.reply_text(f"Direct link: {direct_link}")

# Main function to set up the bot
def main():
    # Replace 'YOUR_TELEGRAM_BOT_API_TOKEN' with your actual bot token from BotFather
    TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
    
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Register command handler for the /start command
    dp.add_handler(CommandHandler("start", start))
    
    # Register message handler to process any text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start the bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C
    updater.idle()

# Entry point for the bot
if __name__ == '__main__':
    main()
