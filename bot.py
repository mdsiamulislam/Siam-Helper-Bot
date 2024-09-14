from typing import Final, Dict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import sys
import io

# Set UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Constants
TOKEN: Final = '7237718794:AAGaC03mxeTKOC4SOlXA6hDiPxpL-c7L0fE'
BOT_USERNAME: Final = '@siam_helper_bot'

# Global dictionary to store filters
filters_dict: Dict[str, str] = {}

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    await update.message.reply_text('Welcome to Siam Helper Bot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command."""
    help_message = """
/start - Start the bot
/help - Show help message
/add_filter <key> <response> - Add a new filter key and response
/remove_filter <key> - Remove a filter key
/list_filters - List all filter keys
    """
    await update.message.reply_text(help_message)

async def add_filter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /add_filter command."""
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text('Usage: /add_filter <key> <response>')
            return

        key = args[0].lower()
        response = update.message.text.split(' ', 2)[2].strip()  # Capture multiline response
        filters_dict[key] = response
        await update.message.reply_text(f'Filter added: "{key}"')
    
    except Exception as e:
        await update.message.reply_text(f'Error: {str(e)}')

async def remove_filter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /remove_filter command."""
    try:
        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Usage: /remove_filter <key>')
            return
        
        key = args[0].lower()
        if key in filters_dict:
            del filters_dict[key]
            await update.message.reply_text(f'Filter "{key}" removed.')
        else:
            await update.message.reply_text(f'Filter "{key}" not found.')
    
    except Exception as e:
        await update.message.reply_text(f'Error: {str(e)}')

async def list_filters_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /list_filters command and show clickable buttons for each filter."""
    if filters_dict:
        keyboard = [
            [InlineKeyboardButton(key, callback_data=key)] for key in filters_dict.keys()
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on a filter to see the response:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("No filters found.")

# Callback Query Handler
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button click events."""
    query = update.callback_query
    await query.answer()

    filter_key = query.data
    if filter_key in filters_dict:
        response = filters_dict[filter_key]
        await query.message.reply_text(response)
    else:
        await query.message.reply_text('Filter not found.')

# Message Handler
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages and apply filters."""
    message_type: str = update.message.chat.type
    text: str = update.message.text.lower()

    if message_type == 'group':
        for key, response in filters_dict.items():
            if key in text:
                await update.message.reply_text(response)
                return

# Error Handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors."""
    print(f'Update {update} caused error {context.error}')

# Main function to start the bot
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('add_filter', add_filter_command))
    app.add_handler(CommandHandler('remove_filter', remove_filter_command))
    app.add_handler(CommandHandler('list_filters', list_filters_command))

    # Add message handler
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    # Add callback query handler for button clicks
    app.add_handler(CallbackQueryHandler(button_click))

    # Add error handler
    app.add_error_handler(error_handler)

    # Run the bot
    app.run_polling(poll_interval=1)
