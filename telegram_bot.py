#!/usr/bin/env python3

from telegram.ext import Application, CommandHandler, MessageHandler, filters
# Define your bot's token (from BotFather)
BOT_TOKEN = "YOUR-TOKEN-GOES-HERE"

# Start command handler
async def start(update, context):
    await update.message.reply_text("Hello! I'm your bot. How can I help you?")

# Echo message handler
async def echo(update, context):
    await update.message.reply_text(f"You said: {update.message.text}")

# Main function
def main():
    # Create the Application and pass in your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
