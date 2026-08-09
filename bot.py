import os
from flask import Flask
from threading import Thread
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
# =========================================================
# MANAGEMENT
# =========================================================
from management import (
    management_basics_menu,
    management_definition_text,
    management_definition_menu,
    management_functions_text,
    management_levels_text,
    management_roles_text,
    management_skills_text,
    efficiency_effectiveness_text,
    management_schools_text,
    lesson_menu,
    exam_question,
    QUESTIONS,
)
# =========================================================
# INTERNATIONAL TRADE
# =========================================================
from trade import (
    trade_menu,
    trade_basics_text,
    trade_documents_text,
    trade_logistics_text,
    trade_payment_text,
    trade_incoterms_text,
    trade_laws_text,
    trade_exam_question,
    TRADE_QUESTIONS,
)
# =========================================================
# SETTINGS
# =========================================================
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))
# =========================================================
# FLASK
# =========================================================
app = Flask(__name__)
@app.route("/")
def home():
    return "Andishkadeh Market Bot is running."
def run_flask():
    app.run(
        host="0.0.0.0",
        port=PORT
    )
# =========================================================
# MAIN MENU
# =========================================================
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 آموزش مدیریت",
                callback_data="management"
            ),
            InlineKeyboardButton(
                "🌍 تجارت بین‌الملل",
                callback_data="trade"
            ),
        ],
        [
            InlineKeyboardButton(
                "📈 بازاریابی و فروش",
                callback_data="marketing"
            ),
            InlineKeyboardButton(
                "💰 اقتصاد و بازار",
                callback_data="economy"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانکداری",
                callback_data="banking"
            ),
            InlineKeyboardButton(
                "🎓 آزمون و تست",
                callback_data="exam"
            ),
        ],
        [
            InlineKeyboardButton(
                "📂 فایل و جزوات",
                callback_data="files"
            ),
            InlineKeyboardButton(
                "📱 شبکه‌های اجتماعی",
                callback_data="social"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# START
# =========================================================
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
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
# =========================================================
# HELP
# =========================================================
async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        """
📚 راهنمای اندیشکده مدیریت و بازار
/start
نمایش منوی اصلی
/help
نمایش راهنما
"""
    )
# =========================================================
# MANAGEMENT MENU
# =========================================================
async def show_management(query):
    keyboard = [
        [
            InlineKeyboardButton(
                "🧠 مبانی مدیریت",
                callback_data="management_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 رفتار سازمانی",
                callback_data="organizational_behavior"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 مدیریت استراتژیک",
                callback_data="strategic_management"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 منابع انسانی",
                callback_data="human_resources"
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
📚 آموزش مدیریت
دانش و مهارت‌های کاربردی مدیریت را از مباحث پایه تا پیشرفته یاد بگیرید.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# GENERIC MESSAGE
# =========================================================
async def generic_message(
    query,
    title,
    description
):
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ]
    ]
    await query.edit_message_text(
        f"""
{title}
{description}
""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# BUTTON HANDLER
# =========================================================
async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    data = query.data
    # =====================================================
    # HOME
    # =====================================================
    if data == "home":
        await query.edit_message_text(
            """
🎓 اندیشکده مدیریت و بازار
👇 از منوی زیر یک بخش را انتخاب کنید:
""",
            reply_markup=main_menu()
        )
        return
    # =====================================================
    # MANAGEMENT
    # =====================================================
    if data == "management":
        await show_management(query)
        return
    # =====================================================
    # MANAGEMENT BASICS
    # =====================================================
    if data == "management_basics":
        await query.edit_message_text(
            """
🧠 مبانی مدیریت
مهم‌ترین مفاهیم پایه مدیریت را در این بخش یاد بگیرید.
👇 یک موضوع را انتخاب کنید:
""",
            reply_markup=management_basics_menu()
        )
        return
    # =====================================================
    # MANAGEMENT DEFINITION
    # =====================================================
    if data == "management_definition":
        await query.edit_message_text(
            management_definition_text(),
            reply_markup=management_definition_menu()
        )
        return
    # =====================================================
    # MANAGEMENT FUNCTIONS
    # =====================================================
    if data == "management_functions":
        await query.edit_message_text(
            management_functions_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # MANAGEMENT LEVELS
    # =====================================================
    if data == "management_levels":
        await query.edit_message_text(
            management_levels_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # MANAGEMENT ROLES
    # =====================================================
    if data == "management_roles":
        await query.edit_message_text(
            management_roles_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # MANAGEMENT SKILLS
    # =====================================================
    if data == "management_skills":
        await query.edit_message_text(
            management_skills_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # EFFICIENCY / EFFECTIVENESS
    # =====================================================
    if data == "efficiency_effectiveness":
        await query.edit_message_text(
            efficiency_effectiveness_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # MANAGEMENT SCHOOLS
    # =====================================================
    if data == "management_schools":
        await query.edit_message_text(
            management_schools_text(),
            reply_markup=lesson_menu()
        )
        return
    # =====================================================
    # MANAGEMENT EXAM
    # =====================================================
    if data == "management_basics_exam":
        text, keyboard = exam_question(
            0,
            0
        )
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    # =====================================================
    # MANAGEMENT DEFINITION EXAM
    # =====================================================
    if data == "management_definition_exam":
        text, keyboard = exam_question(
            0,
            0
        )
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    # =====================================================
    # MANAGEMENT EXAM ANSWERS
    # =====================================================
    if data.startswith("mg_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = QUESTIONS[question_index]
        if selected_answer == question["correct"]:
            score += 1
            result = "✅ پاسخ صحیح است!"
        else:
            correct_answer = question["options"][
                question["correct"]
            ]
            result = (
                "❌ پاسخ اشتباه است.\n\n"
                f"پاسخ صحیح: {correct_answer}"
            )
        next_question = question_index + 1
        if next_question >= len(QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون مبانی مدیریت به پایان رسید!
⭐ امتیاز شما:
{score} از {len(QUESTIONS)}
{result}
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔄 شروع مجدد",
                                callback_data="management_basics_exam"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🔙 مبانی مدیریت",
                                callback_data="management_basics"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🏠 منوی اصلی",
                                callback_data="home"
                            )
                        ],
                    ]
                )
            )
            return
        text, keyboard = exam_question(
            next_question,
            score
        )
        await query.edit_message_text(
            f"""
{result}
{text}
""",
            reply_markup=keyboard
        )
        return
    # =====================================================
    # INTERNATIONAL TRADE
    # =====================================================
    if data == "trade":
        await query.edit_message_text(
            """
🌍 تجارت بین‌الملل
آموزش مفاهیم کاربردی تجارت خارجی، اسناد، قراردادها، حمل‌ونقل، پرداخت‌ها و اینکوترمز.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
            reply_markup=trade_menu()
        )
        return
    # =====================================================
    # TRADE BASICS
    # =====================================================
    if data == "trade_basics":
        await query.edit_message_text(
            trade_basics_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE DOCUMENTS
    # =====================================================
    if data == "trade_documents":
        await query.edit_message_text(
            trade_documents_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE LOGISTICS
    # =====================================================
    if data == "trade_logistics":
        await query.edit_message_text(
            trade_logistics_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE PAYMENT
    # =====================================================
    if data == "trade_payment":
        await query.edit_message_text(
            trade_payment_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE INCOTERMS
    # =====================================================
    if data == "trade_incoterms":
        await query.edit_message_text(
            trade_incoterms_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE LAWS
    # =====================================================
    if data == "trade_laws":
        await query.edit_message_text(
            trade_laws_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    # =====================================================
    # TRADE EXAM
    # =====================================================
    if data == "trade_exam":
        text, keyboard = trade_exam_question(
            0,
            0
        )
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    # =====================================================
    # TRADE EXAM ANSWERS
    # =====================================================
    if data.startswith("trade_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = TRADE_QUESTIONS[
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
                f"پاسخ صحیح: {correct_answer}"
            )
        next_question = question_index + 1
        if next_question >= len(TRADE_QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون تجارت بین‌الملل به پایان رسید!
⭐ امتیاز شما:
{score} از {len(TRADE_QUESTIONS)}
{result}
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔄 شروع مجدد",
                                callback_data="trade_exam"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🔙 تجارت بین‌الملل",
                                callback_data="trade"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🏠 منوی اصلی",
                                callback_data="home"
                            )
                        ],
                    ]
                )
            )
            return
        text, keyboard = trade_exam_question(
            next_question,
            score
        )
        await query.edit_message_text(
            f"""
{result}
{text}
""",
            reply_markup=keyboard
        )
        return
    # =====================================================
    # OTHER MAIN SECTIONS
    # =====================================================
    if data == "marketing":
        await generic_message(
            query,
            "📈 بازاریابی و فروش",
            "محتوای آموزشی بازاریابی و فروش به‌زودی در این بخش قرار می‌گیرد."
        )
        return
    if data == "economy":
        await generic_message(
            query,
            "💰 اقتصاد و بازار",
            "محتوای آموزشی اقتصاد و بازار به‌زودی در این بخش قرار می‌گیرد."
        )
        return
    if data == "banking":
        await generic_message(
            query,
            "🏦 بانکداری",
            "محتوای آموزشی بانکداری به‌زودی در این بخش قرار می‌گیرد."
        )
        return
    if data == "exam":
        await generic_message(
            query,
            "🎓 آزمون و تست",
            "بخش آزمون‌های تخصصی به‌زودی فعال می‌شود."
        )
        return
    if data == "files":
        await generic_message(
            query,
            "📂 فایل و جزوات",
            "فایل‌ها و جزوات آموزشی در این بخش قرار خواهند گرفت."
        )
        return
    if data == "social":
        await generic_message(
            query,
            "📱 شبکه‌های اجتماعی",
            """
📱 شبکه‌های اجتماعی اندیشکده مدیریت و بازار
برای دنبال کردن محتوای جدید، صفحات رسمی اندیشکده را دنبال کنید.
"""
        )
        return
    # =====================================================
    # FUTURE MANAGEMENT
    # =====================================================
    if data == "organizational_behavior":
        await generic_message(
            query,
            "📊 رفتار سازمانی",
            "محتوای رفتار سازمانی به‌زودی اضافه می‌شود."
        )
        return
    if data == "strategic_management":
        await generic_message(
            query,
            "🎯 مدیریت استراتژیک",
            "محتوای مدیریت استراتژیک به‌زودی اضافه می‌شود."
        )
        return
    if data == "human_resources":
        await generic_message(
            query,
            "👥 مدیریت منابع انسانی",
            "محتوای مدیریت منابع انسانی به‌زودی اضافه می‌شود."
        )
        return
    # =====================================================
    # UNKNOWN
    # =====================================================
    await query.edit_message_text(
        """
❌ گزینه موردنظر پیدا نشد.
لطفاً از منوی اصلی دوباره وارد شوید.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ]
            ]
        )
    )
# =========================================================
# TRADE LESSON MENU
# =========================================================
def trade_lesson_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📝 آزمون تجارت بین‌الملل",
                callback_data="trade_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 تجارت بین‌الملل",
                callback_data="trade"
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
# MAIN
# =========================================================
def main():
    if not TOKEN:
        raise ValueError(
            "BOT_TOKEN تنظیم نشده است."
        )
    # Flask server
    Thread(
        target=run_flask,
        daemon=True
    ).start()
    # Telegram application
    telegram_app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )
    # Commands
    telegram_app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )
    telegram_app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )
    # Callback handler
    telegram_app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )
    # Start polling
    telegram_app.run_polling(
        drop_pending_updates=True
    )
# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    main()
