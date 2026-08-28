import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "").strip()

# Tiny web server so Render Free doesn't complain
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(
            "Hey! 👋 I'm offline right now.\n"
            "Leave your message and I'll get back to you ASAP.\n"
            "Working hours: 09:00 - 18:00 Italy time"
        )

if __name__ == "__main__":
    # Start web server in background
    Thread(target=run_flask, daemon=True).start()
    
    print("Bot is running 24/7...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    app.run_polling()
