import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
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
from marketing import (
    marketing_menu,
    marketing_basics_text,
    consumer_behavior_text,
    market_research_text,
    marketing_4p_text,
    marketing_stp_text,
    marketing_branding_text,
    sales_negotiation_text,
    sales_funnel_text,
    digital_marketing_text,
    marketing_exam_question,
    MARKETING_QUESTIONS,
)
from economy import (
    economy_menu,
    economy_lesson_menu,
    economy_basics_text,
    supply_demand_text,
    inflation_text,
    exchange_rate_text,
    monetary_policy_text,
    fiscal_policy_text,
    macroeconomics_text,
    microeconomics_text,
    capital_market_text,
    economy_exam_question,
    ECONOMY_QUESTIONS,
)
from banking import (
    banking_menu,
    banking_lesson_menu,
    bank_basics_text,
    central_bank_text,
    bank_deposits_text,
    bank_facilities_text,
    bank_contracts_text,
    bank_documents_text,
    aml_text,
    cft_text,
    bank_accounting_text,
    international_banking_text,
    electronic_banking_text,
    bank_exam_tips_text,
    bank_exam_question,
    BANK_QUESTIONS,
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
📚 راهنمای ربات
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
# MARKETING LESSON MENU
# =========================================================
def marketing_lesson_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📝 آزمون بازاریابی و فروش",
                callback_data="marketing_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازاریابی و فروش",
                callback_data="marketing"
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
# BANKING LESSON
# =========================================================
async def show_banking_lesson(
    query,
    text
):
    await query.edit_message_text(
        text,
        reply_markup=banking_lesson_menu()
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
    if data == "management_definition":
        await query.edit_message_text(
            management_definition_text(),
            reply_markup=management_definition_menu()
        )
        return
    if data == "management_functions":
        await query.edit_message_text(
            management_functions_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "management_levels":
        await query.edit_message_text(
            management_levels_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "management_roles":
        await query.edit_message_text(
            management_roles_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "management_skills":
        await query.edit_message_text(
            management_skills_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "efficiency_effectiveness":
        await query.edit_message_text(
            efficiency_effectiveness_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "management_schools":
        await query.edit_message_text(
            management_schools_text(),
            reply_markup=lesson_menu()
        )
        return
    if data == "management_basics_exam":
        text, keyboard = exam_question(0, 0)
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
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
    # TRADE
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
    if data == "trade_basics":
        await query.edit_message_text(
            trade_basics_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_documents":
        await query.edit_message_text(
            trade_documents_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_logistics":
        await query.edit_message_text(
            trade_logistics_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_payment":
        await query.edit_message_text(
            trade_payment_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_incoterms":
        await query.edit_message_text(
            trade_incoterms_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_laws":
        await query.edit_message_text(
            trade_laws_text(),
            reply_markup=trade_lesson_menu()
        )
        return
    if data == "trade_exam":
        text, keyboard = trade_exam_question(0, 0)
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    if data.startswith("trade_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = TRADE_QUESTIONS[question_index]
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
    # MARKETING
    # =====================================================
    if data == "marketing":
        await query.edit_message_text(
            """
📈 بازاریابی و فروش
در این بخش با اصول بازاریابی، رفتار مصرف‌کننده، تحقیقات بازار، برندینگ، فروش و بازاریابی دیجیتال آشنا شوید.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
            reply_markup=marketing_menu()
        )
        return
    if data == "marketing_basics":
        await query.edit_message_text(
            marketing_basics_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "consumer_behavior":
        await query.edit_message_text(
            consumer_behavior_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "market_research":
        await query.edit_message_text(
            market_research_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "marketing_4p":
        await query.edit_message_text(
            marketing_4p_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "marketing_stp":
        await query.edit_message_text(
            marketing_stp_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "marketing_branding":
        await query.edit_message_text(
            marketing_branding_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "sales_negotiation":
        await query.edit_message_text(
            sales_negotiation_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "sales_funnel":
        await query.edit_message_text(
            sales_funnel_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "digital_marketing":
        await query.edit_message_text(
            digital_marketing_text(),
            reply_markup=marketing_lesson_menu()
        )
        return
    if data == "marketing_exam":
        text, keyboard = marketing_exam_question(0, 0)
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    if data.startswith("marketing_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = MARKETING_QUESTIONS[question_index]
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
        if next_question >= len(MARKETING_QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون بازاریابی و فروش به پایان رسید!
⭐ امتیاز شما:
{score} از {len(MARKETING_QUESTIONS)}
{result}
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔄 شروع مجدد",
                                callback_data="marketing_exam"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🔙 بازاریابی و فروش",
                                callback_data="marketing"
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
        text, keyboard = marketing_exam_question(
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
    # ECONOMY
    # =====================================================
    if data == "economy":
        await query.edit_message_text(
            """
💰 اقتصاد و بازار
در این بخش با مفاهیم پایه اقتصاد، عرضه و تقاضا، تورم، نرخ ارز، سیاست‌های اقتصادی و بازار سرمایه آشنا شوید.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
            reply_markup=economy_menu()
        )
        return
    if data == "economy_basics":
        await query.edit_message_text(
            economy_basics_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "supply_demand":
        await query.edit_message_text(
            supply_demand_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "inflation":
        await query.edit_message_text(
            inflation_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "exchange_rate":
        await query.edit_message_text(
            exchange_rate_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "monetary_policy":
        await query.edit_message_text(
            monetary_policy_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "fiscal_policy":
        await query.edit_message_text(
            fiscal_policy_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "macroeconomics":
        await query.edit_message_text(
            macroeconomics_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "microeconomics":
        await query.edit_message_text(
            microeconomics_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "capital_market":
        await query.edit_message_text(
            capital_market_text(),
            reply_markup=economy_lesson_menu()
        )
        return
    if data == "economy_exam":
        text, keyboard = economy_exam_question(0, 0)
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    if data.startswith("economy_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = ECONOMY_QUESTIONS[question_index]
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
        if next_question >= len(ECONOMY_QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون اقتصاد و بازار به پایان رسید!
⭐ امتیاز شما:
{score} از {len(ECONOMY_QUESTIONS)}
{result}
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔄 شروع مجدد",
                                callback_data="economy_exam"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🔙 اقتصاد و بازار",
                                callback_data="economy"
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
        text, keyboard = economy_exam_question(
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
    # BANKING
    # =====================================================
    if data == "banking":
        await query.edit_message_text(
            """
🏦 بانکداری تخصصی
دوره تخصصی بانکداری برای یادگیری مفاهیم بانکی و آمادگی آزمون‌های استخدامی بانک‌ها.
📚 از مبانی تا عملیات بانکی، عقود، تسهیلات، پولشویی و بانکداری بین‌الملل.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
            reply_markup=banking_menu()
        )
        return
    # -----------------------------------------------------
    # Banking lessons
    # -----------------------------------------------------
    if data == "bank_basics":
        await show_banking_lesson(
            query,
            bank_basics_text()
        )
        return
    if data == "central_bank":
        await show_banking_lesson(
            query,
            central_bank_text()
        )
        return
    if data == "bank_deposits":
        await show_banking_lesson(
            query,
            bank_deposits_text()
        )
        return
    if data == "bank_facilities":
        await show_banking_lesson(
            query,
            bank_facilities_text()
        )
        return
    if data == "bank_contracts":
        await show_banking_lesson(
            query,
            bank_contracts_text()
        )
        return
    if data == "bank_documents":
        await show_banking_lesson(
            query,
            bank_documents_text()
        )
        return
    if data == "aml":
        await show_banking_lesson(
            query,
            aml_text()
        )
        return
    if data == "cft":
        await show_banking_lesson(
            query,
            cft_text()
        )
        return
    if data == "bank_accounting":
        await show_banking_lesson(
            query,
            bank_accounting_text()
        )
        return
    if data == "international_banking":
        await show_banking_lesson(
            query,
            international_banking_text()
        )
        return
    if data == "electronic_banking":
        await show_banking_lesson(
            query,
            electronic_banking_text()
        )
        return
    if data == "bank_exam_tips":
        await show_banking_lesson(
            query,
            bank_exam_tips_text()
        )
        return
    # =====================================================
    # BANKING EXAM
    # =====================================================
    if data == "bank_exam":
        text, keyboard = bank_exam_question(0, 0)
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    if data.startswith("bank_answer_"):
        parts = data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
        question = BANK_QUESTIONS[question_index]
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
        if next_question >= len(BANK_QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون تخصصی بانکداری به پایان رسید!
⭐ امتیاز شما:
{score} از {len(BANK_QUESTIONS)}
{result}
📌 برای یادگیری بیشتر، بخش‌های آموزشی بانکداری را مطالعه کنید.
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "🔄 آزمون مجدد",
                                callback_data="bank_exam"
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
                                "🏠 منوی اصلی",
                                callback_data="home"
                            )
                        ],
                    ]
                )
            )
            return
        text, keyboard = bank_exam_question(
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
    # OTHER SECTIONS
    # =====================================================
    if data == "exam":
        await generic_message(
            query,
            "🎓 آزمون و تست",
            "آزمون‌های تخصصی هر بخش از منوی همان بخش قابل دسترسی هستند."
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
برای دنبال کردن محتوای جدید:
📸 اینستاگرام
▶️ یوتیوب
📱 تلگرام
اندیشکده مدیریت و بازار
"""
        )
        return
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
# MAIN
# =========================================================
def main():
    if not TOKEN:
        raise ValueError(
            "BOT_TOKEN تنظیم نشده است."
        )
    Thread(
        target=run_flask,
        daemon=True
    ).start()
    telegram_app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )
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
    telegram_app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )
    telegram_app.run_polling(
        drop_pending_updates=True
    )
if __name__ == "__main__":
    main()
