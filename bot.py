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
# TRADE
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
# MARKETING
# =========================================================
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
# =========================================================
# ECONOMY
# =========================================================
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
# =========================================================
# BANKING
# =========================================================
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
    banking_full_exam_text,
    BANKING_QUESTIONS,
)
# =========================================================
# EMPLOYMENT
# =========================================================
try:
    from employment import (
        employment_menu,
        employment_banks_text,
        employment_bank_text,
        employment_subjects_text,
        employment_interview_text,
        employment_iq_text,
        employment_english_text,
        employment_full_exam_text,
        employment_bank_menu,
    )
    EMPLOYMENT_AVAILABLE = True
except ImportError:
    EMPLOYMENT_AVAILABLE = False
# =========================================================
# SERVER
# =========================================================
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))
app = Flask(__name__)
@app.route("/")
def home():
    return "Andishkadeh Market Bot is running."
def run_flask():
    app.run(
        host="0.0.0.0",
        port=PORT,
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
                "🏦 بانکداری تخصصی",
                callback_data="banking"
            ),
            InlineKeyboardButton(
                "🎓 آزمون و تست",
                callback_data="exam"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏆 آزمون‌های استخدامی",
                callback_data="employment"
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
🏦 بانکداری تخصصی
🏆 آزمون‌های استخدامی
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
برای شروع از منوی اصلی یک موضوع را انتخاب کنید.
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
# BANKING LESSON MENU
# =========================================================
def banking_lesson_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔙 بانکداری تخصصی",
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
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# BANKING QUIZ RESULT
# =========================================================
def banking_quiz_result_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 شروع مجدد",
                callback_data="banking_quiz"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بانکداری تخصصی",
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
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# EMPLOYMENT SAFE MENU
# =========================================================
def employment_fallback_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
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
آموزش مفاهیم کاربردی تجارت خارجی، اسناد، حمل‌ونقل، پرداخت‌ها، قراردادها و اینکوترمز.
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
            banking_intro_text(),
            reply_markup=banking_menu()
        )
        return
    if data == "banking_basics":
        await query.edit_message_text(
            banking_basics_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_deposits":
        await query.edit_message_text(
            banking_deposits_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_facilities":
        await query.edit_message_text(
            banking_facilities_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_contracts":
        await query.edit_message_text(
            banking_contracts_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_laws":
        await query.edit_message_text(
            banking_laws_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_checks":
        await query.edit_message_text(
            banking_checks_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_aml":
        await query.edit_message_text(
            banking_aml_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_credit":
        await query.edit_message_text(
            banking_credit_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_electronic":
        await query.edit_message_text(
            banking_electronic_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_risk":
        await query.edit_message_text(
            banking_risk_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_central":
        await query.edit_message_text(
            banking_central_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    if data == "banking_islamic":
        await query.edit_message_text(
            banking_islamic_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    # =====================================================
    # BANKING QUIZ
    # =====================================================
    if data == "banking_quiz":
        text, keyboard = banking_quiz_question(
            0,
            0
        )
        await query.edit_message_text(
            text,
            reply_markup=keyboard
        )
        return
    if data.startswith("banking_answer_"):
        parts = data.split("_")
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
                f"پاسخ صحیح: {correct_answer}"
            )
        next_question = question_index + 1
        if next_question >= len(BANKING_QUESTIONS):
            await query.edit_message_text(
                f"""
🏆 آزمون تخصصی بانکداری به پایان رسید!
⭐ امتیاز شما:
{score} از {len(BANKING_QUESTIONS)}
{result}
""",
                reply_markup=banking_quiz_result_menu()
            )
            return
        text, keyboard = banking_quiz_question(
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
    # BANKING FULL EXAM
    # =====================================================
    if data == "banking_full_exam":
        await query.edit_message_text(
            banking_full_exam_text(),
            reply_markup=banking_lesson_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT
    # =====================================================
    if data == "employment":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🏆 آزمون‌های استخدامی بانک‌ها",
                "فایل employment.py هنوز در پروژه قرار نگرفته است."
            )
            return
        await query.edit_message_text(
            employment_banks_text(),
            reply_markup=employment_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT SUBJECTS
    # =====================================================
    if data == "employment_subjects":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "📚 دروس و منابع",
                "بخش منابع استخدامی هنوز فعال نشده است."
            )
            return
        await query.edit_message_text(
            employment_subjects_text(),
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT INTERVIEW
    # =====================================================
    if data == "employment_interview":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🎤 مصاحبه استخدامی",
                "بخش مصاحبه هنوز فعال نشده است."
            )
            return
        await query.edit_message_text(
            employment_interview_text(),
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT IQ
    # =====================================================
    if data == "employment_iq":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🧠 آزمون هوش",
                "بخش آزمون هوش هنوز فعال نشده است."
            )
            return
        await query.edit_message_text(
            employment_iq_text(),
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT ENGLISH
    # =====================================================
    if data == "employment_english":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🇬🇧 زبان انگلیسی",
                "بخش زبان هنوز فعال نشده است."
            )
            return
        await query.edit_message_text(
            employment_english_text(),
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT FULL EXAM
    # =====================================================
    if data == "employment_full_exam":
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🏆 آزمون جامع استخدامی",
                "بخش آزمون جامع هنوز فعال نشده است."
            )
            return
        await query.edit_message_text(
            employment_full_exam_text(),
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT BANKS
    # =====================================================
    employment_banks = {
        "employment_melli": "بانک ملی ایران",
        "employment_mellat": "بانک ملت",
        "employment_tejarat": "بانک تجارت",
        "employment_saderat": "بانک صادرات ایران",
        "employment_refah": "بانک رفاه کارگران",
        "employment_shahr": "بانک شهر",
        "employment_maskan": "بانک مسکن",
        "employment_keshavarzi": "بانک کشاورزی",
        "employment_sepah": "بانک سپه",
        "employment_mehr": "بانک قرض‌الحسنه مهر ایران",
    }
    if data in employment_banks:
        if not EMPLOYMENT_AVAILABLE:
            await generic_message(
                query,
                "🏦 آزمون استخدامی بانک",
                "بخش استخدامی هنوز فعال نشده است."
            )
            return
        bank_name = employment_banks[data]
        await query.edit_message_text(
            employment_bank_text(bank_name),
            reply_markup=employment_bank_menu(bank_name)
        )
        return
    # =====================================================
    # EMPLOYMENT BANK SUBMENU
    # =====================================================
    if data.startswith("bank_lesson_"):
        bank_name = data.replace(
            "bank_lesson_",
            ""
        )
        await query.edit_message_text(
            f"""
📖 درسنامه استخدامی
🏦 {bank_name}
درسنامه‌های تخصصی این بانک به‌صورت موضوعی ارائه خواهند شد.
📚 محورهای اصلی:
🏦 بانکداری
⚖️ قوانین بانکی
💰 اقتصاد
📊 مدیریت
🧾 حسابداری
📈 مدیریت مالی
🧠 هوش
🇬🇧 زبان
💻 ICDL
""",
            reply_markup=employment_fallback_menu()
        )
        return
    if data.startswith("bank_questions_"):
        bank_name = data.replace(
            "bank_questions_",
            ""
        )
        await query.edit_message_text(
            f"""
📝 نمونه سؤالات استخدامی
🏦 {bank_name}
بانک سؤال این بخش در حال توسعه است.
هدف:
🎯 سؤال‌های پرتکرار
🧠 تست‌های مفهومی
⏱️ تست‌های زمان‌دار
📊 تحلیل پاسخ‌ها
""",
            reply_markup=employment_fallback_menu()
        )
        return
    if data.startswith("bank_exam_"):
        bank_name = data.replace(
            "bank_exam_",
            ""
        )
        await query.edit_message_text(
            f"""
⏱️ آزمون استخدامی
🏦 {bank_name}
آزمون شبیه‌ساز این بانک در حال آماده‌سازی است.
این بخش در نسخه بعدی شامل:
📝 سؤال‌های تخصصی
🧠 هوش
🇬🇧 زبان
💻 ICDL
⏱️ زمان‌بندی
📊 تحلیل نتیجه
خواهد بود.
""",
            reply_markup=employment_fallback_menu()
        )
        return
    if data.startswith("bank_tips_"):
        bank_name = data.replace(
            "bank_tips_",
            ""
        )
        await query.edit_message_text(
            f"""
🎯 نکات مهم استخدامی
🏦 {bank_name}
برای موفقیت در آزمون استخدامی:
1️⃣ دفترچه رسمی آزمون را دقیق مطالعه کنید.
2️⃣ منابع اعلام‌شده را اولویت‌بندی کنید.
3️⃣ تست‌های سال‌های قبل را بررسی کنید.
4️⃣ زمان پاسخ‌گویی را مدیریت کنید.
5️⃣ اشتباهات خود را تحلیل کنید.
6️⃣ قبل از آزمون اصلی چند آزمون شبیه‌ساز انجام دهید.
⚠️ مواد امتحانی و شرایط استخدامی ممکن است در هر دوره تغییر کند.
""",
            reply_markup=employment_fallback_menu()
        )
        return
    # =====================================================
    # OTHER SECTIONS
    # =====================================================
    if data == "exam":
        await generic_message(
            query,
            "🎓 آزمون و تست",
            """
آزمون‌های آموزشی اندیشکده در این بخش قرار می‌گیرند.
📚 مدیریت
🌍 تجارت
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
آزمون‌های تخصصی به‌مرور توسعه داده می‌شوند.
"""
        )
        return
    if data == "files":
        await generic_message(
            query,
            "📂 فایل و جزوات",
            """
فایل‌ها و جزوات آموزشی در این بخش قرار خواهند گرفت.
📚 جزوات
📝 نمونه سؤالات
📑 خلاصه دروس
📊 منابع آزمون
"""
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
    # UNKNOWN CALLBACK
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
