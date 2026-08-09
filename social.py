# social.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# =========================================================
#              لینک شبکه‌های اجتماعی
# =========================================================
INSTAGRAM_URL = "https://www.instagram.com/andishkadeh_market"
WHATSAPP_URL = "https://whatsapp.com/channel/0029Vb77lS7IHphL867sDr1t"
TELEGRAM_URL = "https://t.me/andishkadehmarket_bot"
# =========================================================
#              متن شبکه‌های اجتماعی
# =========================================================
def social_text():
    return """
📱 شبکه‌های اجتماعی
🏛️ اندیشکده مدیریت و بازار
برای دسترسی به جدیدترین آموزش‌ها،
مقالات، نکات کاربردی و آزمون‌های تخصصی،
ما را در شبکه‌های اجتماعی دنبال کنید.
━━━━━━━━━━━━━━━━━━
📚 مدیریت
آموزش مفاهیم و مهارت‌های مدیریت
🌍 تجارت
تجارت و بازرگانی بین‌الملل
📈 بازاریابی
بازاریابی، فروش و برندینگ
💰 اقتصاد
مفاهیم اقتصادی به زبان ساده
🏦 بانکداری
آموزش تخصصی بانکداری و آمادگی آزمون‌های استخدامی
📝 آزمون و تست
تمرین، سنجش و ارزیابی دانش
━━━━━━━━━━━━━━━━━━
🔥 جدیدترین محتواها
📌 آموزش‌های کوتاه
📊 نکات کاربردی و تخصصی
📝 تست‌های آموزشی
🎯 نکات آزمون‌های استخدامی
🚀 مهارت‌های حرفه‌ای
━━━━━━━━━━━━━━━━━━
👇 برای ورود به هر شبکه، دکمه مربوطه را انتخاب کنید.
"""
# =========================================================
#              منوی شبکه‌های اجتماعی
# =========================================================
def social_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📸 اینستاگرام",
                url=INSTAGRAM_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📢 تلگرام",
                url=TELEGRAM_URL
            )
        ],
        [
            InlineKeyboardButton(
                "💬 کانال واتساپ",
                url=WHATSAPP_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
#              ورود به شبکه‌های اجتماعی
# =========================================================
async def social_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        social_text(),
        reply_markup=social_menu()
    )
