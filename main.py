import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
from flask import Flask

# TELEGRAM BOT SECTION
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Crypto Bot! Use /price BTCUSDT")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = context.args[0].upper()
    await update.message.reply_text(f"Price for {symbol}: $1234.56 (demo)")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

# FLASK DUMMY SERVER FOR RENDER
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

def run_bot():
    app.run_polling()

# RUN BOTH
if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    run_bot()

  
