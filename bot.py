import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("8782321567:AAF2KsioL_NEQxrwBOlnaktvU08kf2hNn4M")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey! 👋 I'm offline right now.\n"
        "Leave your message and I'll get back to you ASAP.\n"
        "Working hours: 09:00 - 18:00 Italy time"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
print("Bot is running 24/7...")
app.run_polling()
