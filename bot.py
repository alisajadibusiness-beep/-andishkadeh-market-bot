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
    banking_text,
    banking_menu,
    banking_basics_text,
    banking_deposits_text,
    banking_facilities_text,
    banking_contracts_text,
    banking_checks_text,
    banking_credit_text,
    banking_electronic_text,
    banking_laws_text,
    banking_aml_text,
    banking_risk_text,
    banking_exam_text,
)
from employment import (
    employment_banks_text,
    employment_menu,
    employment_bank_text,
    employment_subjects_text,
    employment_interview_text,
    employment_iq_text,
    employment_english_text,
    employment_full_exam_text,
)
# =========================================================
# SETTINGS
# =========================================================
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))
app = Flask(__name__)
# =========================================================
# RENDER HEALTH CHECK
# =========================================================
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
                "🏆 آزمون‌های استخدامی",
                callback_data="employment"
            )
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
# SAFE MESSAGE SYSTEM
# =========================================================
TELEGRAM_SAFE_LIMIT = 3800
def split_text(text, limit=TELEGRAM_SAFE_LIMIT):
    parts = []
    while len(text) > limit:
        split_at = text.rfind("\n", 0, limit)
        if split_at <= 0:
            split_at = text.rfind(" ", 0, limit)
        if split_at <= 0:
            split_at = limit
        parts.append(text[:split_at].strip())
        text = text[split_at:].lstrip()
    if text.strip():
        parts.append(text.strip())
    return parts
async def send_safe_message(
    query,
    text,
    reply_markup=None
):
    parts = split_text(text)
    if not parts:
        return
    await query.edit_message_text(
        parts[0],
        reply_markup=(
            reply_markup
            if len(parts) == 1
            else None
        )
    )
    for i, part in enumerate(parts[1:]):
        is_last = i == len(parts[1:]) - 1
        await query.message.reply_text(
            part,
            reply_markup=(
                reply_markup
                if is_last
                else None
            )
        )
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
🏆 آزمون‌های استخدامی بانک‌ها
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
🎓 اندیشکده مدیریت و بازار
آموزش + آزمون + آمادگی شغلی
"""
    )
# =========================================================
# MANAGEMENT
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
# TRADE MENU
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
# MARKETING MENU
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
    await send_safe_message(
        query,
        f"""
{title}
{description}
""",
        InlineKeyboardMarkup(keyboard)
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
        await send_safe_message(
            query,
            management_definition_text(),
            management_definition_menu()
        )
        return
    if data == "management_functions":
        await send_safe_message(
            query,
            management_functions_text(),
            lesson_menu()
        )
        return
    if data == "management_levels":
        await send_safe_message(
            query,
            management_levels_text(),
            lesson_menu()
        )
        return
    if data == "management_roles":
        await send_safe_message(
            query,
            management_roles_text(),
            lesson_menu()
        )
        return
    if data == "management_skills":
        await send_safe_message(
            query,
            management_skills_text(),
            lesson_menu()
        )
        return
    if data == "efficiency_effectiveness":
        await send_safe_message(
            query,
            efficiency_effectiveness_text(),
            lesson_menu()
        )
        return
    if data == "management_schools":
        await send_safe_message(
            query,
            management_schools_text(),
            lesson_menu()
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
آموزش مفاهیم کاربردی تجارت خارجی، اسناد، حمل‌ونقل، پرداخت‌ها و اینکوترمز.
👇 موضوع موردنظر خود را انتخاب کنید:
""",
            reply_markup=trade_menu()
        )
        return
    if data == "trade_basics":
        await send_safe_message(
            query,
            trade_basics_text(),
            trade_lesson_menu()
        )
        return
    if data == "trade_documents":
        await send_safe_message(
            query,
            trade_documents_text(),
            trade_lesson_menu()
        )
        return
    if data == "trade_logistics":
        await send_safe_message(
            query,
            trade_logistics_text(),
            trade_lesson_menu()
        )
        return
    if data == "trade_payment":
        await send_safe_message(
            query,
            trade_payment_text(),
            trade_lesson_menu()
        )
        return
    if data == "trade_incoterms":
        await send_safe_message(
            query,
            trade_incoterms_text(),
            trade_lesson_menu()
        )
        return
    if data == "trade_laws":
        await send_safe_message(
            query,
            trade_laws_text(),
            trade_lesson_menu()
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
        await send_safe_message(
            query,
            marketing_basics_text(),
            marketing_lesson_menu()
        )
        return
    if data == "consumer_behavior":
        await send_safe_message(
            query,
            consumer_behavior_text(),
            marketing_lesson_menu()
        )
        return
    if data == "market_research":
        await send_safe_message(
            query,
            market_research_text(),
            marketing_lesson_menu()
        )
        return
    if data == "marketing_4p":
        await send_safe_message(
            query,
            marketing_4p_text(),
            marketing_lesson_menu()
        )
        return
    if data == "marketing_stp":
        await send_safe_message(
            query,
            marketing_stp_text(),
            marketing_lesson_menu()
        )
        return
    if data == "marketing_branding":
        await send_safe_message(
            query,
            marketing_branding_text(),
            marketing_lesson_menu()
        )
        return
    if data == "sales_negotiation":
        await send_safe_message(
            query,
            sales_negotiation_text(),
            marketing_lesson_menu()
        )
        return
    if data == "sales_funnel":
        await send_safe_message(
            query,
            sales_funnel_text(),
            marketing_lesson_menu()
        )
        return
    if data == "digital_marketing":
        await send_safe_message(
            query,
            digital_marketing_text(),
            marketing_lesson_menu()
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
        await send_safe_message(
            query,
            economy_basics_text(),
            economy_lesson_menu()
        )
        return
    if data == "supply_demand":
        await send_safe_message(
            query,
            supply_demand_text(),
            economy_lesson_menu()
        )
        return
    if data == "inflation":
        await send_safe_message(
            query,
            inflation_text(),
            economy_lesson_menu()
        )
        return
    if data == "exchange_rate":
        await send_safe_message(
            query,
            exchange_rate_text(),
            economy_lesson_menu()
        )
        return
    if data == "monetary_policy":
        await send_safe_message(
            query,
            monetary_policy_text(),
            economy_lesson_menu()
        )
        return
    if data == "fiscal_policy":
        await send_safe_message(
            query,
            fiscal_policy_text(),
            economy_lesson_menu()
        )
        return
    if data == "macroeconomics":
        await send_safe_message(
            query,
            macroeconomics_text(),
            economy_lesson_menu()
        )
        return
    if data == "microeconomics":
        await send_safe_message(
            query,
            microeconomics_text(),
            economy_lesson_menu()
        )
        return
    if data == "capital_market":
        await send_safe_message(
            query,
            capital_market_text(),
            economy_lesson_menu()
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
        await send_safe_message(
            query,
            banking_text(),
            banking_menu()
        )
        return
    if data == "banking_basics":
        await send_safe_message(
            query,
            banking_basics_text(),
            banking_menu()
        )
        return
    if data == "banking_deposits":
        await send_safe_message(
            query,
            banking_deposits_text(),
            banking_menu()
        )
        return
    if data == "banking_facilities":
        await send_safe_message(
            query,
            banking_facilities_text(),
            banking_menu()
        )
        return
    if data == "banking_contracts":
        await send_safe_message(
            query,
            banking_contracts_text(),
            banking_menu()
        )
        return
    if data == "banking_checks":
        await send_safe_message(
            query,
            banking_checks_text(),
            banking_menu()
        )
        return
    if data == "banking_credit":
        await send_safe_message(
            query,
            banking_credit_text(),
            banking_menu()
        )
        return
    if data == "banking_electronic":
        await send_safe_message(
            query,
            banking_electronic_text(),
            banking_menu()
        )
        return
    if data == "banking_laws":
        await send_safe_message(
            query,
            banking_laws_text(),
            banking_menu()
        )
        return
    if data == "banking_aml":
        await send_safe_message(
            query,
            banking_aml_text(),
            banking_menu()
        )
        return
    if data == "banking_risk":
        await send_safe_message(
            query,
            banking_risk_text(),
            banking_menu()
        )
        return
    if data == "banking_exam":
        await send_safe_message(
            query,
            banking_exam_text(),
            banking_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT
    # =====================================================
    if data == "employment":
        await send_safe_message(
            query,
            employment_banks_text(),
            employment_menu()
        )
        return
    if data == "employment_subjects":
        await send_safe_message(
            query,
            employment_subjects_text(),
            employment_menu()
        )
        return
    if data == "employment_interview":
        await send_safe_message(
            query,
            employment_interview_text(),
            employment_menu()
        )
        return
    if data == "employment_iq":
        await send_safe_message(
            query,
            employment_iq_text(),
            employment_menu()
        )
        return
    if data == "employment_english":
        await send_safe_message(
            query,
            employment_english_text(),
            employment_menu()
        )
        return
    if data == "employment_full_exam":
        await send_safe_message(
            query,
            employment_full_exam_text(),
            employment_menu()
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
        bank_name = employment_banks[data]
        await send_safe_message(
            query,
            employment_bank_text(bank_name),
            employment_menu()
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
آزمون‌های تخصصی اندیشکده در حال توسعه هستند.
به‌زودی آزمون‌های موضوعی و جامع در بخش‌های مختلف فعال می‌شوند.
"""
        )
        return
    if data == "files":
        await generic_message(
            query,
            "📂 فایل و جزوات",
            """
فایل‌ها و جزوات آموزشی در این بخش قرار خواهند گرفت.
📚 جزوات مدیریت
🌍 تجارت بین‌الملل
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
🏆 منابع آزمون استخدامی
"""
        )
        return
    if data == "social":
        await generic_message(
            query,
            "📱 شبکه‌های اجتماعی",
            """
📱 شبکه‌های اجتماعی اندیشکده مدیریت و بازار
برای دنبال کردن محتوای آموزشی جدید،
صفحات رسمی اندیشکده را دنبال کنید.
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
# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    main()
