import logging
from typing import Optional
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

class SimpleTelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.application = Application.builder().token(token).build()

        # Set up logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def start(self, update: Update, context: CallbackContext):
        if update.message:
            await update.message.reply_text('Hello! I am your bot.')

    async def echo(self, update: Update, context: CallbackContext):
        if update.message:
            await update.message.reply_text(update.message.text or "")

    async def error(self, update: Optional[object], context: CallbackContext):
        self.logger.warning(f'Update {update} caused error {context.error}')

    def run(self):
        # Add command and message handlers
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        # Log all errors
        self.application.add_error_handler(self.error)

        # Start the bot
        self.application.run_polling()

if __name__ == "__main__":
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    bot = SimpleTelegramBot('YOUR_TOKEN_HERE')
    bot.run()