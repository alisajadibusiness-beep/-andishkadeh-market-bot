import os
from flask import Flask
from threading import Thread
from from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from menus import main_menu, trade_menu
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

app = Flask(__name__)


@app.route("/")
def home():
    return "Andishkadeh Market Bot is running."


def 
    keyboard = [
        [
            InlineKeyboardButton("📚 آموزش مدیریت", callback_data="management"),
            InlineKeyboardButton("🌍 تجارت بین‌الملل", callback_data="trade"),
        ],
        [
            InlineKeyboardButton("📈 بازاریابی و فروش", callback_data="marketing"),
            InlineKeyboardButton("💰 اقتصاد و بازار", callback_data="economy"),
        ],
        [
            InlineKeyboardButton("🏦 بانکداری", callback_data="banking"),
            InlineKeyboardButton("🎓 آزمون و تست", callback_data="exam"),
        ],
        [
            InlineKeyboardButton("📂 فایل و جزوات", callback_data="files"),
            InlineKeyboardButton("📱 شبکه‌های اجتماعی", callback_data="social"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


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

👇 موضوع موردنظر خود را انتخاب کنید:
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )

if query.data == "trade":
    await query.edit_message_text(
        "🌍 تجارت بین‌الملل\n\n"
        "موضوع موردنظر خود را انتخاب کنید:",
        reply_markup=trade_menu()
    )
    return
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات\n\n"
        "برای مشاهده منوی اصلی، /start را ارسال کنید."
    )

شبکه‌های اجتماعی اندیشکده مدیریت و بازار."
        ),
    }

    text = sections.get(
        query.data,
        "گزینه موردنظر پیدا نشد."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 بازگشت به منوی اصلی",
                callback_data="home"
            )
        ]
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def home_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = """
🎓 اندیشکده مدیریت و بازار

👇 از منوی زیر یک بخش را انتخاب کنید:
"""

    await query.edit_message_text(
        text,
        reply_markup=main_menu()
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

    telegram_app.add_handler(
        CallbackQueryHandler(home_button, pattern="^home$")
    )

    telegram_app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    telegram_app.run_polling()


if __name__ == "__main__":
    main()
