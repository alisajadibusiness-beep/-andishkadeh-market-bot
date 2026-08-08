import os
from threading import Thread

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from menus import main_menu, trade_menu


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

👇 موضوع موردنظر خود را انتخاب کنید:
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات\n\n"
        "برای مشاهده منوی اصلی، /start را ارسال کنید."
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "trade":
        await query.edit_message_text(
            "🌍 تجارت بین‌الملل\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=trade_menu()
        )
        return

    sections = {
        "trade_learning": (
            "📘 آموزش تجارت بین‌الملل\n\n"
            "آموزش مفاهیم پایه و تخصصی تجارت بین‌الملل."
        ),
        "trade_import_export": (
            "🚢 واردات و صادرات\n\n"
            "آشنایی با فرآیندهای واردات، صادرات و مراحل انجام معاملات."
        ),
        "trade_documents": (
            "📑 اسناد و قراردادهای تجاری\n\n"
            "معرفی اسناد مهم تجاری و اصول قراردادهای بین‌المللی."
        ),
        "trade_incoterms": (
            "🌐 اینکوترمز\n\n"
            "آشنایی با قواعد اینکوترمز و مسئولیت‌های خریدار و فروشنده."
        ),
        "trade_payment": (
            "💳 پرداخت‌های بین‌المللی\n\n"
            "آشنایی با روش‌های پرداخت و تسویه در تجارت بین‌الملل."
        ),
        "trade_logistics": (
            "🚚 حمل‌ونقل و لجستیک\n\n"
            "آشنایی با روش‌های حمل، لجستیک و جابه‌جایی کالا."
        ),
        "trade_exam": (
            "📝 آزمون تجارت بین‌الملل\n\n"
            "سوالات و آزمون‌های آموزشی تجارت بین‌الملل."
        ),
        "management": (
            "📚 آموزش مدیریت\n\n"
            "مفاهیم مدیریت، رفتار سازمانی و مهارت‌های مدیریتی."
        ),
        "marketing": (
            "📈 بازاریابی و فروش\n\n"
            "آموزش بازاریابی، فروش، مذاکره و جذب مشتری."
        ),
        "economy": (
            "💰 اقتصاد و بازار\n\n"
            "مفاهیم اقتصادی و آشنایی با بازارها."
        ),
        "banking": (
            "🏦 بانکداری\n\n"
            "مفاهیم بانکداری، قوانین بانکی و خدمات مالی."
        ),
        "exam": (
            "🎓 آزمون و تست\n\n"
            "سوالات و آزمون‌های آموزشی."
        ),
        "files": (
            "📂 فایل و جزوات\n\n"
            "فایل‌ها و جزوات آموزشی در این بخش قرار می‌گیرند."
        ),
        "social": (
            "📱 شبکه‌های اجتماعی\n\n"
            "شبکه‌های اجتماعی اندیشکده مدیریت و بازار."
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
    app.run(
        host="0.0.0.0",
        port=PORT
    )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است.")

    Thread(
        target=run_flask,
        daemon=True
    ).start()

    telegram_app = Application.builder().token(TOKEN).build()

    telegram_app.add_handler(
        CommandHandler("start", start)
    )

    telegram_app.add_handler(
        CommandHandler("help", help_command)
    )

    telegram_app.add_handler(
        CallbackQueryHandler(
            home_button,
            pattern="^home$"
        )
    )

    telegram_app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    telegram_app.run_polling()


if __name__ == "__main__":
    main()
