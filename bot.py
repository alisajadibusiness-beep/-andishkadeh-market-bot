from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

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
    banking_full_exam_question,
    banking_result_menu,

    BANKING_QUESTIONS,
    BANKING_FULL_EXAM_QUESTIONS,
)


# =========================================================
#                 متن و منوی اصلی
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
    ]

    return InlineKeyboardMarkup(keyboard)


def main_menu_text():

    return """
🏛️ اندیشکده مدیریت و بازار

مرکز آموزش مدیریت، تجارت، بازاریابی، اقتصاد و بانکداری

━━━━━━━━━━━━━━━━━━

🎓 آموزش و آزمون
📚 مدیریت
🌍 تجارت
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری

━━━━━━━━━━━━━━━━━━

👇 بخش موردنظر را انتخاب کنید:
"""


# =========================================================
#                 /start
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
#                 منوی اصلی
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
#                 منوی آزمون و تست
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


def exams_intro_text():

    return """
🎓 آزمون و تست

مرکز تخصصی آزمون‌های اندیشکده مدیریت و بازار

در این بخش می‌توانید با استفاده از آزمون‌های موضوعی و جامع، میزان یادگیری و آمادگی خود را ارزیابی کنید.

━━━━━━━━━━━━━━━━━━

📚 مدیریت

آزمون‌های تخصصی مدیریت و مباحث مرتبط با مدیریت بازرگانی

🌍 تجارت

آزمون‌های تجارت و بازرگانی بین‌الملل

📈 بازاریابی

آزمون‌های تخصصی بازاریابی، فروش و برندینگ

💰 اقتصاد

آزمون‌های اقتصاد خرد، کلان و مباحث کاربردی اقتصادی

🏦 بانکداری

آموزش، تست تخصصی و آزمون جامع بانکداری

━━━━━━━━━━━━━━━━━━

🎯 مسیر پیشنهادی:

📖 مطالعه درسنامه
⬇️
📝 حل تست تخصصی
⬇️
🔄 مرور پاسخ‌های اشتباه
⬇️
🏆 آزمون جامع
⬇️
📊 ارزیابی نتیجه

━━━━━━━━━━━━━━━━━━

⭐ هدف:

یادگیری مفهومی
+
تمرین تستی
+
افزایش سرعت و دقت
+
سنجش آمادگی

━━━━━━━━━━━━━━━━━━

📌 آزمون‌های جدید به‌صورت مرحله‌ای اضافه خواهند شد.
"""


async def exams_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    await query.edit_message_text(
        exams_intro_text(),
        reply_markup=exams_menu()
    )


# =========================================================
#                 ورود به بانکداری از آزمون
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
#                 بخش‌های آینده آزمون
# =========================================================

async def future_exam_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    data = query.data

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
        data,
        "🎓 آزمون"
    )

    await query.edit_message_text(
        f"""
{title}

━━━━━━━━━━━━━━━━━━

این بخش در حال توسعه است.

📌 بانک سؤال تخصصی این بخش به‌صورت مرحله‌ای اضافه خواهد شد.

━━━━━━━━━━━━━━━━━━

🔜 مباحث آینده:

• درسنامه تخصصی
• تست موضوعی
• آزمون جامع
• محاسبه درصد
• تعیین سطح
• تحلیل پاسخ‌های اشتباه
""",
        reply_markup=InlineKeyboardMarkup([
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
        ])
    )


# =========================================================
#                 منوی بانکداری
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
#                 درسنامه‌های بانکداری
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

    text = lesson_function()

    await query.edit_message_text(
        text,
        reply_markup=banking_back_menu()
    )


# =========================================================
#                 تست تخصصی بانکداری
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

    # بررسی پاسخ

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

    # پایان آزمون

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

        text = f"""
🏆 آزمون تخصصی بانکداری به پایان رسید!

━━━━━━━━━━━━━━━━━━

⭐ امتیاز شما:

{score} از {total}

📊 درصد:

{percentage}٪

🎯 سطح:

{level}

━━━━━━━━━━━━━━━━━━

{result}

━━━━━━━━━━━━━━━━━━

📚 پیشنهاد:

مباحثی را که در آن‌ها اشتباه داشتی دوباره مرور کن.
"""

        await query.edit_message_text(
            text,
            reply_markup=banking_result_menu()
        )

        return

    # سؤال بعدی

    text, keyboard = banking_quiz_question(
        index=next_question,
        score=score
    )

    await query.edit_message_text(
        f"""
{result}

{text}
""",
        reply_markup=keyboard
    )


# =========================================================
#                 آزمون جامع بانکداری
# =========================================================

async def banking_full_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    text, keyboard = banking_full_exam_question(
        index=0,
        score=0
    )

    await query.edit_message_text(
        text,
        reply_markup=keyboard
    )


async def banking_full_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    parts = query.data.split("_")

    question_index = int(parts[3])
    selected_answer = int(parts[4])
    score = int(parts[5])

    question = BANKING_FULL_EXAM_QUESTIONS[
        question_index
    ]

    # بررسی پاسخ

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

    # پایان آزمون

    if next_question >= len(
        BANKING_FULL_EXAM_QUESTIONS
    ):

        total = len(
            BANKING_FULL_EXAM_QUESTIONS
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

        text = f"""
🏆 آزمون جامع بانکداری به پایان رسید!

━━━━━━━━━━━━━━━━━━

⭐ امتیاز شما:

{score} از {total}

📊 درصد:

{percentage}٪

🎯 سطح:

{level}

━━━━━━━━━━━━━━━━━━

{result}

━━━━━━━━━━━━━━━━━━

📚 پیشنهاد:

سوالاتی را که اشتباه پاسخ دادی دوباره مرور کن و مباحث مربوط به آن‌ها را مرور کن.
"""

        await query.edit_message_text(
            text,
            reply_markup=banking_result_menu()
        )

        return

    # سؤال بعدی

    text, keyboard = banking_full_exam_question(
        index=next_question,
        score=score
    )

    await query.edit_message_text(
        f"""
{result}

{text}
""",
        reply_markup=keyboard
    )


# =========================================================
#                 ثبت Handlerها
# =========================================================

def register_handlers(application):

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
    # بانکداری از منوی آزمون
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            exam_banking_callback,
            pattern=r"^exam_banking$"
        )
    )

    # -----------------------------------------------------
    # مدیریت / تجارت / بازاریابی / اقتصاد
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
    # ورود مستقیم به بانکداری
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            banking_callback,
            pattern=r"^banking$"
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
    # تست تخصصی بانکداری
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_start,
            pattern=r"^banking_quiz$"
        )
    )

    # -----------------------------------------------------
    # پاسخ تست تخصصی
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            banking_answer_callback,
            pattern=r"^banking_answer_\d+_\d+_\d+$"
        )
    )

    # -----------------------------------------------------
    # آزمون جامع بانکداری
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            banking_full_exam_start,
            pattern=r"^banking_full_exam$"
        )
    )

    # -----------------------------------------------------
    # پاسخ آزمون جامع
    # -----------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            banking_full_answer_callback,
            pattern=r"^banking_full_answer_\d+_\d+_\d+$"
        )
    )


# =========================================================
#                 اجرای ربات
# =========================================================

def main():

    TOKEN = "YOUR_BOT_TOKEN"

    application = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    # /start

    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # ثبت Handlerها

    register_handlers(
        application
    )

    print(
        "🏛️ Andishkadeh Market Bot is running..."
    )

    application.run_polling()


# =========================================================
#                 اجرا
# =========================================================

if __name__ == "__main__":
    main()
