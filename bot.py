# bot.py
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# =========================================================
# IMPORT BANKING
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
# IMPORT MANAGEMENT
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
    QUESTIONS as MANAGEMENT_QUESTIONS,
    exam_question as management_exam_question,
    exam_start_menu,
)

# =========================================================
# IMPORT TRADE
# =========================================================
from trade import (
    trade_menu,
    trade_basics_text,
    trade_documents_text,
    trade_logistics_text,
    trade_payment_text,
    trade_incoterms_text,
    trade_laws_text,
    TRADE_QUESTIONS,
    trade_exam_question,
)

# =========================================================
# IMPORT MARKETING
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
    MARKETING_QUESTIONS,
    marketing_exam_question,
)

# =========================================================
# IMPORT ECONOMY
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
    ECONOMY_QUESTIONS,
    economy_exam_question,
)

# =========================================================
# IMPORT EMPLOYMENT
# =========================================================
from employment import (
    employment_banks_text,
    employment_menu,
    employment_bank_text,
    employment_bank_menu,
    employment_subjects_text,
    employment_interview_text,
    employment_iq_text,
    employment_english_text,
    employment_full_exam_text,
    employment_back_menu,
)

# =========================================================
# IMPORT SOCIAL
# =========================================================
from social import social_callback

# =========================================================
# TOKEN
# =========================================================
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set.")


# =========================================================
# MAIN MENU
# =========================================================
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📚 آموزش مدیریت", callback_data="management"),
            InlineKeyboardButton("🌍 تجارت بین‌الملل", callback_data="trade"),
        ],
        [
            InlineKeyboardButton("📈 بازاریابی و فروش", callback_data="marketing"),
            InlineKeyboardButton("💰 اقتصاد و بازار", callback_data="economy"),
        ],
        [
            InlineKeyboardButton("🏦 بانکداری", callback_data="banking"),
            InlineKeyboardButton("🎓 آزمون و تست", callback_data="exams"),
        ],
        [
            InlineKeyboardButton("📚 آزمون‌های استخدامی", callback_data="employment"),
            InlineKeyboardButton("📱 شبکه‌های اجتماعی", callback_data="social"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


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
# START / HOME
# =========================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            main_menu_text(),
            reply_markup=main_menu(),
        )


async def home_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        main_menu_text(),
        reply_markup=main_menu(),
    )


# =========================================================
# SIMPLE SECTION CALLBACK
# =========================================================
async def section_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    sections = {
        "management": (
            "📚 آموزش مدیریت\n━━━━━━━━━━━━━━━━━━\n"
            "مبانی و مفاهیم مدیریت، مهارت‌ها، نقش‌های مدیر و آزمون تخصصی.",
            management_basics_menu(),
        ),
        "trade": (
            "🌍 تجارت بین‌الملل\n━━━━━━━━━━━━━━━━━━\n"
            "مفاهیم پایه، اسناد، حمل‌ونقل، پرداخت، اینکوترمز و آزمون.",
            trade_menu(),
        ),
        "marketing": (
            "📈 بازاریابی و فروش\n━━━━━━━━━━━━━━━━━━\n"
            "اصول بازاریابی، رفتار مصرف‌کننده، STP، برندینگ، فروش و بازاریابی دیجیتال.",
            marketing_menu(),
        ),
        "economy": (
            "💰 اقتصاد و بازار\n━━━━━━━━━━━━━━━━━━\n"
            "مبانی اقتصاد، عرضه و تقاضا، تورم، ارز، سیاست پولی و مالی و بازار سرمایه.",
            economy_menu(),
        ),
    }

    if query.data not in sections:
        return

    text, keyboard = sections[query.data]
    await query.edit_message_text(text, reply_markup=keyboard)


# =========================================================
# EXAMS MENU
# =========================================================
def exams_menu():
    keyboard = [
        [InlineKeyboardButton("📚 مدیریت", callback_data="exam_management")],
        [InlineKeyboardButton("🌍 تجارت", callback_data="exam_trade")],
        [InlineKeyboardButton("📈 بازاریابی", callback_data="exam_marketing")],
        [InlineKeyboardButton("💰 اقتصاد", callback_data="exam_economics")],
        [InlineKeyboardButton("🏦 بانکداری", callback_data="exam_banking")],
        [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
    ]
    return InlineKeyboardMarkup(keyboard)


def exams_text():
    return """
🎓 آزمون و تست
مرکز تخصصی آزمون‌های اندیشکده مدیریت و بازار
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
"""


async def exams_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(exams_text(), reply_markup=exams_menu())


# =========================================================
# BANKING
# =========================================================
async def banking_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        banking_intro_text(),
        reply_markup=banking_menu(),
    )


BANKING_LESSONS = {
    "banking_basics": banking_basics_text,
    "banking_deposits": banking_deposits_text,
    "banking_facilities": banking_facilities_text,
    "banking_contracts": banking_contracts_text,
    "banking_laws": banking_laws_text,
    "banking_checks": banking_checks_text,
    "banking_aml": banking_aml_text,
    "banking_credit": banking_credit_text,
    "banking_electronic": banking_electronic_text,
    "banking_risk": banking_risk_text,
    "banking_central": banking_central_text,
    "banking_islamic": banking_islamic_text,
}


async def banking_lesson_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lesson_function = BANKING_LESSONS.get(query.data)
    if not lesson_function:
        return
    await query.edit_message_text(
        lesson_function(),
        reply_markup=banking_back_menu(),
    )


async def banking_quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text, keyboard = banking_quiz_question(index=0, score=0)
    await query.edit_message_text(text, reply_markup=keyboard)


async def banking_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        parts = query.data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
    except (ValueError, IndexError):
        await query.edit_message_text(
            "❌ خطایی در پردازش پاسخ رخ داد.",
            reply_markup=banking_back_menu(),
        )
        return

    if question_index >= len(BANKING_QUESTIONS):
        await query.edit_message_text(
            "❌ سؤال موردنظر پیدا نشد.",
            reply_markup=banking_back_menu(),
        )
        return

    question = BANKING_QUESTIONS[question_index]

    if selected_answer == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        correct_answer = question["options"][question["correct"]]
        result = f"❌ پاسخ اشتباه است.\n\n✅ پاسخ صحیح: {correct_answer}"

    next_question = question_index + 1

    if next_question >= len(BANKING_QUESTIONS):
        total = len(BANKING_QUESTIONS)
        percentage = int((score / total) * 100)

        if percentage >= 90:
            level = "🔥 فوق‌العاده"
        elif percentage >= 70:
            level = "⭐ عالی"
        elif percentage >= 50:
            level = "👍 متوسط"
        else:
            level = "📚 نیازمند مرور"

        keyboard = [
            [InlineKeyboardButton("🔄 تکرار آزمون", callback_data="banking_quiz")],
            [InlineKeyboardButton("🏦 بانکداری", callback_data="banking")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
        ]

        await query.edit_message_text(
            f"""
🏆 آزمون تخصصی بانکداری به پایان رسید!
━━━━━━━━━━━━━━━━━━
⭐ امتیاز: {score} از {total}
📊 درصد: {percentage}٪
🎯 سطح: {level}
━━━━━━━━━━━━━━━━━━
{result}
━━━━━━━━━━━━━━━━━━
📚 پیشنهاد:
پاسخ‌های اشتباه خود را مرور کنید.
""",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    text, keyboard = banking_quiz_question(
        index=next_question,
        score=score,
    )
    await query.edit_message_text(
        f"{result}\n━━━━━━━━━━━━━━━━━━\n{text}",
        reply_markup=keyboard,
    )


# =========================================================
# MANAGEMENT
# =========================================================
MANAGEMENT_LESSONS = {
    "management_definition": management_definition_text,
    "management_functions": management_functions_text,
    "management_levels": management_levels_text,
    "management_roles": management_roles_text,
    "management_skills": management_skills_text,
    "efficiency_effectiveness": efficiency_effectiveness_text,
    "management_schools": management_schools_text,
}


async def management_basics_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "📚 مبانی مدیریت\n━━━━━━━━━━━━━━━━━━\nدرسنامه‌ها و آزمون مبانی مدیریت:",
        reply_markup=management_basics_menu(),
    )


async def management_lesson_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    func = MANAGEMENT_LESSONS.get(query.data)
    if not func:
        return

    keyboard = (
        management_definition_menu()
        if query.data == "management_definition"
        else lesson_menu()
    )

    await query.edit_message_text(func(), reply_markup=keyboard)


async def management_exam_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text, keyboard = management_exam_question(index=0, score=0)
    await query.edit_message_text(text, reply_markup=keyboard)


async def management_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        _, _, index, selected, score = query.data.split("_")
        index = int(index)
        selected = int(selected)
        score = int(score)
    except (ValueError, IndexError):
        await query.edit_message_text("❌ خطا در پردازش پاسخ.", reply_markup=management_basics_menu())
        return

    question = MANAGEMENT_QUESTIONS[index]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: {question['options'][question['correct']]}"
        )

    next_index = index + 1

    if next_index >= len(MANAGEMENT_QUESTIONS):
        total = len(MANAGEMENT_QUESTIONS)
        percentage = int(score / total * 100)
        keyboard = [
            [InlineKeyboardButton("🔄 تکرار آزمون", callback_data="management_definition_exam")],
            [InlineKeyboardButton("📚 مبانی مدیریت", callback_data="management_basics")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
        ]
        await query.edit_message_text(
            f"""
🏆 آزمون مبانی مدیریت به پایان رسید!
━━━━━━━━━━━━━━━━━━
⭐ امتیاز: {score} از {total}
📊 درصد: {percentage}٪
━━━━━━━━━━━━━━━━━━
{result}
""",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    text, keyboard = management_exam_question(index=next_index, score=score)
    await query.edit_message_text(
        f"{result}\n━━━━━━━━━━━━━━━━━━\n{text}",
        reply_markup=keyboard,
    )


# =========================================================
# TRADE
# =========================================================
TRADE_LESSONS = {
    "trade_basics": trade_basics_text,
    "trade_documents": trade_documents_text,
    "trade_logistics": trade_logistics_text,
    "trade_payment": trade_payment_text,
    "trade_incoterms": trade_incoterms_text,
    "trade_laws": trade_laws_text,
}


async def trade_lesson_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    func = TRADE_LESSONS.get(query.data)
    if not func:
        return

    await query.edit_message_text(func(), reply_markup=trade_menu())


async def trade_exam_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text, keyboard = trade_exam_question(index=0, score=0)
    await query.edit_message_text(text, reply_markup=keyboard)


async def trade_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        _, _, _, index, selected, score = query.data.split("_")
        index = int(index)
        selected = int(selected)
        score = int(score)
    except (ValueError, IndexError):
        await query.edit_message_text("❌ خطا در پردازش پاسخ.", reply_markup=trade_menu())
        return

    question = TRADE_QUESTIONS[index]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = f"❌ پاسخ اشتباه است.\n✅ پاسخ صحیح: {question['options'][question['correct']]}"

    next_index = index + 1
    if next_index >= len(TRADE_QUESTIONS):
        total = len(TRADE_QUESTIONS)
        percentage = int(score / total * 100)
        keyboard = [
            [InlineKeyboardButton("🔄 تکرار آزمون", callback_data="trade_exam")],
            [InlineKeyboardButton("🌍 تجارت بین‌الملل", callback_data="trade")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
        ]
        await query.edit_message_text(
            f"🏆 آزمون تجارت بین‌الملل به پایان رسید!\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"⭐ امتیاز: {score} از {total}\n"
            f"📊 درصد: {percentage}٪\n"
            f"━━━━━━━━━━━━━━━━━━\n{result}",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    text, keyboard = trade_exam_question(index=next_index, score=score)
    await query.edit_message_text(
        f"{result}\n━━━━━━━━━━━━━━━━━━\n{text}",
        reply_markup=keyboard,
    )


# =========================================================
# MARKETING
# =========================================================
MARKETING_LESSONS = {
    "marketing_basics": marketing_basics_text,
    "consumer_behavior": consumer_behavior_text,
    "market_research": market_research_text,
    "marketing_4p": marketing_4p_text,
    "marketing_stp": marketing_stp_text,
    "marketing_branding": marketing_branding_text,
    "sales_negotiation": sales_negotiation_text,
    "sales_funnel": sales_funnel_text,
    "digital_marketing": digital_marketing_text,
}


async def marketing_lesson_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    func = MARKETING_LESSONS.get(query.data)
    if not func:
        return

    await query.edit_message_text(func(), reply_markup=marketing_menu())


async def marketing_exam_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text, keyboard = marketing_exam_question(index=0, score=0)
    await query.edit_message_text(text, reply_markup=keyboard)


async def marketing_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        _, _, _, index, selected, score = query.data.split("_")
        index = int(index)
        selected = int(selected)
        score = int(score)
    except (ValueError, IndexError):
        await query.edit_message_text("❌ خطا در پردازش پاسخ.", reply_markup=marketing_menu())
        return

    question = MARKETING_QUESTIONS[index]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = f"❌ پاسخ اشتباه است.\n✅ پاسخ صحیح: {question['options'][question['correct']]}"

    next_index = index + 1
    if next_index >= len(MARKETING_QUESTIONS):
        total = len(MARKETING_QUESTIONS)
        percentage = int(score / total * 100)
        keyboard = [
            [InlineKeyboardButton("🔄 تکرار آزمون", callback_data="marketing_exam")],
            [InlineKeyboardButton("📈 بازاریابی و فروش", callback_data="marketing")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
        ]
        await query.edit_message_text(
            f"🏆 آزمون بازاریابی و فروش به پایان رسید!\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"⭐ امتیاز: {score} از {total}\n"
            f"📊 درصد: {percentage}٪\n"
            f"━━━━━━━━━━━━━━━━━━\n{result}",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    text, keyboard = marketing_exam_question(index=next_index, score=score)
    await query.edit_message_text(
        f"{result}\n━━━━━━━━━━━━━━━━━━\n{text}",
        reply_markup=keyboard,
    )


# =========================================================
# ECONOMY
# =========================================================
ECONOMY_LESSONS = {
    "economy_basics": economy_basics_text,
    "supply_demand": supply_demand_text,
    "inflation": inflation_text,
    "exchange_rate": exchange_rate_text,
    "monetary_policy": monetary_policy_text,
    "fiscal_policy": fiscal_policy_text,
    "macroeconomics": macroeconomics_text,
    "microeconomics": microeconomics_text,
    "capital_market": capital_market_text,
}


async def economy_lesson_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    func = ECONOMY_LESSONS.get(query.data)
    if not func:
        return

    await query.edit_message_text(func(), reply_markup=economy_lesson_menu())


async def economy_exam_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text, keyboard = economy_exam_question(index=0, score=0)
    await query.edit_message_text(text, reply_markup=keyboard)


async def economy_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        _, _, _, index, selected, score = query.data.split("_")
        index = int(index)
        selected = int(selected)
        score = int(score)
    except (ValueError, IndexError):
        await query.edit_message_text("❌ خطا در پردازش پاسخ.", reply_markup=economy_menu())
        return

    question = ECONOMY_QUESTIONS[index]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = f"❌ پاسخ اشتباه است.\n✅ پاسخ صحیح: {question['options'][question['correct']]}"

    next_index = index + 1
    if next_index >= len(ECONOMY_QUESTIONS):
        total = len(ECONOMY_QUESTIONS)
        percentage = int(score / total * 100)
        keyboard = [
            [InlineKeyboardButton("🔄 تکرار آزمون", callback_data="economy_exam")],
            [InlineKeyboardButton("💰 اقتصاد و بازار", callback_data="economy")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
        ]
        await query.edit_message_text(
            f"🏆 آزمون اقتصاد و بازار به پایان رسید!\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"⭐ امتیاز: {score} از {total}\n"
            f"📊 درصد: {percentage}٪\n"
            f"━━━━━━━━━━━━━━━━━━\n{result}",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    text, keyboard = economy_exam_question(index=next_index, score=score)
    await query.edit_message_text(
        f"{result}\n━━━━━━━━━━━━━━━━━━\n{text}",
        reply_markup=keyboard,
    )


# =========================================================
# EMPLOYMENT
# =========================================================
BANK_NAMES = {
    "employment_melli": "بانک ملی",
    "employment_mellat": "بانک ملت",
    "employment_tejarat": "بانک تجارت",
    "employment_saderat": "بانک صادرات",
    "employment_refah": "بانک رفاه",
    "employment_shahr": "بانک شهر",
    "employment_maskan": "بانک مسکن",
    "employment_keshavarzi": "بانک کشاورزی",
    "employment_sepah": "بانک سپه",
    "employment_mehr": "بانک مهر ایران",
}


async def employment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        employment_banks_text(),
        reply_markup=employment_menu(),
    )


async def employment_bank_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bank_name = BANK_NAMES.get(query.data)
    if not bank_name:
        return

    await query.edit_message_text(
        employment_bank_text(bank_name),
        reply_markup=employment_bank_menu(bank_name),
    )


async def employment_simple_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    pages = {
        "employment_subjects": ("📚 دروس و منابع", employment_subjects_text()),
        "employment_iq": ("🧠 آزمون هوش و استعداد", employment_iq_text()),
        "employment_english": ("🇬🇧 زبان انگلیسی", employment_english_text()),
        "employment_full_exam": ("🏆 آزمون جامع استخدامی", employment_full_exam_text()),
        "employment_interview": ("🎤 آمادگی مصاحبه استخدامی", employment_interview_text()),
    }

    if query.data not in pages:
        return

    _, text = pages[query.data]
    await query.edit_message_text(text, reply_markup=employment_back_menu())


async def employment_bank_placeholder_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    parts = query.data.split("_", 2)
    bank_name = parts[2] if len(parts) == 3 else "بانک"

    labels = {
        "lesson": "📖 درسنامه",
        "questions": "📝 نمونه سؤالات",
        "exam": "⏱️ آزمون زمان‌دار",
        "tips": "🎯 نکات مهم",
    }

    action = parts[1] if len(parts) > 1 else "lesson"
    label = labels.get(action, "بخش موردنظر")

    await query.edit_message_text(
        f"""
{label}
━━━━━━━━━━━━━━━━━━
🚧 این بخش در حال توسعه است.
محتوای تخصصی این قسمت به‌زودی اضافه می‌شود.
""",
        reply_markup=employment_back_menu(),
    )


# =========================================================
# FUTURE EXAMS
# =========================================================
async def future_exam_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    titles = {
        "exam_management": "📚 آزمون مدیریت",
        "exam_trade": "🌍 آزمون تجارت",
        "exam_marketing": "📈 آزمون بازاریابی",
        "exam_economics": "💰 آزمون اقتصاد",
    }

    title = titles.get(query.data, "🎓 آزمون")
    keyboard = [
        [InlineKeyboardButton("🔙 آزمون و تست", callback_data="exams")],
        [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")],
    ]

    await query.edit_message_text(
        f"""
{title}
━━━━━━━━━━━━━━━━━━
برای شروع آزمون تخصصی، می‌توانید از منوی همان بخش وارد آزمون شوید.
""",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================================================
# REGISTER HANDLERS
# =========================================================
def register_handlers(application):
    # Home
    application.add_handler(CallbackQueryHandler(home_callback, pattern=r"^home$"))

    # Main sections
    application.add_handler(
        CallbackQueryHandler(section_callback, pattern=r"^(management|trade|marketing|economy)$")
    )

    # Exams menu
    application.add_handler(CallbackQueryHandler(exams_callback, pattern=r"^exams$"))

    # Banking
    application.add_handler(CallbackQueryHandler(banking_callback, pattern=r"^banking$"))
    application.add_handler(
        CallbackQueryHandler(
            banking_lesson_callback,
            pattern=r"^banking_(basics|deposits|facilities|contracts|laws|checks|aml|credit|electronic|risk|central|islamic)$",
        )
    )
    application.add_handler(CallbackQueryHandler(banking_quiz_start, pattern=r"^banking_quiz$"))
    application.add_handler(
        CallbackQueryHandler(
            banking_answer_callback,
            pattern=r"^banking_answer_\d+_\d+_\d+$",
        )
    )

    # Management
    application.add_handler(
        CallbackQueryHandler(
            management_basics_callback,
            pattern=r"^management_basics$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_lesson_callback,
            pattern=r"^(management_definition|management_functions|management_levels|management_roles|management_skills|efficiency_effectiveness|management_schools)$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_exam_start,
            pattern=r"^management_definition_exam$|^management_basics_exam$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_answer_callback,
            pattern=r"^mg_answer_\d+_\d+_\d+$",
        )
    )

    # Trade
    application.add_handler(
        CallbackQueryHandler(
            trade_lesson_callback,
            pattern=r"^(trade_basics|trade_documents|trade_logistics|trade_payment|trade_incoterms|trade_laws)$",
        )
    )
    application.add_handler(CallbackQueryHandler(trade_exam_start, pattern=r"^trade_exam$"))
    application.add_handler(
        CallbackQueryHandler(
            trade_answer_callback,
            pattern=r"^trade_answer_\d+_\d+_\d+$",
        )
    )

    # Marketing
    application.add_handler(
        CallbackQueryHandler(
            marketing_lesson_callback,
            pattern=r"^(marketing_basics|consumer_behavior|market_research|marketing_4p|marketing_stp|marketing_branding|sales_negotiation|sales_funnel|digital_marketing)$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(marketing_exam_start, pattern=r"^marketing_exam$")
    )
    application.add_handler(
        CallbackQueryHandler(
            marketing_answer_callback,
            pattern=r"^marketing_answer_\d+_\d+_\d+$",
        )
    )

    # Economy
    application.add_handler(
        CallbackQueryHandler(
            economy_lesson_callback,
            pattern=r"^(economy_basics|supply_demand|inflation|exchange_rate|monetary_policy|fiscal_policy|macroeconomics|microeconomics|capital_market)$",
        )
    )
    application.add_handler(CallbackQueryHandler(economy_exam_start, pattern=r"^economy_exam$"))
    application.add_handler(
        CallbackQueryHandler(
            economy_answer_callback,
            pattern=r"^economy_answer_\d+_\d+_\d+$",
        )
    )

    # Employment
    application.add_handler(CallbackQueryHandler(employment_callback, pattern=r"^employment$"))
    application.add_handler(
        CallbackQueryHandler(
            employment_bank_callback,
            pattern=r"^employment_(melli|mellat|tejarat|saderat|refah|shahr|maskan|keshavarzi|sepah|mehr)$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_simple_callback,
            pattern=r"^(employment_subjects|employment_iq|employment_english|employment_full_exam|employment_interview)$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_bank_placeholder_callback,
            pattern=r"^bank_(lesson|questions|exam|tips)_.+$",
        )
    )

    # Social
    application.add_handler(
        CallbackQueryHandler(social_callback, pattern=r"^social$")
    )

    # Old/future exam buttons
    application.add_handler(
        CallbackQueryHandler(
            future_exam_callback,
            pattern=r"^exam_(management|trade|marketing|economics)$",
        )
    )


# =========================================================
# MAIN
# =========================================================
def main():
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    register_handlers(application)

    print("🏛️ Andishkadeh Market Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
