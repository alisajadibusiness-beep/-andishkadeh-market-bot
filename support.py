import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


SUPPORT_CARD_NUMBER = os.getenv(
    "SUPPORT_CARD_NUMBER",
    "6219861875458621",
)

SUPPORT_CARD_DISPLAY = os.getenv(
    "SUPPORT_CARD_DISPLAY",
    "6219-8618-7545-8621",
)

SUPPORT_CARD_OWNER = os.getenv(
    "SUPPORT_CARD_OWNER",
    "علی سجادی",
)


def support_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📱 حمایت با کارت‌به‌کارت",
                callback_data="support_card",
            )
        ],
        [
            InlineKeyboardButton(
                "💳 پرداخت آنلاین 🔒 به‌زودی",
                callback_data="support_online",
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def support_text():
    return """
💎 حمایت از اندیشکده
━━━━━━━━━━━━━━━━━━

🌱 اندیشکده مدیریت و بازار با هدف
توسعه آموزش‌های تخصصی، آزمون‌های
حرفه‌ای و ابزارهای یادگیری فعالیت می‌کند.

❤️ اگر این مجموعه برای شما مفید بوده،
می‌توانید با حمایت مالی به ادامه توسعه
و تولید محتوای تخصصی کمک کنید.

━━━━━━━━━━━━━━━━━━

💚 حمایت شما صرف توسعه:

📚 محتوای آموزشی
📝 آزمون‌های تخصصی
🎯 آزمون‌های استخدامی
📊 تحلیل عملکرد
🚀 امکانات جدید ربات

می‌شود.

━━━━━━━━━━━━━━━━━━

🙏 از همراهی شما سپاسگزاریم.
"""


def support_card_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📋 دریافت شماره کارت",
                callback_data="support_card_copy",
            )
        ],
        [
            InlineKeyboardButton(
                "💎 حمایت از اندیشکده",
                callback_data="support",
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def support_card_text():
    return f"""
📱 حمایت با کارت‌به‌کارت
━━━━━━━━━━━━━━━━━━

💳 شماره کارت:

{SUPPORT_CARD_DISPLAY}

👤 به نام:

{SUPPORT_CARD_OWNER}

━━━━━━━━━━━━━━━━━━

💡 مبلغ حمایت کاملاً اختیاری است.

پس از واریز، در صورت تمایل می‌توانید
رسید پرداخت را برای پشتیبانی ارسال کنید.

❤️ از حمایت شما ممنونیم.
"""


async def support_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        support_text(),
        reply_markup=support_menu(),
    )


async def support_card_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        support_card_text(),
        reply_markup=support_card_menu(),
    )


async def support_card_copy_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer(
        "شماره کارت ارسال شد 📋",
        show_alert=True,
    )

    await query.message.reply_text(
        f"💳 شماره کارت برای کپی:\n\n"
        f"{SUPPORT_CARD_NUMBER}\n\n"
        f"👤 به نام: {SUPPORT_CARD_OWNER}"
    )


async def support_online_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(
                "📱 کارت‌به‌کارت",
                callback_data="support_card",
            )
        ],
        [
            InlineKeyboardButton(
                "💎 حمایت",
                callback_data="support",
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home",
            )
        ],
    ]

    await query.edit_message_text(
        """
💳 پرداخت آنلاین
━━━━━━━━━━━━━━━━━━

🔒 درگاه پرداخت آنلاین فعلاً فعال نیست.

🚀 این بخش در نسخه بعدی به یک
درگاه پرداخت معتبر متصل خواهد شد.

❤️ در حال حاضر می‌توانید از
روش کارت‌به‌کارت استفاده کنید.
""",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
