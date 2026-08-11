# =========================================================
# 🏛️ ANDISHKADEH MANAGEMENT & MARKET BOT
# 🤖 MAIN BOT - FINAL CONNECTOR
# =========================================================
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
# =========================================================
# MENUS
# =========================================================
from menus import (
    main_menu,
    main_menu_text,
    management_menu,
    trade_menu,
    marketing_menu,
    economy_menu,
    economy_lesson_menu,
)
# =========================================================
# BANKING
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
    QUESTIONS as MANAGEMENT_QUESTIONS,
    exam_question as management_exam_question,
)
# =========================================================
# TRADE
# =========================================================
from trade import (
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
# MARKETING
# =========================================================
from marketing import (
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
# ECONOMY
# =========================================================
from economy import (
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
# EMPLOYMENT
# =========================================================
from employment import (
    BANKS,
    employment_menu,
    employment_text,
    banks_menu,
    bank_detail_menu,
    bank_detail_text,
    general_subjects_menu,
    general_subjects_text,
    specialized_subjects_menu,
    specialized_subjects_text,
    iq_menu,
    iq_text,
    english_menu,
    english_text,
    it_menu,
    it_text,
    roadmap_menu,
    roadmap_text,
    interview_menu,
    interview_text,
)
# =========================================================
# SOCIAL
# =========================================================
from social import social_callback
# =========================================================
# LOGGING
# =========================================================
logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
# =========================================================
# TOKEN
# =========================================================
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is not set."
    )
# =========================================================
# COMMON KEYBOARDS
# =========================================================
def home_keyboard():
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home",
                )
            ]
        ]
    )
# =========================================================
# /START
# =========================================================
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not update.message:
        return
    user = update.effective_user
    name = (
        user.first_name
        if user and user.first_name
        else "دوست عزیز"
    )
    text = f"""
سلام <b>{name}</b> 👋
به <b>اندیشکده مدیریت و بازار</b> خوش آمدید.
🎓 آموزش تخصصی
📝 آزمون و تست
📊 سنجش و تحلیل عملکرد
🏦 بانکداری
🎯 آمادگی استخدامی
🌍 تجارت بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
{main_menu_text()}
"""
    await update.message.reply_text(
        text,
        reply_markup=main_menu(),
        parse_mode="HTML",
    )
# =========================================================
# HOME
# =========================================================
async def home_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        main_menu_text(),
        reply_markup=main_menu(),
        parse_mode="HTML",
    )
# =========================================================
# MAIN SECTIONS
# =========================================================
async def section_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    sections = {
        "management": (
            """
📚 <b>مرکز آموزش مدیریت</b>
━━━━━━━━━━━━━━━━━━
مدیریت را مفهومی یاد بگیرید،
سپس با تست و تمرین آن را تثبیت کنید.
📖 مبانی مدیریت
📝 آزمون تخصصی
🎯 مفاهیم کاربردی
""",
            management_menu(),
        ),
        "trade": (
            """
🌍 <b>مرکز تجارت بین‌الملل</b>
━━━━━━━━━━━━━━━━━━
📘 مفاهیم پایه
📑 اسناد و قراردادها
🚚 لجستیک
💳 پرداخت بین‌المللی
🌐 Incoterms
⚖️ قوانین تجارت
""",
            trade_menu(),
        ),
        "marketing": (
            """
📈 <b>مرکز بازاریابی و فروش</b>
━━━━━━━━━━━━━━━━━━
📚 اصول بازاریابی
🧠 رفتار مصرف‌کننده
🎯 STP
🏷️ برندینگ
🤝 فروش و مذاکره
📱 بازاریابی دیجیتال
""",
            marketing_menu(),
        ),
        "economy": (
            """
💰 <b>مرکز اقتصاد و بازار</b>
━━━━━━━━━━━━━━━━━━
📚 مبانی اقتصاد
📈 عرضه و تقاضا
🔥 تورم
💱 نرخ ارز
🏦 سیاست پولی
💰 سیاست مالی
📊 اقتصاد کلان و خرد
📈 بازار سرمایه
""",
            economy_menu(),
        ),
    }
    data = query.data
    if data not in sections:
        return
    text, keyboard = sections[data]
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# BANKING
# =========================================================
async def banking_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        banking_intro_text,
        reply_markup=banking_menu(),
        parse_mode="HTML",
    )
# =========================================================
# BANKING LESSONS
# =========================================================
BANKING_LESSONS = {
    "banking_intro": lambda: banking_intro_text,
    "banking_basics": lambda: banking_basics_text,
    "banking_deposits": lambda: banking_deposits_text,
    "banking_facilities": lambda: banking_facilities_text,
    "banking_contracts": lambda: banking_contracts_text,
    "banking_laws": lambda: banking_laws_text,
    "banking_checks": lambda: banking_checks_text,
    "banking_aml": lambda: banking_aml_text,
    "banking_credit": lambda: banking_credit_text,
    "banking_electronic": lambda: banking_electronic_text,
    "banking_risk": lambda: banking_risk_text,
    "banking_central": lambda: banking_central_text,
    "banking_islamic": lambda: banking_islamic_text,
}
async def banking_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    getter = BANKING_LESSONS.get(
        query.data
    )
    if not getter:
        return
    text = getter()
    await query.edit_message_text(
        text,
        reply_markup=banking_back_menu(),
        parse_mode="HTML",
    )
# =========================================================
# BANKING QUIZ
# =========================================================
async def banking_quiz_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    if not BANKING_QUESTIONS:
        await query.edit_message_text(
            "⚠️ سؤال فعالی برای آزمون بانکداری وجود ندارد.",
            reply_markup=banking_back_menu(),
        )
        return
    text, keyboard = banking_quiz_question(
        index=0,
        score=0,
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )
async def banking_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        parts = query.data.split("_")
        question_index = int(parts[2])
        selected_answer = int(parts[3])
        score = int(parts[4])
    except (
        ValueError,
        IndexError,
    ):
        await query.edit_message_text(
            "❌ خطا در پردازش پاسخ.",
            reply_markup=banking_back_menu(),
        )
        return
    if not (
        0
        <= question_index
        < len(BANKING_QUESTIONS)
    ):
        await query.edit_message_text(
            "❌ سؤال موردنظر پیدا نشد.",
            reply_markup=banking_back_menu(),
        )
        return
    question = BANKING_QUESTIONS[
        question_index
    ]
    if selected_answer == question["correct"]:
        score += 1
        result = (
            "✅ <b>پاسخ صحیح است.</b>"
        )
    else:
        correct = question["options"][
            question["correct"]
        ]
        result = (
            "❌ <b>پاسخ اشتباه است.</b>\n\n"
            f"✅ پاسخ صحیح: <b>{correct}</b>"
        )
    next_index = question_index + 1
    if next_index >= len(
        BANKING_QUESTIONS
    ):
        total = len(
            BANKING_QUESTIONS
        )
        percentage = (
            int(
                score
                / total
                * 100
            )
            if total
            else 0
        )
        if percentage >= 90:
            level = "🏆 استاد بانکداری"
        elif percentage >= 80:
            level = "🔥 حرفه‌ای"
        elif percentage >= 70:
            level = "⭐ خوب"
        elif percentage >= 50:
            level = "📚 متوسط"
        else:
            level = "🔄 نیازمند مرور"
        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup,
        )
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔄 تکرار آزمون",
                        callback_data="banking_quiz",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏦 بانکداری",
                        callback_data="banking",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home",
                    )
                ],
            ]
        )
        await query.edit_message_text(
            f"""
🏆 <b>آزمون بانکداری به پایان رسید</b>
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
<b>{score} از {total}</b>
📊 درصد:
<b>{percentage}٪</b>
🎯 سطح:
<b>{level}</b>
━━━━━━━━━━━━━━━━━━
{result}
💡 پاسخ‌های اشتباه را مرور کنید
و دوباره آزمون را انجام دهید.
""",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
        return
    text, keyboard = banking_quiz_question(
        index=next_index,
        score=score,
    )
    await query.edit_message_text(
        f"""
{result}
━━━━━━━━━━━━━━━━━━
{text}
""",
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# MANAGEMENT
# =========================================================
MANAGEMENT_LESSONS = {
    "management_definition":
        management_definition_text,
    "management_functions":
        management_functions_text,
    "management_levels":
        management_levels_text,
    "management_roles":
        management_roles_text,
    "management_skills":
        management_skills_text,
    "efficiency_effectiveness":
        efficiency_effectiveness_text,
    "management_schools":
        management_schools_text,
}
async def management_basics_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
📚 <b>مبانی مدیریت</b>
━━━━━━━━━━━━━━━━━━
📖 درسنامه‌های تخصصی مدیریت
📝 آزمون مبانی مدیریت
🎯 مفاهیم کلیدی
""",
        reply_markup=management_basics_menu(),
        parse_mode="HTML",
    )
async def management_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    func = MANAGEMENT_LESSONS.get(
        query.data
    )
    if not func:
        return
    keyboard = (
        management_definition_menu()
        if query.data
        == "management_definition"
        else lesson_menu()
    )
    await query.edit_message_text(
        func(),
        reply_markup=keyboard,
        parse_mode="HTML",
    )
async def management_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    text, keyboard = management_exam_question(
        index=0,
        score=0,
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )
async def management_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        parts = query.data.split("_")
        index = int(parts[2])
        selected = int(parts[3])
        score = int(parts[4])
    except (
        ValueError,
        IndexError,
    ):
        await query.edit_message_text(
            "❌ خطا در پردازش پاسخ.",
            reply_markup=management_basics_menu(),
        )
        return
    if not (
        0 <= index < len(
            MANAGEMENT_QUESTIONS
        )
    ):
        return
    question = MANAGEMENT_QUESTIONS[
        index
    ]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: "
            f"{question['options'][question['correct']]}"
        )
    next_index = index + 1
    if next_index >= len(
        MANAGEMENT_QUESTIONS
    ):
        total = len(
            MANAGEMENT_QUESTIONS
        )
        percentage = (
            int(score / total * 100)
            if total
            else 0
        )
        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup,
        )
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔄 تکرار آزمون",
                        callback_data="management_basics_exam",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 مبانی مدیریت",
                        callback_data="management_basics",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home",
                    )
                ],
            ]
        )
        await query.edit_message_text(
            f"""
🏆 <b>آزمون مدیریت تمام شد</b>
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
<b>{score} از {total}</b>
📊 درصد:
<b>{percentage}٪</b>
━━━━━━━━━━━━━━━━━━
{result}
""",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
        return
    text, keyboard = management_exam_question(
        index=next_index,
        score=score,
    )
    await query.edit_message_text(
        f"{result}\n\n━━━━━━━━━━━━━━━━━━\n\n{text}",
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# TRADE
# =========================================================
TRADE_LESSONS = {
    "trade_basics":
        trade_basics_text,
    "trade_documents":
        trade_documents_text,
    "trade_logistics":
        trade_logistics_text,
    "trade_payment":
        trade_payment_text,
    "trade_incoterms":
        trade_incoterms_text,
    "trade_laws":
        trade_laws_text,
}
async def trade_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    func = TRADE_LESSONS.get(
        query.data
    )
    if not func:
        return
    await query.edit_message_text(
        func(),
        reply_markup=trade_menu(),
        parse_mode="HTML",
    )
async def trade_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    text, keyboard = trade_exam_question(
        index=0,
        score=0,
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )
async def trade_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        parts = query.data.split("_")
        index = int(parts[2])
        selected = int(parts[3])
        score = int(parts[4])
    except (
        ValueError,
        IndexError,
    ):
        await query.edit_message_text(
            "❌ خطا در پردازش پاسخ.",
            reply_markup=trade_menu(),
        )
        return
    question = TRADE_QUESTIONS[index]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: "
            f"{question['options'][question['correct']]}"
        )
    next_index = index + 1
    if next_index >= len(
        TRADE_QUESTIONS
    ):
        total = len(
            TRADE_QUESTIONS
        )
        percentage = (
            int(score / total * 100)
            if total
            else 0
        )
        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup,
        )
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔄 تکرار آزمون",
                        callback_data="trade_exam",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌍 تجارت",
                        callback_data="trade",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home",
                    )
                ],
            ]
        )
        await query.edit_message_text(
            f"""
🏆 <b>آزمون تجارت به پایان رسید</b>
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
<b>{score} از {total}</b>
📊 درصد:
<b>{percentage}٪</b>
━━━━━━━━━━━━━━━━━━
{result}
""",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
        return
    text, keyboard = trade_exam_question(
        index=next_index,
        score=score,
    )
    await query.edit_message_text(
        f"{result}\n\n━━━━━━━━━━━━━━━━━━\n\n{text}",
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# MARKETING
# =========================================================
MARKETING_LESSONS = {
    "marketing_basics":
        marketing_basics_text,
    "consumer_behavior":
        consumer_behavior_text,
    "market_research":
        market_research_text,
    "marketing_4p":
        marketing_4p_text,
    "marketing_stp":
        marketing_stp_text,
    "marketing_branding":
        marketing_branding_text,
    "sales_negotiation":
        sales_negotiation_text,
    "sales_funnel":
        sales_funnel_text,
    "digital_marketing":
        digital_marketing_text,
}
async def marketing_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    func = MARKETING_LESSONS.get(
        query.data
    )
    if not func:
        return
    from menus import marketing_menu
    await query.edit_message_text(
        func(),
        reply_markup=marketing_menu(),
        parse_mode="HTML",
    )
async def marketing_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    text, keyboard = marketing_exam_question(
        index=0,
        score=0,
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )
async def marketing_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        parts = query.data.split("_")
        index = int(parts[2])
        selected = int(parts[3])
        score = int(parts[4])
    except (
        ValueError,
        IndexError,
    ):
        return
    question = MARKETING_QUESTIONS[
        index
    ]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: "
            f"{question['options'][question['correct']]}"
        )
    next_index = index + 1
    if next_index >= len(
        MARKETING_QUESTIONS
    ):
        total = len(
            MARKETING_QUESTIONS
        )
        percentage = (
            int(score / total * 100)
            if total
            else 0
        )
        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup,
        )
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔄 تکرار آزمون",
                        callback_data="marketing_exam",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📈 بازاریابی",
                        callback_data="marketing",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home",
                    )
                ],
            ]
        )
        await query.edit_message_text(
            f"""
🏆 <b>آزمون بازاریابی تمام شد</b>
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
<b>{score} از {total}</b>
📊 درصد:
<b>{percentage}٪</b>
━━━━━━━━━━━━━━━━━━
{result}
""",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
        return
    text, keyboard = marketing_exam_question(
        index=next_index,
        score=score,
    )
    await query.edit_message_text(
        f"{result}\n\n━━━━━━━━━━━━━━━━━━\n\n{text}",
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# ECONOMY
# =========================================================
ECONOMY_LESSONS = {
    "economy_basics":
        economy_basics_text,
    "supply_demand":
        supply_demand_text,
    "inflation":
        inflation_text,
    "exchange_rate":
        exchange_rate_text,
    "monetary_policy":
        monetary_policy_text,
    "fiscal_policy":
        fiscal_policy_text,
    "macroeconomics":
        macroeconomics_text,
    "microeconomics":
        microeconomics_text,
    "capital_market":
        capital_market_text,
}
async def economy_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    func = ECONOMY_LESSONS.get(
        query.data
    )
    if not func:
        return
    await query.edit_message_text(
        func(),
        reply_markup=economy_lesson_menu(),
        parse_mode="HTML",
    )
async def economy_exam_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    text, keyboard = economy_exam_question(
        index=0,
        score=0,
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
    )
async def economy_answer_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        parts = query.data.split("_")
        index = int(parts[2])
        selected = int(parts[3])
        score = int(parts[4])
    except (
        ValueError,
        IndexError,
    ):
        return
    question = ECONOMY_QUESTIONS[
        index
    ]
    if selected == question["correct"]:
        score += 1
        result = "✅ پاسخ صحیح است."
    else:
        result = (
            "❌ پاسخ اشتباه است.\n"
            f"✅ پاسخ صحیح: "
            f"{question['options'][question['correct']]}"
        )
    next_index = index + 1
    if next_index >= len(
        ECONOMY_QUESTIONS
    ):
        total = len(
            ECONOMY_QUESTIONS
        )
        percentage = (
            int(score / total * 100)
            if total
            else 0
        )
        from telegram import (
            InlineKeyboardButton,
            InlineKeyboardMarkup,
        )
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔄 تکرار آزمون",
                        callback_data="economy_exam",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💰 اقتصاد",
                        callback_data="economy",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home",
                    )
                ],
            ]
        )
        await query.edit_message_text(
            f"""
🏆 <b>آزمون اقتصاد تمام شد</b>
━━━━━━━━━━━━━━━━━━
⭐ امتیاز:
<b>{score} از {total}</b>
📊 درصد:
<b>{percentage}٪</b>
━━━━━━━━━━━━━━━━━━
{result}
""",
            reply_markup=keyboard,
            parse_mode="HTML",
        )
        return
    text, keyboard = economy_exam_question(
        index=next_index,
        score=score,
    )
    await query.edit_message_text(
        f"{result}\n\n━━━━━━━━━━━━━━━━━━\n\n{text}",
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# EXAMS CENTER
# =========================================================
def exams_menu():
    from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
    )
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 مدیریت",
                    callback_data="management_basics_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "🌍 تجارت",
                    callback_data="trade_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "📈 بازاریابی",
                    callback_data="marketing_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "💰 اقتصاد",
                    callback_data="economy_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏦 بانکداری",
                    callback_data="banking_quiz",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home",
                )
            ],
        ]
    )
async def exams_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
🎓 <b>مرکز آزمون اندیشکده</b>
━━━━━━━━━━━━━━━━━━
📝 آزمون‌های تخصصی
🎯 سنجش دانش
📊 محاسبه درصد
🏆 ارزیابی عملکرد
مسیر پیشنهادی:
📖 آموزش
⬇️
📝 تست
⬇️
🔄 مرور اشتباهات
⬇️
🏆 آزمون مجدد
""",
        reply_markup=exams_menu(),
        parse_mode="HTML",
    )
# =========================================================
# EMPLOYMENT
# =========================================================
async def employment_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        employment_text(),
        reply_markup=employment_menu(),
        parse_mode="HTML",
    )
async def employment_banks_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
🏦 <b>بانک‌های هدف</b>
بانک موردنظر خود را انتخاب کنید:
""",
        reply_markup=banks_menu(),
        parse_mode="HTML",
    )
async def employment_bank_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    prefix = "employment_bank_"
    if not query.data.startswith(prefix):
        return
    bank_key = query.data[
        len(prefix):
    ]
    if bank_key not in BANKS:
        await query.edit_message_text(
            "⚠️ بانک موردنظر پیدا نشد.",
            reply_markup=banks_menu(),
        )
        return
    await query.edit_message_text(
        bank_detail_text(bank_key),
        reply_markup=bank_detail_menu(bank_key),
        parse_mode="HTML",
    )
async def employment_general_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        general_subjects_text(),
        reply_markup=general_subjects_menu(),
        parse_mode="HTML",
    )
async def employment_specialized_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        specialized_subjects_text(),
        reply_markup=specialized_subjects_menu(),
        parse_mode="HTML",
    )
async def employment_iq_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        iq_text(),
        reply_markup=iq_menu(),
        parse_mode="HTML",
    )
async def employment_english_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        english_text(),
        reply_markup=english_menu(),
        parse_mode="HTML",
    )
async def employment_it_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        it_text(),
        reply_markup=it_menu(),
        parse_mode="HTML",
    )
async def employment_roadmap_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        roadmap_text(),
        reply_markup=roadmap_menu(),
        parse_mode="HTML",
    )
async def employment_interview_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        interview_text(),
        reply_markup=interview_menu(),
        parse_mode="HTML",
    )
# =========================================================
# EMPLOYMENT BANK ACTIONS
# =========================================================
async def employment_bank_action_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    if len(parts) < 3:
        return
    action = parts[1]
    bank_key = "_".join(parts[2:])
    bank = BANKS.get(bank_key)
    if not bank:
        return
    labels = {
        "subjects":
            "📚 منابع و دروس",
        "questions":
            "📝 نمونه سؤالات",
        "exam":
            "⏱️ آزمون زمان‌دار",
        "tips":
            "🎯 نکات مهم آزمونی",
        "interview":
            "🎤 آمادگی مصاحبه",
    }
    title = labels.get(
        action,
        "🎯 بخش استخدامی",
    )
    await query.edit_message_text(
        f"""
{title}
━━━━━━━━━━━━━━━━━━
🏦 <b>{bank["name"]}</b>
این بخش در نسخه فعلی به مرکز
محتوای تخصصی بانک متصل شده است.
📌 توجه:
شرایط استخدام، مواد آزمون و مراحل
هر فراخوان ممکن است متفاوت باشد.
برای اطلاعات قطعی، دفترچه رسمی
همان فراخوان را ملاک قرار دهید.
""",
        reply_markup=bank_detail_menu(
            bank_key
        ),
        parse_mode="HTML",
    )
# =========================================================
# BANKING FULL EXAM REDIRECT
# =========================================================
async def banking_full_exam_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
🏆 <b>آزمون جامع بانکداری</b>
━━━━━━━━━━━━━━━━━━
این آزمون برای سنجش دانش شما
در مهم‌ترین مباحث بانکداری طراحی شده است.
📚 مبانی
💰 سپرده‌ها
💳 تسهیلات
📑 عقود
⚖️ قوانین
🔐 مبارزه با پولشویی
📊 اعتبارسنجی
💻 بانکداری الکترونیک
📈 مدیریت ریسک
👇 برای شروع، آزمون تخصصی را اجرا کنید.
""",
        reply_markup=banking_back_menu(),
        parse_mode="HTML",
    )
# =========================================================
# REGISTER HANDLERS
# =========================================================
def register_handlers(
    application: Application
):
    # =====================================================
    # COMMANDS
    # =====================================================
    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )
    # =====================================================
    # HOME
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern=r"^home$",
        )
    )
    # =====================================================
    # MAIN SECTIONS
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            section_callback,
            pattern=r"^(management|trade|marketing|economy)$",
        )
    )
    # =====================================================
    # EXAMS
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            exams_callback,
            pattern=r"^exams$",
        )
    )
    # =====================================================
    # BANKING
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            banking_callback,
            pattern=r"^banking$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_lesson_callback,
            pattern=(
                r"^banking_"
                r"(intro|basics|deposits|facilities|contracts|"
                r"laws|checks|aml|credit|electronic|risk|"
                r"central|islamic)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_start,
            pattern=r"^banking_quiz$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_answer_callback,
            pattern=r"^banking_answer_\d+_\d+_\d+$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_full_exam_callback,
            pattern=r"^banking_full_exam$",
        )
    )
    # =====================================================
    # MANAGEMENT
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            management_basics_callback,
            pattern=r"^management_basics$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_lesson_callback,
            pattern=(
                r"^(management_definition|management_functions|"
                r"management_levels|management_roles|"
                r"management_skills|efficiency_effectiveness|"
                r"management_schools)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_exam_start,
            pattern=r"^management_basics_exam$|^management_definition_exam$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            management_answer_callback,
            pattern=r"^mg_answer_\d+_\d+_\d+$",
        )
    )
    # =====================================================
    # TRADE
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            trade_lesson_callback,
            pattern=(
                r"^(trade_basics|trade_documents|"
                r"trade_logistics|trade_payment|"
                r"trade_incoterms|trade_laws)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            trade_exam_start,
            pattern=r"^trade_exam$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            trade_answer_callback,
            pattern=r"^trade_answer_\d+_\d+_\d+$",
        )
    )
    # =====================================================
    # MARKETING
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            marketing_lesson_callback,
            pattern=(
                r"^(marketing_basics|consumer_behavior|"
                r"market_research|marketing_4p|marketing_stp|"
                r"marketing_branding|sales_negotiation|"
                r"sales_funnel|digital_marketing)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            marketing_exam_start,
            pattern=r"^marketing_exam$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            marketing_answer_callback,
            pattern=r"^marketing_answer_\d+_\d+_\d+$",
        )
    )
    # =====================================================
    # ECONOMY
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            economy_lesson_callback,
            pattern=(
                r"^(economy_basics|supply_demand|inflation|"
                r"exchange_rate|monetary_policy|fiscal_policy|"
                r"macroeconomics|microeconomics|capital_market)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            economy_exam_start,
            pattern=r"^economy_exam$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            economy_answer_callback,
            pattern=r"^economy_answer_\d+_\d+_\d+$",
        )
    )
    # =====================================================
    # EMPLOYMENT
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            employment_callback,
            pattern=r"^employment$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_banks_callback,
            pattern=r"^employment_banks$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_general_callback,
            pattern=r"^employment_general_subjects$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_specialized_callback,
            pattern=r"^employment_specialized_subjects$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_iq_callback,
            pattern=r"^employment_iq$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_english_callback,
            pattern=r"^employment_english$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_it_callback,
            pattern=r"^employment_it$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_roadmap_callback,
            pattern=r"^employment_roadmap$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_interview_callback,
            pattern=r"^employment_interview$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_bank_callback,
            pattern=r"^employment_bank_.+$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_bank_action_callback,
            pattern=r"^bank_(subjects|questions|exam|tips|interview)_.+$",
        )
    )
    # =====================================================
    # SOCIAL
    # =====================================================
    application.add_handler(
        CallbackQueryHandler(
            social_callback,
            pattern=r"^social$",
        )
    )
# =========================================================
# ERROR HANDLER
# =========================================================
async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):
    logger.error(
        "Unhandled exception while processing update",
        exc_info=context.error,
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
    register_handlers(
        application
    )
    application.add_error_handler(
        error_handler
    )
    logger.info(
        "🏛️ Andishkadeh Market Bot started successfully."
    )
    print(
        "🏛️ Andishkadeh Market Bot is running..."
    )
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )
# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    main()
