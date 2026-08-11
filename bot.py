# =========================================================
# 🏛️ ANDISHKADEH MANAGEMENT & MARKET BOT
# 🤖 MAIN BOT
# =========================================================
import os
import logging
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
# MENUS
# =========================================================
from menus import (
    main_menu,
    main_menu_text,
    management_menu,
    trade_menu,
    marketing_menu,
    economy_menu,
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
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is not set."
    )
# =========================================================
# ECONOMY LESSON MENU
# =========================================================
def economy_lesson_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 مبانی علم اقتصاد",
                    callback_data="economy_basics",
                ),
                InlineKeyboardButton(
                    "📈 عرضه و تقاضا",
                    callback_data="supply_demand",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🔥 تورم و شاخص قیمت‌ها",
                    callback_data="inflation",
                ),
                InlineKeyboardButton(
                    "💱 نرخ ارز",
                    callback_data="exchange_rate",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏦 سیاست پولی",
                    callback_data="monetary_policy",
                ),
                InlineKeyboardButton(
                    "💰 سیاست مالی",
                    callback_data="fiscal_policy",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📊 اقتصاد کلان",
                    callback_data="macroeconomics",
                ),
                InlineKeyboardButton(
                    "📉 اقتصاد خرد",
                    callback_data="microeconomics",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📈 بازار سرمایه",
                    callback_data="capital_market",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🔙 اقتصاد و بازار",
                    callback_data="economy",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home",
                ),
            ],
        ]
    )
# =========================================================
# HOME KEYBOARD
# =========================================================
def home_keyboard():
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
🏛️ <b>به اندیشکده مدیریت و بازار خوش آمدید</b>
مرکز تخصصی:
📚 آموزش
📝 آزمون
📊 تحلیل عملکرد
🏦 بانکداری
🎯 استخدام بانک‌ها
🌍 تجارت بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
━━━━━━━━━━━━━━━━━━
اینجا فقط قرار نیست مطالعه کنید؛
قرار است <b>یاد بگیرید، تست بزنید و پیشرفت خودتان را بسنجید.</b>
👇 از منوی زیر شروع کنید.
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
مدیریت را از مفاهیم پایه تا
مباحث تخصصی یاد بگیرید.
📖 درسنامه
🧠 مفاهیم کلیدی
📝 آزمون
🎯 آمادگی آزمون‌های تخصصی
""",
            management_menu(),
        ),
        "trade": (
            """
🌍 <b>مرکز تجارت بین‌الملل</b>
━━━━━━━━━━━━━━━━━━
📚 مفاهیم پایه تجارت
📑 اسناد و قراردادهای تجاری
🚚 حمل‌ونقل و لجستیک
💳 روش‌های پرداخت
🌐 Incoterms
⚖️ قوانین و سازمان‌های تجاری
👇 بخش موردنظر را انتخاب کنید.
""",
            trade_menu(),
        ),
        "marketing": (
            """
📈 <b>مرکز بازاریابی و فروش</b>
━━━━━━━━━━━━━━━━━━
📚 اصول بازاریابی
🧠 رفتار مصرف‌کننده
🔎 تحقیقات بازار
🎯 STP
🏷️ برندینگ
🤝 فروش و مذاکره
📱 بازاریابی دیجیتال
👇 مسیر یادگیری خود را انتخاب کنید.
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
📊 اقتصاد کلان
📉 اقتصاد خرد
📈 بازار سرمایه
👇 موضوع موردنظر را انتخاب کنید.
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
    "banking_intro": banking_intro_text,
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
async def banking_lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    text = BANKING_LESSONS.get(
        query.data
    )
    if not text:
        return
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
            """
⚠️ <b>آزمون بانکداری</b>
در حال حاضر سؤالی برای این آزمون
ثبت نشده است.
""",
            reply_markup=banking_back_menu(),
            parse_mode="HTML",
        )
        return
    try:
        text, keyboard = banking_quiz_question(
            0,
            0,
        )
    except TypeError:
        try:
            text, keyboard = banking_quiz_question(
                index=0,
                score=0,
            )
        except Exception as error:
            logger.exception(error)
            await query.edit_message_text(
                "❌ خطا در اجرای آزمون بانکداری.",
                reply_markup=banking_back_menu(),
            )
            return
    await query.edit_message_text(
        text,
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
از این بخش می‌توانید مفاهیم اصلی
مدیریت را مرحله‌به‌مرحله مطالعه کنید.
📖 آموزش
📝 تست
🎯 مرور مفاهیم
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
    try:
        text = func()
    except TypeError:
        text = func
    await query.edit_message_text(
        text,
        reply_markup=lesson_menu(),
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
    try:
        text = func()
    except TypeError:
        text = func
    await query.edit_message_text(
        text,
        reply_markup=trade_menu(),
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
    try:
        text = func()
    except TypeError:
        text = func
    await query.edit_message_text(
        text,
        reply_markup=marketing_menu(),
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
    try:
        text = func()
    except TypeError:
        text = func
    await query.edit_message_text(
        text,
        reply_markup=economy_lesson_menu(),
        parse_mode="HTML",
    )
# =========================================================
# EXAMS MENU
# =========================================================
def exams_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 مدیریت",
                    callback_data="management_exam",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🌍 تجارت بین‌الملل",
                    callback_data="trade_exam",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📈 بازاریابی و فروش",
                    callback_data="marketing_exam",
                ),
            ],
            [
                InlineKeyboardButton(
                    "💰 اقتصاد و بازار",
                    callback_data="economy_exam",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏦 بانکداری",
                    callback_data="banking_quiz",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home",
                ),
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
🎓 <b>مرکز آزمون</b>
━━━━━━━━━━━━━━━━━━
در این بخش می‌توانید دانش خود را
در حوزه‌های مختلف بسنجید.
📊 امتیاز
📈 درصد
🏆 ارزیابی
🔄 آزمون مجدد
👇 حوزه آزمون را انتخاب کنید.
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
    try:
        text = employment_text()
    except TypeError:
        text = employment_text
    await query.edit_message_text(
        text,
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
🏦 <b>آزمون‌های استخدامی بانک‌ها</b>
━━━━━━━━━━━━━━━━━━
بانک موردنظر خود را انتخاب کنید:
🎯 منابع
📝 سؤالات
📚 دروس
🎤 مصاحبه
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
    bank_key = query.data[
        len(prefix):
    ]
    if bank_key not in BANKS:
        await query.edit_message_text(
            "⚠️ بانک موردنظر پیدا نشد.",
            reply_markup=banks_menu(),
        )
        return
    try:
        text = bank_detail_text(
            bank_key
        )
    except TypeError:
        text = bank_detail_text
    await query.edit_message_text(
        text,
        reply_markup=bank_detail_menu(
            bank_key
        ),
        parse_mode="HTML",
    )
async def employment_general_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = general_subjects_text()
    except TypeError:
        text = general_subjects_text
    await query.edit_message_text(
        text,
        reply_markup=general_subjects_menu(),
        parse_mode="HTML",
    )
async def employment_specialized_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = specialized_subjects_text()
    except TypeError:
        text = specialized_subjects_text
    await query.edit_message_text(
        text,
        reply_markup=specialized_subjects_menu(),
        parse_mode="HTML",
    )
async def employment_iq_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = iq_text()
    except TypeError:
        text = iq_text
    await query.edit_message_text(
        text,
        reply_markup=iq_menu(),
        parse_mode="HTML",
    )
async def employment_english_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = english_text()
    except TypeError:
        text = english_text
    await query.edit_message_text(
        text,
        reply_markup=english_menu(),
        parse_mode="HTML",
    )
async def employment_it_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = it_text()
    except TypeError:
        text = it_text
    await query.edit_message_text(
        text,
        reply_markup=it_menu(),
        parse_mode="HTML",
    )
async def employment_roadmap_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = roadmap_text()
    except TypeError:
        text = roadmap_text
    await query.edit_message_text(
        text,
        reply_markup=roadmap_menu(),
        parse_mode="HTML",
    )
async def employment_interview_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    try:
        text = interview_text()
    except TypeError:
        text = interview_text
    await query.edit_message_text(
        text,
        reply_markup=interview_menu(),
        parse_mode="HTML",
    )
# =========================================================
# SOCIAL
# =========================================================
async def social_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await social_callback(
        update,
        context,
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
# REGISTER HANDLERS
# =========================================================
def register_handlers(
    application: Application
):
    # -----------------------------------------------------
    # COMMANDS
    # -----------------------------------------------------
    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )
    # -----------------------------------------------------
    # HOME
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern=r"^home$",
        )
    )
    # -----------------------------------------------------
    # MAIN SECTIONS
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            section_callback,
            pattern=r"^(management|trade|marketing|economy)$",
        )
    )
    # -----------------------------------------------------
    # EXAMS
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exams_callback,
            pattern=r"^exam$|^exams$",
        )
    )
    # -----------------------------------------------------
    # BANKING
    # -----------------------------------------------------
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
                r"(intro|basics|deposits|facilities|"
                r"contracts|laws|checks|aml|credit|"
                r"electronic|risk|central|islamic)$"
            ),
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_start,
            pattern=r"^banking_quiz$",
        )
    )
    # -----------------------------------------------------
    # MANAGEMENT
    # -----------------------------------------------------
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
                r"^(management_definition|"
                r"management_functions|"
                r"management_levels|"
                r"management_roles|"
                r"management_skills|"
                r"efficiency_effectiveness|"
                r"management_schools)$"
            ),
        )
    )
    # -----------------------------------------------------
    # TRADE
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            trade_lesson_callback,
            pattern=(
                r"^(trade_basics|"
                r"trade_documents|"
                r"trade_logistics|"
                r"trade_payment|"
                r"trade_incoterms|"
                r"trade_laws)$"
            ),
        )
    )
    # -----------------------------------------------------
    # MARKETING
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            marketing_lesson_callback,
            pattern=(
                r"^(marketing_basics|"
                r"consumer_behavior|"
                r"market_research|"
                r"marketing_4p|"
                r"marketing_stp|"
                r"marketing_branding|"
                r"sales_negotiation|"
                r"sales_funnel|"
                r"digital_marketing)$"
            ),
        )
    )
    # -----------------------------------------------------
    # ECONOMY
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            economy_lesson_callback,
            pattern=(
                r"^(economy_basics|"
                r"supply_demand|"
                r"inflation|"
                r"exchange_rate|"
                r"monetary_policy|"
                r"fiscal_policy|"
                r"macroeconomics|"
                r"microeconomics|"
                r"capital_market)$"
            ),
        )
    )
    # -----------------------------------------------------
    # EMPLOYMENT
    # -----------------------------------------------------
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
            pattern=r"^employment_general$|^employment_general_subjects$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            employment_specialized_callback,
            pattern=r"^employment_specialized$|^employment_specialized_subjects$",
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
    # -----------------------------------------------------
    # SOCIAL
    # -----------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            social_handler,
            pattern=r"^social$",
        )
    )
# =========================================================
# MAIN
# =========================================================
def main():
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )
    register_handlers(
        application
    )
    application.add_error_handler(
        error_handler
    )
    logger.info(
        "🏛️ Andishkadeh Market Bot started."
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
