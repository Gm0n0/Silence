from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot's token from BotFather
TOKEN = "8052878806:AAEO-EP0dAWWeiirlKgiY3l_iGNLoi8M0h0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # The URL of your GitHub Pages site
    web_app_url = "https://gm0n0.github.io/Silence/"

    # Create the inline button for the Web App
    keyboard = [
        [InlineKeyboardButton("🛍️ Open Gift Shop", web_app=WebAppInfo(url=web_app_url))]
    ]
    
    # Send a message with the inline button
    await update.message.reply_text("Click below to open the Gift Shop:", reply_markup=InlineKeyboardMarkup(keyboard))

# Create the application with your bot token
application = Application.builder().token(TOKEN).build()

# Add the /start command handler
application.add_handler(CommandHandler("start", start))

# Start polling to keep the bot running
application.run_polling()
