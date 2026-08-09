from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)
from banking import (
    banking_menu,
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
# /start
# =========================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 بانکداری تخصصی",
                callback_data="banking"
            )
        ]
    ]
    await update.message.reply_text(
        """
🏛️ اندیشکده مدیریت و بازار
به بخش آموزش و آمادگی آزمون‌های بانکی خوش آمدید.
👇 از منوی زیر وارد بخش بانکداری شوید:
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# منوی بانکداری
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
# درسنامه‌های بانکداری
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
# =========================================================
# نمایش درسنامه
# =========================================================
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
# منوی برگشت بانکداری
# =========================================================
async def banking_back_callback(
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
# شروع تست تخصصی
# =========================================================
async def banking_quiz_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    context.user_data["banking_quiz_score"] = 0
    text, keyboard = banking_quiz_question(
        index=0,
        score=0
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard
    )
# =========================================================
# پاسخ تست تخصصی
# =========================================================
async def banking_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    # banking_answer_INDEX_SELECTED_SCORE
    question_index = int(parts[2])
    selected_answer = int(parts[3])
    score = int(parts[4])
    question = BANKING_QUESTIONS[question_index]
    # -----------------------------------------------------
    # بررسی پاسخ
    # -----------------------------------------------------
    if selected_answer == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است!"
    else:
        correct_answer = question["options"][
            question["correct"]
        ]
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: {correct_answer}"
        )
    # -----------------------------------------------------
    # سؤال بعدی
    # -----------------------------------------------------
    next_question = question_index + 1
    # -----------------------------------------------------
    # پایان آزمون
    # -----------------------------------------------------
    if next_question >= len(BANKING_QUESTIONS):
        total = len(BANKING_QUESTIONS)
        percentage = int(
            (score / total) * 100
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
مباحثی که در آن‌ها اشتباه داشتی را دوباره مرور کن.
"""
        await query.edit_message_text(
            text,
            reply_markup=banking_result_menu()
        )
        return
    # -----------------------------------------------------
    # نمایش سؤال بعدی
    # -----------------------------------------------------
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
# شروع آزمون جامع
# =========================================================
async def banking_full_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    context.user_data["banking_full_score"] = 0
    text, keyboard = banking_full_exam_question(
        index=0,
        score=0
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard
    )
# =========================================================
# پاسخ آزمون جامع
# =========================================================
async def banking_full_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    # banking_full_answer_INDEX_SELECTED_SCORE
    question_index = int(parts[3])
    selected_answer = int(parts[4])
    score = int(parts[5])
    question = BANKING_FULL_EXAM_QUESTIONS[
        question_index
    ]
    # -----------------------------------------------------
    # بررسی پاسخ
    # -----------------------------------------------------
    if selected_answer == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است!"
    else:
        correct_answer = question["options"][
            question["correct"]
        ]
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: {correct_answer}"
        )
    # -----------------------------------------------------
    # سؤال بعدی
    # -----------------------------------------------------
    next_question = question_index + 1
    # -----------------------------------------------------
    # پایان آزمون جامع
    # -----------------------------------------------------
    if next_question >= len(
        BANKING_FULL_EXAM_QUESTIONS
    ):
        total = len(
            BANKING_FULL_EXAM_QUESTIONS
        )
        percentage = int(
            (score / total) * 100
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
سوالاتی را که اشتباه پاسخ دادی دوباره مرور کن و سپس آزمون را تکرار کن.
"""
        await query.edit_message_text(
            text,
            reply_markup=banking_result_menu()
        )
        return
    # -----------------------------------------------------
    # سؤال بعدی
    # -----------------------------------------------------
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
# منوی اصلی
# =========================================================
async def home_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 بانکداری تخصصی",
                callback_data="banking"
            )
        ]
    ]
    await query.edit_message_text(
        """
🏛️ اندیشکده مدیریت و بازار
منوی اصلی
👇 بخش موردنظر را انتخاب کنید:
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# ثبت Handlerها
# =========================================================
def register_banking_handlers(application):
    # -----------------------------------------------------
    # ورود به بانکداری
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_callback,
            pattern=r"^banking$"
        )
    )
    # -----------------------------------------------------
    # درسنامه‌ها
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_lesson_callback,
            pattern=(
                r"^banking_"
                r"(basics|deposits|facilities|contracts|laws|"
                r"checks|aml|credit|electronic|risk|central|islamic)$"
            )
        )
    )
    # -----------------------------------------------------
    # برگشت به بانکداری
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_back_callback,
            pattern=r"^banking$"
        )
    )
    # -----------------------------------------------------
    # شروع تست تخصصی
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
    # شروع آزمون جامع
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
    # -----------------------------------------------------
    # منوی اصلی
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern=r"^home$"
        )
    )
# =========================================================
# اجرای ربات
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
    # ثبت Handlerهای بانکداری
    register_banking_handlers(
        application
    )
    print(
        "🏛️ Andishkadeh Market Bot is running..."
    )
    application.run_polling()
# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    main()
