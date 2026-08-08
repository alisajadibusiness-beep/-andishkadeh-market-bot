import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

app = Flask(__name__)


@app.route("/")
def home():
    return "Andishkadeh Market Bot is running."


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🎓 به اندیشکده مدیریت و بازار خوش آمدید

مرجع آموزش و محتوای کاربردی در حوزه:

📚 مدیریت و کسب‌وکار
🌍 تجارت بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
🏦 بانکداری
🎓 آزمون و منابع آموزشی

از منوی ربات موضوع موردنظر خود را انتخاب کنید.
"""
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات اندیشکده مدیریت و بازار\n\n"
        "برای شروع، دستور /start را ارسال کنید."
    )


def run_flask():
    app.run(host="0.0.0.0", port=PORT)


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است.")

    Thread(target=run_flask, daemon=True).start()

    telegram_app = Application.builder().token(TOKEN).build()

    telegram_app.add_handler(CommandHandler("start", start))
    telegram_app.add_handler(CommandHandler("help", help_command))

    telegram_app.run_polling()


if __name__ == "__main__":
    main()
