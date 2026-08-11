from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


# =========================================================
# 💎 SUPPORT / DONATION
# =========================================================

CARD_NUMBER = "6219861875458621"
CARD_DISPLAY = "6219-8618-7545-8621"
CARD_OWNER = "علی سجادی"


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
                callback_data="support_online_disabled",
            )
        ],
        [
            InlineKeyboardButton(
                "📞 ارتباط با ما",
                callback_data="social",
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

🌱 اندیشکده مدیریت و بازار با هدف توسعه
آموزش‌های تخصصی، آزمون‌های حرفه‌ای،
آزمون‌های استخدامی و ابزارهای یادگیری
در حوزه‌های مختلف فعالیت می‌کند.

❤️ اگر این ربات برای شما مفید بوده،
می‌توانید با حمایت مالی به توسعه و
بهبود امکانات آن کمک کنید.

━━━━━━━━━━━━━━━━━━
💚 روش فعلی حمایت

📱 کارت‌به‌کارت

💳 مبلغ حمایت کاملاً اختیاری است.

🙏 هر مبلغی، حتی کوچک، برای ادامه
و توسعه این پروژه ارزشمند است.

━━━━━━━━━━━━━━━━━━
"""


def support_card_text():
    return f"""
📱 حمایت از طریق کارت‌به‌کارت
━━━━━━━━━━━━━━━━━━

💳 شماره کارت:

{CARD_DISPLAY}

👤 به نام:

{CARD_OWNER}

━━━━━━━━━━━━━━━━━━

💡 مبلغ حمایت کاملاً اختیاری است.

پس از واریز، در صورت نیاز می‌توانید
رسید پرداخت را برای پشتیبانی ارسال کنید.

❤️ از همراهی و حمایت شما سپاسگزاریم.
"""


def support_card_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📋 کپی شماره کارت",
                callback_data="support_copy_card",
            )
        ],
        [
            InlineKeyboardButton(
                "💎 حمایت مالی",
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


async def support_copy_card_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer(
        "شماره کارت برای کپی آماده است 📋",
        show_alert=True,
    )

    await query.message.reply_text(
        f"💳 شماره کارت:\n\n{CARD_NUMBER}\n\n"
        f"👤 به نام: {CARD_OWNER}"
    )


async def support_online_disabled_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        """
💳 پرداخت آنلاین
━━━━━━━━━━━━━━━━━━

🔒 درگاه پرداخت آنلاین هنوز فعال نشده است.

🚀 این بخش در نسخه بعدی با اتصال
درگاه پرداخت معتبر فعال خواهد شد.

❤️ فعلاً می‌توانید از طریق
کارت‌به‌کارت از پروژه حمایت کنید.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📱 کارت‌به‌کارت",
                        callback_data="support_card",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💎 حمایت مالی",
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
        ),
    )
