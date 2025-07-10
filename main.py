import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

import os
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to CRYPTO BOT! Use /price <symbol> to get started.")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /price <symbol>\nExample: /price BTCUSDT")
        return

    symbol = context.args[0].upper()
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        data = response.json()
        if "price" in data:
            await update.message.reply_text(f"The current price of {symbol} is ${float(data['price']):,.2f}")
        else:
            await update.message.reply_text("Invalid symbol or API issue.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
