# bot.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)
# =========================================================
#              Import بخش‌های آموزشی
# =========================================================
from banking import (
    banking_menu,
    banking_back_menu,
    banking_intro_text,
    banking_basics_text,
    banking_deposits_text,
    banking_facilities_text,
    banking_contracts_text,
    banking_laws_text,
    banking_checks_text,
    banking_aml_text,
    banking_credit_text,
    banking_electronic_text,
    banking_risk_text,
    banking_central_text,
    banking_islamic_text,
    banking_quiz_question,
    BANKING_QUESTIONS,
)
# =========================================================
#              شبکه‌های اجتماعی
# =========================================================
from social import (
    social_callback,
)
# =========================================================
#              تنظیمات ربات
# =========================================================

# =========================================================
#              منوی اصلی
# =========================================================
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🎓 آزمون و تست",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 بانکداری تخصصی",
                callback_data="banking"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 شبکه‌های اجتماعی",
                callback_data="social"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
#              متن منوی اصلی
# =========================================================
def main_menu_text():
    return """
🏛️ اندیشکده مدیریت و بازار
مرکز آموزش تخصصی مدیریت، تجارت، بازاریابی، اقتصاد و بانکداری
━━━━━━━━━━━━━━━━━━
📚 آموزش تخصصی
📝 آزمون و تست
🎯 آمادگی آزمون‌های استخدامی
📊 یادگیری مفهومی و کاربردی
━━━━━━━━━━━━━━━━━━
📖 حوزه‌های آموزشی:
📚 مدیریت
🌍 تجارت و بازرگانی
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
━━━━━━━━━━━━━━━━━━
👇 بخش موردنظر خود را انتخاب کنید:
"""
# =========================================================
#              دستور /start
# =========================================================
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        main_menu_text(),
        reply_markup=main_menu()
    )
# =========================================================
#              بازگشت به منوی اصلی
# =========================================================
async def home_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        main_menu_text(),
        reply_markup=main_menu()
    )
# =========================================================
#              منوی آزمون و تست
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
#              متن آزمون و تست
# =========================================================
def exams_text():
    return """
🎓 آزمون و تست
مرکز تخصصی آزمون‌های اندیشکده مدیریت و بازار
در این بخش می‌توانید با استفاده از آزمون‌های موضوعی و جامع، میزان یادگیری و آمادگی خود را ارزیابی کنید.
━━━━━━━━━━━━━━━━━━
📚 مدیریت
آزمون‌های تخصصی مدیریت و مدیریت بازرگانی
🌍 تجارت
آزمون‌های تجارت و بازرگانی بین‌الملل
📈 بازاریابی
آزمون‌های بازاریابی، فروش و برندینگ
💰 اقتصاد
آزمون‌های اقتصاد خرد، کلان و مفاهیم کاربردی
🏦 بانکداری
آموزش و آزمون تخصصی بانکداری
━━━━━━━━━━━━━━━━━━
🎯 مسیر پیشنهادی:
📖 مطالعه درسنامه
⬇️
📝 حل تست تخصصی
⬇️
🔄 مرور اشتباهات
⬇️
🏆 آزمون جامع
⬇️
📊 بررسی نتیجه
━━━━━━━━━━━━━━━━━━
⭐ هدف:
یادگیری مفهومی
+
تمرین تستی
+
افزایش سرعت و دقت
+
آمادگی آزمونی
"""
async def exams_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        exams_text(),
        reply_markup=exams_menu()
    )
# =========================================================
#              ورود به بانکداری
# =========================================================
async def exam_banking_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        banking_intro_text(),
        reply_markup=banking_menu()
    )
# =========================================================
#              بخش‌های در حال توسعه
# =========================================================
async def future_exam_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    titles = {
        "exam_management":
            "📚 آزمون مدیریت",
        "exam_trade":
            "🌍 آزمون تجارت",
        "exam_marketing":
            "📈 آزمون بازاریابی",
        "exam_economics":
            "💰 آزمون اقتصاد",
    }
    title = titles.get(
        query.data,
        "🎓 آزمون"
    )
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
        f"""
{title}
━━━━━━━━━━━━━━━━━━
🚧 این بخش در حال توسعه است.
به‌زودی موارد زیر اضافه می‌شوند:
📖 درسنامه تخصصی
📝 تست موضوعی
🏆 آزمون جامع
📊 محاسبه درصد
🎯 تعیین سطح
🔄 تکرار آزمون
📚 تحلیل پاسخ‌های اشتباه
━━━━━━━━━━━━━━━━━━
🏛️ اندیشکده مدیریت و بازار
""",
        reply_markup=InlineKeyboardMarkup(
            keyboard
        )
    )
# =========================================================
#              منوی بانکداری
# =========================================================
async def banking_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        banking_intro_text(),
        reply_markup=banking_menu()
    )
# =========================================================
#              درسنامه‌های بانکداری
# =========================================================
BANKING_LESSONS = {
    "banking_basics":
        banking_basics_text,
    "banking_deposits":
        banking_deposits_text,
    "banking_facilities":
        banking_facilities_text,
    "banking_contracts":
        banking_contracts_text,
    "banking_laws":
        banking_laws_text,
    "banking_checks":
        banking_checks_text,
    "banking_aml":
        banking_aml_text,
    "banking_credit":
        banking_credit_text,
    "banking_electronic":
        banking_electronic_text,
    "banking_risk":
        banking_risk_text,
    "banking_central":
        banking_central_text,
    "banking_islamic":
        banking_islamic_text,
}
async def banking_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data not in BANKING_LESSONS:
        return
    lesson_function = BANKING_LESSONS[data]
    await query.edit_message_text(
        lesson_function(),
        reply_markup=banking_back_menu()
    )
# =========================================================
#              تست تخصصی بانکداری
# =========================================================
async def banking_quiz_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    text, keyboard = banking_quiz_question(
        index=0,
        score=0
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard
    )
# =========================================================
#              پاسخ تست بانکداری
# =========================================================
async def banking_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    question_index = int(parts[2])
    selected_answer = int(parts[3])
    score = int(parts[4])
    question = BANKING_QUESTIONS[
        question_index
    ]
    if selected_answer == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است!"
    else:
        correct_answer = question["options"][
            question["correct"]
        ]
        result = (
            "❌ پاسخ اشتباه است.\n\n"
            f"✅ پاسخ صحیح: {correct_answer}"
        )
    next_question = question_index + 1
    # -----------------------------------------------------
    # پایان آزمون
    # -----------------------------------------------------
    if next_question >= len(
        BANKING_QUESTIONS
    ):
        total = len(
            BANKING_QUESTIONS
        )
        percentage = int(
            score / total * 100
        )
        if percentage >= 90:
            level = "🔥 فوق‌العاده"
        elif percentage >= 70:
            level = "⭐ عالی"
        elif percentage >= 50:
            level = "👍 متوسط"
        else:
            level = "📚 نیازمند مرور"
        keyboard = [
            [
                InlineKeyboardButton(
                    "🔄 تکرار آزمون",
                    callback_data="banking_quiz"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏦 بانکداری",
                    callback_data="banking"
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
            f"""
🏆 آزمون تخصصی بانکداری به پایان رسید!
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
{score} از {total}
📊 درصد:
{percentage}٪
🎯 سطح:
{level}
━━━━━━━━━━━━━━━━━━
{result}
━━━━━━━━━━━━━━━━━━
📚 پیشنهاد:
پاسخ‌های اشتباه خود را مرور کنید و
مبحث مربوطه را دوباره مطالعه کنید.
""",
            reply_markup=InlineKeyboardMarkup(
                keyboard
            )
        )
        return
    # -----------------------------------------------------
    # سؤال بعدی
    # -----------------------------------------------------
    text, keyboard = banking_quiz_question(
        index=next_question,
        score=score
    )
    await query.edit_message_text(
        f"""
{result}
━━━━━━━━━━━━━━━━━━
{text}
""",
        reply_markup=keyboard
    )
# =========================================================
#              ثبت Handlerها
# =========================================================
def register_handlers(
    application
):
    # -----------------------------------------------------
    # منوی اصلی
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern=r"^home$"
        )
    )
    # -----------------------------------------------------
    # آزمون و تست
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exams_callback,
            pattern=r"^exams$"
        )
    )
    # -----------------------------------------------------
    # ورود به بانکداری
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_banking_callback,
            pattern=r"^exam_banking$"
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_callback,
            pattern=r"^banking$"
        )
    )
    # -----------------------------------------------------
    # آزمون‌های آینده
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            future_exam_callback,
            pattern=(
                r"^exam_"
                r"(management|trade|marketing|economics)$"
            )
        )
    )
    # -----------------------------------------------------
    # درسنامه‌های بانکداری
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_lesson_callback,
            pattern=(
                r"^banking_"
                r"(basics|deposits|facilities|contracts|"
                r"laws|checks|aml|credit|electronic|"
                r"risk|central|islamic)$"
            )
        )
    )
    # -----------------------------------------------------
    # تست تخصصی
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_start,
            pattern=r"^banking_quiz$"
        )
    )
    # -----------------------------------------------------
    # پاسخ تست
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_answer_callback,
            pattern=r"^banking_answer_\d+_\d+_\d+$"
        )
    )
    # -----------------------------------------------------
    # شبکه‌های اجتماعی
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            social_callback,
            pattern=r"^social$"
        )
    )
# =========================================================
#              اجرای ربات
# =========================================================
def main():
    application = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )
    # -----------------------------------------------------
    # دستور /start
    # -----------------------------------------------------
    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )
    # -----------------------------------------------------
    # ثبت Handlerها
    # -----------------------------------------------------
    register_handlers(
        application
    )
    print(
        "🏛️ Andishkadeh Market Bot is running..."
    )
    application.run_polling()
# =========================================================
#              شروع برنامه
# =========================================================
if __name__ == "__main__":
    main()
