# exams.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from banking import (
    banking_menu,
    banking_intro_text,
)
# =========================================================
# منوی اصلی آزمون و تست
# =========================================================
def exams_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 مدیریت",
                callback_data="exam_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 تجارت",
                callback_data="exam_trade"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 بازاریابی",
                callback_data="exam_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 اقتصاد",
                callback_data="exam_economics"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 بانکداری",
                callback_data="exam_banking"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# متن معرفی آزمون و تست
# =========================================================
def exams_intro_text():
    return """
🎓 آزمون و تست
آزمون‌های تخصصی اندیشکده مدیریت و بازار برای سنجش دانش، مرور مطالب و آمادگی آزمون‌های دانشگاهی و استخدامی طراحی شده‌اند.
━━━━━━━━━━━━━━━━━━
📚 مدیریت
آزمون‌ها و تست‌های تخصصی مدیریت
🌍 تجارت
آزمون‌های تجارت و بازرگانی بین‌الملل
📈 بازاریابی
تست‌های تخصصی بازاریابی و فروش
💰 اقتصاد
آزمون‌های اقتصاد خرد، کلان و مباحث کاربردی
🏦 بانکداری
آموزش، تست تخصصی و آزمون جامع بانکداری
━━━━━━━━━━━━━━━━━━
🎯 مسیر پیشنهادی:
📖 مطالعه درسنامه
⬇️
📝 تست تخصصی
⬇️
🔄 مرور پاسخ‌های اشتباه
⬇️
🏆 آزمون جامع
⬇️
📊 ارزیابی نتیجه
━━━━━━━━━━━━━━━━━━
⭐ هدف اندیشکده:
یادگیری مفهومی
+
تمرین تستی
+
سنجش واقعی آمادگی
━━━━━━━━━━━━━━━━━━
📌 آزمون‌ها و مباحث جدید به‌صورت مرحله‌ای به این بخش اضافه می‌شوند.
"""
# =========================================================
# ورود به بخش آزمون
# =========================================================
async def exams_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        exams_intro_text(),
        reply_markup=exams_menu()
    )
# =========================================================
# ورود به بانکداری از بخش آزمون
# =========================================================
async def exam_banking_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        banking_intro_text(),
        reply_markup=banking_menu()
    )
# =========================================================
# بخش‌های آینده
# =========================================================
async def exam_management_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 آزمون و تست",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    await query.edit_message_text(
        """
📚 آزمون مدیریت
بخش آزمون‌های تخصصی مدیریت در حال توسعه است.
━━━━━━━━━━━━━━━━━━
📌 مباحث آینده:
• اصول مدیریت
• رفتار سازمانی
• مدیریت منابع انسانی
• مدیریت استراتژیک
• مدیریت بازرگانی
• تصمیم‌گیری
• تست‌های استخدامی مدیریت
━━━━━━━━━━━━━━━━━━
🔜 آزمون‌های تخصصی این بخش به‌مرور اضافه می‌شوند.
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# تجارت
# =========================================================
async def exam_trade_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 آزمون و تست",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    await query.edit_message_text(
        """
🌍 آزمون تجارت
بخش آزمون‌های تجارت و بازرگانی بین‌الملل در حال توسعه است.
━━━━━━━━━━━━━━━━━━
📌 مباحث آینده:
• تجارت بین‌الملل
• صادرات و واردات
• اینکوترمز
• اسناد تجاری
• حمل‌ونقل بین‌المللی
• روش‌های پرداخت بین‌المللی
• تعرفه و گمرک
• قراردادهای تجاری
━━━━━━━━━━━━━━━━━━
🔜 آزمون‌های تخصصی این بخش به‌مرور اضافه می‌شوند.
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# بازاریابی
# =========================================================
async def exam_marketing_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 آزمون و تست",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    await query.edit_message_text(
        """
📈 آزمون بازاریابی
بخش آزمون‌های تخصصی بازاریابی در حال توسعه است.
━━━━━━━━━━━━━━━━━━
📌 مباحث آینده:
• اصول بازاریابی
• رفتار مصرف‌کننده
• تحقیقات بازار
• بازاریابی دیجیتال
• فروش
• تبلیغات
• برندینگ
• استراتژی بازاریابی
━━━━━━━━━━━━━━━━━━
🔜 آزمون‌های تخصصی این بخش به‌مرور اضافه می‌شوند.
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# اقتصاد
# =========================================================
async def exam_economics_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 آزمون و تست",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]
    await query.edit_message_text(
        """
💰 آزمون اقتصاد
بخش آزمون‌های تخصصی اقتصاد در حال توسعه است.
━━━━━━━━━━━━━━━━━━
📌 مباحث آینده:
• اقتصاد خرد
• اقتصاد کلان
• عرضه و تقاضا
• کشش
• تولید و هزینه
• بازارها
• تورم
• بیکاری
• سیاست پولی
• سیاست مالی
• رشد اقتصادی
━━━━━━━━━━━━━━━━━━
🔜 آزمون‌های تخصصی این بخش به‌مرور اضافه می‌شوند.
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# ثبت Handlerهای آزمون
# =========================================================
def register_exam_handlers(application):
    # -----------------------------------------------------
    # منوی آزمون
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exams_callback,
            pattern=r"^exams$"
        )
    )
    # -----------------------------------------------------
    # بانکداری
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_banking_callback,
            pattern=r"^exam_banking$"
        )
    )
    # -----------------------------------------------------
    # مدیریت
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_management_callback,
            pattern=r"^exam_management$"
        )
    )
    # -----------------------------------------------------
    # تجارت
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_trade_callback,
            pattern=r"^exam_trade$"
        )
    )
    # -----------------------------------------------------
    # بازاریابی
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_marketing_callback,
            pattern=r"^exam_marketing$"
        )
    )
    # -----------------------------------------------------
    # اقتصاد
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_economics_callback,
            pattern=r"^exam_economics$"
        )
    )
