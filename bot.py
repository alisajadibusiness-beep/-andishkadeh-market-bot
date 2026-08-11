# ============================================================
# 🏛️ ANDISHKADEH MARKET BOT
# Telegram Educational & Exam Bot
# ============================================================
import os
import logging
import importlib
from typing import Any
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
# ============================================================
# CONFIG
# ============================================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is not set."
    )
# ============================================================
# LOGGING
# ============================================================
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("andishkadeh")
# ============================================================
# SAFE MODULE LOADER
# ============================================================
def load_module(name: str):
    try:
        return importlib.import_module(name)
    except Exception as error:
        logger.warning(
            "Could not load module '%s': %s",
            name,
            error,
        )
        return None
menus = load_module("menus")
banking = load_module("banking")
management = load_module("management")
trade = load_module("trade")
marketing = load_module("marketing")
economy = load_module("economy")
employment = load_module("employment")
social = load_module("social")
# ============================================================
# SAFE ATTRIBUTE
# ============================================================
def get_attr(
    module: Any,
    name: str,
    default=None,
):
    if module is None:
        return default
    return getattr(
        module,
        name,
        default,
    )
# ============================================================
# SAFE CALL
# ============================================================
def safe_call(
    value,
    default="",
):
    if value is None:
        return default
    if callable(value):
        try:
            return value()
        except TypeError:
            try:
                return value
            except Exception:
                return default
        except Exception as error:
            logger.warning(
                "Function execution error: %s",
                error,
            )
            return default
    return value
# ============================================================
# MAIN MENU
# ============================================================
def main_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 آموزش مدیریت",
                    callback_data="management",
                ),
                InlineKeyboardButton(
                    "🌍 تجارت بین‌الملل",
                    callback_data="trade",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📈 بازاریابی و فروش",
                    callback_data="marketing",
                ),
                InlineKeyboardButton(
                    "💰 اقتصاد و بازار",
                    callback_data="economy",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏦 بانکداری",
                    callback_data="banking",
                ),
                InlineKeyboardButton(
                    "🎓 آزمون و تست",
                    callback_data="exam",
                ),
            ],
            [
                InlineKeyboardButton(
                    "🏆 آزمون استخدامی بانک‌ها",
                    callback_data="employment",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📂 فایل و جزوات",
                    callback_data="files",
                ),
                InlineKeyboardButton(
                    "📱 شبکه‌های اجتماعی",
                    callback_data="social",
                ),
            ],
        ]
    )
def home_text():
    custom_text = get_attr(
        menus,
        "main_menu_text",
    )
    text = safe_call(
        custom_text,
        "",
    )
    if text:
        return text
    return """
🏛️ <b>اندیشکده مدیریت و بازار</b>
━━━━━━━━━━━━━━━━━━
🎯 <b>یادگیری | آزمون | تحلیل عملکرد</b>
مرجع تخصصی آموزش و آمادگی آزمون در حوزه‌های:
📚 مدیریت
🌍 تجارت بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
🏦 بانکداری
🎓 آزمون‌های استخدامی بانک‌ها
━━━━━━━━━━━━━━━━━━
از منوی زیر مسیر موردنظر خود را انتخاب کنید 👇
"""
# ============================================================
# GENERIC BACK BUTTON
# ============================================================
def back_home_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 بازگشت به منوی اصلی",
                    callback_data="home",
                )
            ]
        ]
    )
# ============================================================
# SECTION KEYBOARDS
# ============================================================
def management_keyboard():
    custom = get_attr(
        management,
        "management_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📖 مبانی مدیریت",
                    callback_data="management_basics",
                )
            ],
            [
                InlineKeyboardButton(
                    "📝 آزمون مدیریت",
                    callback_data="management_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
def trade_keyboard():
    custom = get_attr(
        trade,
        "trade_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 مفاهیم پایه تجارت",
                    callback_data="trade_basics",
                )
            ],
            [
                InlineKeyboardButton(
                    "📑 اسناد و قراردادهای تجاری",
                    callback_data="trade_documents",
                )
            ],
            [
                InlineKeyboardButton(
                    "🚚 حمل‌ونقل و لجستیک",
                    callback_data="trade_logistics",
                )
            ],
            [
                InlineKeyboardButton(
                    "💳 روش‌های پرداخت بین‌المللی",
                    callback_data="trade_payment",
                )
            ],
            [
                InlineKeyboardButton(
                    "🌐 اینکوترمز",
                    callback_data="trade_incoterms",
                )
            ],
            [
                InlineKeyboardButton(
                    "⚖️ قوانین تجارت",
                    callback_data="trade_laws",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
def marketing_keyboard():
    custom = get_attr(
        marketing,
        "marketing_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 اصول بازاریابی",
                    callback_data="marketing_basics",
                )
            ],
            [
                InlineKeyboardButton(
                    "🧠 رفتار مصرف‌کننده",
                    callback_data="consumer_behavior",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔎 تحقیقات بازار",
                    callback_data="market_research",
                )
            ],
            [
                InlineKeyboardButton(
                    "🎯 آمیخته بازاریابی 4P",
                    callback_data="marketing_4p",
                )
            ],
            [
                InlineKeyboardButton(
                    "📊 STP و بخش‌بندی بازار",
                    callback_data="marketing_stp",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏷️ برندینگ",
                    callback_data="marketing_branding",
                )
            ],
            [
                InlineKeyboardButton(
                    "🤝 فروش و مذاکره",
                    callback_data="sales_negotiation",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
def economy_keyboard():
    custom = get_attr(
        economy,
        "economy_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📚 مبانی علم اقتصاد",
                    callback_data="economy_basics",
                )
            ],
            [
                InlineKeyboardButton(
                    "📈 عرضه و تقاضا",
                    callback_data="supply_demand",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔥 تورم و شاخص قیمت‌ها",
                    callback_data="inflation",
                )
            ],
            [
                InlineKeyboardButton(
                    "💱 نرخ ارز",
                    callback_data="exchange_rate",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏦 سیاست پولی",
                    callback_data="monetary_policy",
                )
            ],
            [
                InlineKeyboardButton(
                    "💰 سیاست مالی",
                    callback_data="fiscal_policy",
                )
            ],
            [
                InlineKeyboardButton(
                    "📊 اقتصاد کلان",
                    callback_data="macroeconomics",
                )
            ],
            [
                InlineKeyboardButton(
                    "📉 اقتصاد خرد",
                    callback_data="microeconomics",
                )
            ],
            [
                InlineKeyboardButton(
                    "📈 بازار سرمایه",
                    callback_data="capital_market",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
def banking_keyboard():
    custom = get_attr(
        banking,
        "banking_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📖 مقدمه بانکداری",
                    callback_data="banking_intro",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏦 مبانی بانکداری",
                    callback_data="banking_basics",
                )
            ],
            [
                InlineKeyboardButton(
                    "💰 سپرده‌ها",
                    callback_data="banking_deposits",
                )
            ],
            [
                InlineKeyboardButton(
                    "💳 تسهیلات بانکی",
                    callback_data="banking_facilities",
                )
            ],
            [
                InlineKeyboardButton(
                    "📑 عقود بانکی",
                    callback_data="banking_contracts",
                )
            ],
            [
                InlineKeyboardButton(
                    "⚖️ قوانین بانکی",
                    callback_data="banking_laws",
                )
            ],
            [
                InlineKeyboardButton(
                    "🧾 چک و اسناد بانکی",
                    callback_data="banking_checks",
                )
            ],
            [
                InlineKeyboardButton(
                    "🛡️ مبارزه با پولشویی",
                    callback_data="banking_aml",
                )
            ],
            [
                InlineKeyboardButton(
                    "📊 اعتبار و ریسک",
                    callback_data="banking_credit",
                )
            ],
            [
                InlineKeyboardButton(
                    "💻 بانکداری الکترونیک",
                    callback_data="banking_electronic",
                )
            ],
            [
                InlineKeyboardButton(
                    "📝 آزمون بانکداری",
                    callback_data="banking_quiz",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
# ============================================================
# EXAM MENU
# ============================================================
def exam_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏦 بانکداری",
                    callback_data="banking_quiz",
                )
            ],
            [
                InlineKeyboardButton(
                    "📚 مدیریت",
                    callback_data="management_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "🌍 تجارت بین‌الملل",
                    callback_data="trade_exam",
                )
            ],
            [
                InlineKeyboardButton(
                    "📈 بازاریابی و فروش",
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
                    "🏆 آزمون استخدامی بانک‌ها",
                    callback_data="employment",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
# ============================================================
# EMPLOYMENT MENU
# ============================================================
def employment_keyboard():
    custom = get_attr(
        employment,
        "employment_menu",
    )
    result = safe_call(
        custom,
        None,
    )
    if result:
        return result
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏦 بانک‌های هدف",
                    callback_data="employment_banks",
                )
            ],
            [
                InlineKeyboardButton(
                    "📚 دروس عمومی",
                    callback_data="employment_general",
                )
            ],
            [
                InlineKeyboardButton(
                    "🏦 دروس تخصصی بانکی",
                    callback_data="employment_specialized",
                )
            ],
            [
                InlineKeyboardButton(
                    "🧠 هوش و استعداد",
                    callback_data="employment_iq",
                )
            ],
            [
                InlineKeyboardButton(
                    "🇬🇧 زبان انگلیسی",
                    callback_data="employment_english",
                )
            ],
            [
                InlineKeyboardButton(
                    "💻 فناوری اطلاعات",
                    callback_data="employment_it",
                )
            ],
            [
                InlineKeyboardButton(
                    "🗺️ نقشه راه قبولی",
                    callback_data="employment_roadmap",
                )
            ],
            [
                InlineKeyboardButton(
                    "🎤 آمادگی مصاحبه",
                    callback_data="employment_interview",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home",
                )
            ],
        ]
    )
# ============================================================
# LESSON DATA
# ============================================================
LESSON_MODULES = {
    # Banking
    "banking_intro": banking,
    "banking_basics": banking,
    "banking_deposits": banking,
    "banking_facilities": banking,
    "banking_contracts": banking,
    "banking_laws": banking,
    "banking_checks": banking,
    "banking_aml": banking,
    "banking_credit": banking,
    "banking_electronic": banking,
    "banking_risk": banking,
    "banking_central": banking,
    "banking_islamic": banking,
    # Management
    "management_definition": management,
    "management_functions": management,
    "management_levels": management,
    "management_roles": management,
    "management_skills": management,
    "efficiency_effectiveness": management,
    "management_schools": management,
    # Trade
    "trade_basics": trade,
    "trade_documents": trade,
    "trade_logistics": trade,
    "trade_payment": trade,
    "trade_incoterms": trade,
    "trade_laws": trade,
    # Marketing
    "marketing_basics": marketing,
    "consumer_behavior": marketing,
    "market_research": marketing,
    "marketing_4p": marketing,
    "marketing_stp": marketing,
    "marketing_branding": marketing,
    "sales_negotiation": marketing,
    # Economy
    "economy_basics": economy,
    "supply_demand": economy,
    "inflation": economy,
    "exchange_rate": economy,
    "monetary_policy": economy,
    "fiscal_policy": economy,
    "macroeconomics": economy,
    "microeconomics": economy,
    "capital_market": economy,
}
# ============================================================
# LESSON FUNCTION NAMES
# ============================================================
LESSON_FUNCTIONS = {
    "banking_intro": "banking_intro_text",
    "banking_basics": "banking_basics_text",
    "banking_deposits": "banking_deposits_text",
    "banking_facilities": "banking_facilities_text",
    "banking_contracts": "banking_contracts_text",
    "banking_laws": "banking_laws_text",
    "banking_checks": "banking_checks_text",
    "banking_aml": "banking_aml_text",
    "banking_credit": "banking_credit_text",
    "banking_electronic": "banking_electronic_text",
    "banking_risk": "banking_risk_text",
    "banking_central": "banking_central_text",
    "banking_islamic": "banking_islamic_text",
    "management_definition": "management_definition_text",
    "management_functions": "management_functions_text",
    "management_levels": "management_levels_text",
    "management_roles": "management_roles_text",
    "management_skills": "management_skills_text",
    "efficiency_effectiveness": "efficiency_effectiveness_text",
    "management_schools": "management_schools_text",
    "trade_basics": "trade_basics_text",
    "trade_documents": "trade_documents_text",
    "trade_logistics": "trade_logistics_text",
    "trade_payment": "trade_payment_text",
    "trade_incoterms": "trade_incoterms_text",
    "trade_laws": "trade_laws_text",
    "marketing_basics": "marketing_basics_text",
    "consumer_behavior": "consumer_behavior_text",
    "market_research": "market_research_text",
    "marketing_4p": "marketing_4p_text",
    "marketing_stp": "marketing_stp_text",
    "marketing_branding": "marketing_branding_text",
    "sales_negotiation": "sales_negotiation_text",
    "economy_basics": "economy_basics_text",
    "supply_demand": "supply_demand_text",
    "inflation": "inflation_text",
    "exchange_rate": "exchange_rate_text",
    "monetary_policy": "monetary_policy_text",
    "fiscal_policy": "fiscal_policy_text",
    "macroeconomics": "macroeconomics_text",
    "microeconomics": "microeconomics_text",
    "capital_market": "capital_market_text",
}
# ============================================================
# GET LESSON
# ============================================================
def get_lesson(
    callback_data: str,
):
    module = LESSON_MODULES.get(
        callback_data
    )
    function_name = LESSON_FUNCTIONS.get(
        callback_data
    )
    if module is None:
        return None
    if function_name is None:
        return None
    function = getattr(
        module,
        function_name,
        None,
    )
    if function is None:
        return None
    return safe_call(
        function,
        None,
    )
# ============================================================
# START
# ============================================================
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    user = update.effective_user
    name = (
        user.first_name
        if user and user.first_name
        else "دوست عزیز"
    )
    text = f"""
👋 سلام <b>{name}</b>
🏛️ <b>به اندیشکده مدیریت و بازار خوش آمدید.</b>
━━━━━━━━━━━━━━━━━━
اینجا یک مسیر کامل برای:
📚 آموزش تخصصی
📝 آزمون و تست
🎯 آمادگی استخدامی
📊 ارزیابی عملکرد
🏆 پیشرفت مرحله‌ای
در اختیار شماست.
━━━━━━━━━━━━━━━━━━
👇 از منوی زیر انتخاب کنید:
"""
    await update.message.reply_text(
        text,
        reply_markup=main_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# HOME
# ============================================================
async def home_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        home_text(),
        reply_markup=main_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# MAIN SECTIONS
# ============================================================
async def section_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    data = query.data
    sections = {
        "management": (
            """
📚 <b>آموزش مدیریت</b>
━━━━━━━━━━━━━━━━━━
از مبانی مدیریت تا مفاهیم تخصصی
و آزمون‌های مرتبط.
👇 بخش موردنظر را انتخاب کنید.
""",
            management_keyboard(),
        ),
        "trade": (
            """
🌍 <b>تجارت بین‌الملل</b>
━━━━━━━━━━━━━━━━━━
📑 اسناد تجاری
🚚 لجستیک
💳 پرداخت‌های بین‌المللی
🌐 Incoterms
⚖️ قوانین تجارت
👇 موضوع موردنظر را انتخاب کنید.
""",
            trade_keyboard(),
        ),
        "marketing": (
            """
📈 <b>بازاریابی و فروش</b>
━━━━━━━━━━━━━━━━━━
🎯 استراتژی بازاریابی
🧠 رفتار مشتری
🔎 تحقیقات بازار
🏷️ برندینگ
🤝 فروش و مذاکره
👇 مسیر یادگیری را انتخاب کنید.
""",
            marketing_keyboard(),
        ),
        "economy": (
            """
💰 <b>اقتصاد و بازار</b>
━━━━━━━━━━━━━━━━━━
📚 مبانی اقتصاد
📈 عرضه و تقاضا
🔥 تورم
💱 نرخ ارز
🏦 سیاست پولی
💰 سیاست مالی
📊 اقتصاد کلان
📉 اقتصاد خرد
👇 موضوع موردنظر را انتخاب کنید.
""",
            economy_keyboard(),
        ),
        "banking": (
            """
🏦 <b>مرکز تخصصی بانکداری</b>
━━━━━━━━━━━━━━━━━━
📚 آموزش بانکداری
💳 تسهیلات
💰 سپرده‌ها
⚖️ قوانین بانکی
🛡️ مبارزه با پولشویی
📊 اعتبار و ریسک
💻 بانکداری الکترونیک
📝 آزمون بانکداری
👇 انتخاب کنید.
""",
            banking_keyboard(),
        ),
        "employment": (
            """
🏆 <b>مرکز آمادگی آزمون استخدامی بانک‌ها</b>
━━━━━━━━━━━━━━━━━━
🎯 آمادگی آزمون کتبی
📚 دروس عمومی و تخصصی
🧠 هوش و استعداد
🇬🇧 زبان
💻 فناوری اطلاعات
🎤 آمادگی مصاحبه
👇 مسیر خود را انتخاب کنید.
""",
            employment_keyboard(),
        ),
        "exam": (
            """
🎓 <b>مرکز آزمون و تست</b>
━━━━━━━━━━━━━━━━━━
دانش خود را در حوزه‌های مختلف
بسنجید و نقاط قوت و ضعف خود
را شناسایی کنید.
👇 حوزه آزمون را انتخاب کنید.
""",
            exam_keyboard(),
        ),
    }
    if data not in sections:
        return
    text, keyboard = sections[data]
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# ============================================================
# LESSON CALLBACK
# ============================================================
async def lesson_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    data = query.data
    text = get_lesson(
        data
    )
    if not text:
        text = """
⚠️ <b>محتوای این بخش هنوز آماده نشده است.</b>
این بخش در حال تکمیل است.
🔄 به‌زودی محتوای تخصصی آن
در ربات قرار خواهد گرفت.
"""
    if data.startswith("banking_"):
        keyboard = banking_keyboard()
    elif data.startswith("management_") or data in (
        "efficiency_effectiveness",
    ):
        keyboard = management_keyboard()
    elif data.startswith("trade_"):
        keyboard = trade_keyboard()
    elif data.startswith("marketing_") or data in (
        "consumer_behavior",
        "market_research",
        "sales_negotiation",
    ):
        keyboard = marketing_keyboard()
    elif data in (
        "economy_basics",
        "supply_demand",
        "inflation",
        "exchange_rate",
        "monetary_policy",
        "fiscal_policy",
        "macroeconomics",
        "microeconomics",
        "capital_market",
    ):
        keyboard = economy_keyboard()
    else:
        keyboard = back_home_keyboard()
    await query.edit_message_text(
        str(text),
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# ============================================================
# BANKING QUIZ
# ============================================================
async def banking_quiz_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    quiz_text = get_attr(
        banking,
        "banking_quiz_text",
        None,
    )
    text = safe_call(
        quiz_text,
        None,
    )
    if not text:
        text = """
📝 <b>آزمون تخصصی بانکداری</b>
━━━━━━━━━━━━━━━━━━
این بخش برای سنجش دانش شما
در حوزه بانکداری طراحی شده است.
🎯 در نسخه فعلی، محتوای آزمون
از فایل <b>banking.py</b> دریافت می‌شود.
📚 سوالات و سیستم امتیازدهی
در مرحله بعدی تکمیل می‌شوند.
"""
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔄 شروع آزمون",
                    callback_data="banking_quiz_start",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بانکداری",
                    callback_data="banking",
                )
            ],
        ]
    )
    await query.edit_message_text(
        str(text),
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# ============================================================
# QUIZ START
# ============================================================
async def banking_quiz_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    questions = get_attr(
        banking,
        "BANKING_QUESTIONS",
        [],
    )
    if not questions:
        await query.edit_message_text(
            """
⚠️ <b>سؤال آزمون پیدا نشد.</b>
در فایل <b>banking.py</b>
هنوز مجموعه سوالات آزمون تعریف نشده است.
""",
            reply_markup=banking_keyboard(),
            parse_mode="HTML",
        )
        return
    await query.edit_message_text(
        """
🎯 <b>آزمون بانکداری</b>
━━━━━━━━━━━━━━━━━━
مجموعه سوالات شناسایی شد.
برای فعال‌سازی کامل:
⏱️ زمان‌سنج
📊 امتیاز
📈 درصد
🧠 تحلیل عملکرد
🎯 سطح‌بندی
باید ساختار سوالات موجود در
<b>banking.py</b> را با موتور آزمون
هماهنگ کنیم.
👇 مرحله بعد همین بخش است.
""",
        reply_markup=banking_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# EMPLOYMENT
# ============================================================
async def employment_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
🏆 <b>آزمون استخدامی بانک‌ها</b>
━━━━━━━━━━━━━━━━━━
یک مسیر کامل برای آمادگی آزمون:
🏦 بانک‌های هدف
📚 دروس عمومی
🏦 دروس تخصصی
🧠 هوش و استعداد
🇬🇧 زبان انگلیسی
💻 فناوری اطلاعات
🗺️ نقشه راه مطالعه
🎤 مصاحبه استخدامی
👇 انتخاب کنید.
""",
        reply_markup=employment_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# SOCIAL
# ============================================================
async def social_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    function = get_attr(
        social,
        "social_callback",
        None,
    )
    if function:
        try:
            await function(
                update,
                context,
            )
            return
        except Exception as error:
            logger.warning(
                "Social callback error: %s",
                error,
            )
    await query.edit_message_text(
        """
📱 <b>شبکه‌های اجتماعی</b>
━━━━━━━━━━━━━━━━━━
برای دسترسی به صفحات رسمی
اندیشکده مدیریت و بازار
از لینک‌های رسمی استفاده کنید.
🔗 لینک‌ها در حال تکمیل هستند.
""",
        reply_markup=back_home_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# FILES
# ============================================================
async def files_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        """
📂 <b>فایل و جزوات</b>
━━━━━━━━━━━━━━━━━━
در این بخش می‌توانید به:
📚 جزوات آموزشی
📝 نمونه سوالات
📊 منابع آزمون
📑 فایل‌های تخصصی
دسترسی پیدا کنید.
⚠️ بخش فایل‌ها در حال توسعه است.
""",
        reply_markup=back_home_keyboard(),
        parse_mode="HTML",
    )
# ============================================================
# UNKNOWN CALLBACK
# ============================================================
async def unknown_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    await query.answer(
        "این بخش هنوز فعال نشده است.",
        show_alert=False,
    )
# ============================================================
# ERROR HANDLER
# ============================================================
async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):
    logger.error(
        "Unhandled exception:",
        exc_info=context.error,
    )
# ============================================================
# APPLICATION
# ============================================================
def build_application():
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )
    # --------------------------------------------------------
    # COMMAND
    # --------------------------------------------------------
    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )
    # --------------------------------------------------------
    # HOME
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            home_callback,
            pattern=r"^home$",
        )
    )
    # --------------------------------------------------------
    # MAIN SECTIONS
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            section_callback,
            pattern=(
                r"^(management|trade|marketing|"
                r"economy|banking|employment|exam)$"
            ),
        )
    )
    # --------------------------------------------------------
    # LESSONS
    # --------------------------------------------------------
    lesson_pattern = (
        r"^(banking_intro|"
        r"banking_basics|"
        r"banking_deposits|"
        r"banking_facilities|"
        r"banking_contracts|"
        r"banking_laws|"
        r"banking_checks|"
        r"banking_aml|"
        r"banking_credit|"
        r"banking_electronic|"
        r"banking_risk|"
        r"banking_central|"
        r"banking_islamic|"
        r"management_definition|"
        r"management_functions|"
        r"management_levels|"
        r"management_roles|"
        r"management_skills|"
        r"management_schools|"
        r"efficiency_effectiveness|"
        r"trade_basics|"
        r"trade_documents|"
        r"trade_logistics|"
        r"trade_payment|"
        r"trade_incoterms|"
        r"trade_laws|"
        r"marketing_basics|"
        r"consumer_behavior|"
        r"market_research|"
        r"marketing_4p|"
        r"marketing_stp|"
        r"marketing_branding|"
        r"sales_negotiation|"
        r"economy_basics|"
        r"supply_demand|"
        r"inflation|"
        r"exchange_rate|"
        r"monetary_policy|"
        r"fiscal_policy|"
        r"macroeconomics|"
        r"microeconomics|"
        r"capital_market)$"
    )
    application.add_handler(
        CallbackQueryHandler(
            lesson_callback,
            pattern=lesson_pattern,
        )
    )
    # --------------------------------------------------------
    # BANKING QUIZ
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_callback,
            pattern=r"^banking_quiz$",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            banking_quiz_start,
            pattern=r"^banking_quiz_start$",
        )
    )
    # --------------------------------------------------------
    # SOCIAL
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            social_callback,
            pattern=r"^social$",
        )
    )
    # --------------------------------------------------------
    # FILES
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            files_callback,
            pattern=r"^files$",
        )
    )
    # --------------------------------------------------------
    # EMPLOYMENT
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            employment_callback,
            pattern=r"^employment$",
        )
    )
    # --------------------------------------------------------
    # UNKNOWN
    # --------------------------------------------------------
    application.add_handler(
        CallbackQueryHandler(
            unknown_callback,
        )
    )
    # --------------------------------------------------------
    # ERRORS
    # --------------------------------------------------------
    application.add_error_handler(
        error_handler
    )
    return application
# ============================================================
# MAIN
# ============================================================
def main():
    logger.info(
        "🏛️ Andishkadeh Market Bot is starting..."
    )
    application = build_application()
    logger.info(
        "✅ Application created successfully."
    )
    logger.info(
        "🚀 Bot is running."
    )
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )
# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()
