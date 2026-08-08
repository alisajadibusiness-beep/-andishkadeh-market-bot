import os
from threading import Thread

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from menus import main_menu, trade_menu


TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

app = Flask(__name__)


@app.route("/")
def home():
    return "Andishkadeh Market Bot is running."


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


# =========================
# HELP
# =========================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات\n\n"
        "برای مشاهده منوی اصلی، /start را ارسال کنید."
    )


# =========================
# MENUS
# =========================

def management_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🧠 مبانی مدیریت",
                callback_data="management_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 رفتار سازمانی",
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
                "💼 مدیریت منابع انسانی",
                callback_data="human_resources"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 مدیریت مالی",
                callback_data="financial_management"
            )
        ],
        [
            InlineKeyboardButton(
                "📖 منابع و کتاب‌ها",
                callback_data="management_books"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون مدیریت",
                callback_data="management_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def marketing_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📣 مبانی بازاریابی",
                callback_data="marketing_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 بازاریابی دیجیتال",
                callback_data="digital_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 فروش و مذاکره",
                callback_data="sales_negotiation"
            )
        ],
        [
            InlineKeyboardButton(
                "👤 رفتار مصرف‌کننده",
                callback_data="consumer_behavior"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 شبکه‌های اجتماعی",
                callback_data="social_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 تحقیقات بازار",
                callback_data="market_research"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون بازاریابی",
                callback_data="marketing_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def economy_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 مبانی اقتصاد",
                callback_data="economy_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 اقتصاد کلان",
                callback_data="macro_economics"
            )
        ],
        [
            InlineKeyboardButton(
                "📉 اقتصاد خرد",
                callback_data="micro_economics"
            )
        ],
        [
            InlineKeyboardButton(
                "💵 تورم و نقدینگی",
                callback_data="inflation_liquidity"
            )
        ],
        [
            InlineKeyboardButton(
                "💱 ارز و بازار ارز",
                callback_data="foreign_exchange"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 بازارهای مالی",
                callback_data="financial_markets"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون اقتصاد",
                callback_data="economy_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def banking_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 مبانی بانکداری",
                callback_data="banking_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "⚖️ قوانین و مقررات بانکی",
                callback_data="banking_laws"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 خدمات بانکی",
                callback_data="banking_services"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 تسهیلات و اعتبارات",
                callback_data="loans_credits"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 مبارزه با پولشویی",
                callback_data="aml"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 مدیریت بانک",
                callback_data="bank_management"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون بانکداری",
                callback_data="banking_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def exam_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 آزمون مدیریت",
                callback_data="exam_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 آزمون تجارت بین‌الملل",
                callback_data="exam_trade"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 آزمون بازاریابی",
                callback_data="exam_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 آزمون اقتصاد",
                callback_data="exam_economy"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 آزمون بانکداری",
                callback_data="exam_banking"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 هوش و استعداد",
                callback_data="exam_iq"
            )
        ],
        [
            InlineKeyboardButton(
                "🇬🇧 زبان انگلیسی",
                callback_data="exam_english"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def files_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📕 جزوات مدیریت",
                callback_data="files_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 جزوات تجارت بین‌الملل",
                callback_data="files_trade"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 جزوات بازاریابی",
                callback_data="files_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 جزوات اقتصاد",
                callback_data="files_economy"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 جزوات بانکداری",
                callback_data="files_banking"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 منابع آزمون",
                callback_data="files_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def social_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📸 اینستاگرام",
                callback_data="instagram"
            )
        ],
        [
            InlineKeyboardButton(
                "▶️ یوتیوب",
                callback_data="youtube"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 واتساپ",
                callback_data="whatsapp"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 کانال تلگرام",
                callback_data="telegram_channel"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 وب‌سایت",
                callback_data="website"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# BUTTON HANDLER
# =========================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # -------------------------
    # تجارت بین‌الملل
    # -------------------------

    if query.data == "trade":
        await query.edit_message_text(
            "🌍 تجارت بین‌الملل\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=trade_menu()
        )
        return

    # -------------------------
    # مدیریت
    # -------------------------

    if query.data == "management":
        await query.edit_message_text(
            "📚 آموزش مدیریت\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=management_menu()
        )
        return

    # -------------------------
    # بازاریابی
    # -------------------------

    if query.data == "marketing":
        await query.edit_message_text(
            "📈 بازاریابی و فروش\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=marketing_menu()
        )
        return

    # -------------------------
    # اقتصاد
    # -------------------------

    if query.data == "economy":
        await query.edit_message_text(
            "💰 اقتصاد و بازار\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=economy_menu()
        )
        return

    # -------------------------
    # بانکداری
    # -------------------------

    if query.data == "banking":
        await query.edit_message_text(
            "🏦 بانکداری\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=banking_menu()
        )
        return

    # -------------------------
    # آزمون
    # -------------------------

    if query.data == "exam":
        await query.edit_message_text(
            "🎓 آزمون و تست\n\n"
            "موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=exam_menu()
        )
        return

    # -------------------------
    # فایل‌ها
    # -------------------------

    if query.data == "files":
        await query.edit_message_text(
            "📂 فایل و جزوات\n\n"
            "دسته‌بندی فایل موردنظر را انتخاب کنید:",
            reply_markup=files_menu()
        )
        return

    # -------------------------
    # شبکه‌های اجتماعی
    # -------------------------

    if query.data == "social":
        await query.edit_message_text(
            "📱 شبکه‌های اجتماعی\n\n"
            "شبکه اجتماعی موردنظر را انتخاب کنید:",
            reply_markup=social_menu()
        )
        return

    # -------------------------
    # اسناد تجاری
    # -------------------------

    if query.data == "trade_documents":
        keyboard = [
            [
                InlineKeyboardButton(
                    "📄 پروفرما اینویس",
                    callback_data="proforma_invoice"
                )
            ],
            [
                InlineKeyboardButton(
                    "🧾 فاکتور تجاری",
                    callback_data="commercial_invoice"
                )
            ],
            [
                InlineKeyboardButton(
                    "📦 پکینگ لیست",
                    callback_data="packing_list"
                )
            ],
            [
                InlineKeyboardButton(
                    "🚢 بارنامه",
                    callback_data="bill_of_lading"
                )
            ],
            [
                InlineKeyboardButton(
                    "🛃 گواهی مبدأ",
                    callback_data="certificate_origin"
                )
            ],
            [
                InlineKeyboardButton(
                    "📜 قرارداد فروش بین‌المللی",
                    callback_data="international_contract"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚖️ نکات حقوقی قراردادها",
                    callback_data="contract_legal"
                )
            ],
            [
                InlineKeyboardButton(
                    "📝 آزمون اسناد تجاری",
                    callback_data="documents_exam"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت به تجارت بین‌الملل",
                    callback_data="trade"
                )
            ],
        ]

        await query.edit_message_text(
            "📑 اسناد و قراردادهای تجاری\n\n"
            "سند یا موضوع موردنظر خود را انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # -------------------------
    # محتوای آموزشی
    # -------------------------

    contents = {

        "management_basics":
            "🧠 مبانی مدیریت\n\n"
            "مدیریت فرآیند برنامه‌ریزی، سازماندهی، هدایت و کنترل منابع "
            "برای رسیدن به اهداف سازمان است.",

        "organizational_behavior":
            "👥 رفتار سازمانی\n\n"
            "بررسی رفتار افراد و گروه‌ها در سازمان و تأثیر آن بر عملکرد "
            "و بهره‌وری.",

        "strategic_management":
            "🎯 مدیریت استراتژیک\n\n"
            "فرآیند تعیین اهداف بلندمدت سازمان و انتخاب راهبردهای مناسب "
            "برای دستیابی به آنها.",

        "human_resources":
            "💼 مدیریت منابع انسانی\n\n"
            "شامل جذب، آموزش، ارزیابی، توسعه و نگهداشت کارکنان سازمان.",

        "financial_management":
            "📊 مدیریت مالی\n\n"
            "مدیریت منابع مالی، تصمیم‌گیری درباره سرمایه‌گذاری، تأمین مالی "
            "و کنترل منابع مالی سازمان.",

        "management_books":
            "📖 منابع و کتاب‌های مدیریت\n\n"
            "در این بخش منابع و کتاب‌های منتخب مدیریت معرفی خواهند شد.",

        "management_exam":
            "📝 آزمون مدیریت\n\n"
            "آزمون‌های چهارگزینه‌ای مدیریت در این بخش قرار خواهند گرفت.",

        "marketing_basics":
            "📣 مبانی بازاریابی\n\n"
            "بازاریابی فرآیند شناسایی نیاز مشتری، ایجاد ارزش و ارائه آن "
            "به بازار است.",

        "digital_marketing":
            "🎯 بازاریابی دیجیتال\n\n"
            "آشنایی با بازاریابی در فضای دیجیتال، محتوا، موتورهای جستجو "
            "و شبکه‌های اجتماعی.",

        "sales_negotiation":
            "💬 فروش و مذاکره\n\n"
            "اصول مذاکره، شناخت مشتری، ارائه ارزش و تکنیک‌های فروش.",

        "consumer_behavior":
            "👤 رفتار مصرف‌کننده\n\n"
            "بررسی عوامل مؤثر بر تصمیم خرید و رفتار مشتریان.",

        "social_marketing":
            "📱 بازاریابی شبکه‌های اجتماعی\n\n"
            "استراتژی تولید محتوا، جذب مخاطب و تبدیل مخاطب به مشتری.",

        "market_research":
            "📊 تحقیقات بازار\n\n"
            "جمع‌آوری و تحلیل اطلاعات بازار برای تصمیم‌گیری بهتر کسب‌وکار.",

        "marketing_exam":
            "📝 آزمون بازاریابی\n\n"
            "سوالات آموزشی بازاریابی و فروش در این بخش قرار می‌گیرند.",

        "economy_basics":
            "📚 مبانی اقتصاد\n\n"
            "آشنایی با مفاهیم پایه عرضه، تقاضا، قیمت، بازار و منابع محدود.",

        "macro_economics":
            "📈 اقتصاد کلان\n\n"
            "بررسی تورم، بیکاری، رشد اقتصادی، تولید ناخالص داخلی و سیاست‌های اقتصادی.",

        "micro_economics":
            "📉 اقتصاد خرد\n\n"
            "بررسی رفتار مصرف‌کننده، تولیدکننده، بازار و قیمت‌گذاری.",

        "inflation_liquidity":
            "💵 تورم و نقدینگی\n\n"
            "بررسی مفهوم تورم، نقدینگی و عوامل مؤثر بر تغییر سطح عمومی قیمت‌ها.",

        "foreign_exchange":
            "💱 ارز و بازار ارز\n\n"
            "آشنایی با نرخ ارز، بازار ارز و عوامل مؤثر بر ارزش پول‌ها.",

        "financial_markets":
            "📊 بازارهای مالی\n\n"
            "آشنایی با بازار سرمایه، بازار پول و ابزارهای مالی.",

        "economy_exam":
            "📝 آزمون اقتصاد\n\n"
            "سوالات چهارگزینه‌ای اقتصاد در این بخش قرار خواهند گرفت.",

        "banking_basics":
            "🏦 مبانی بانکداری\n\n"
            "آشنایی با مفهوم بانک، انواع بانک‌ها، سپرده‌ها و خدمات بانکی.",

        "banking_laws":
            "⚖️ قوانین و مقررات بانکی\n\n"
            "آشنایی آموزشی با قوانین و مقررات مرتبط با نظام بانکی.",

        "banking_services":
            "💳 خدمات بانکی\n\n"
            "آشنایی با انواع خدمات بانکی، حساب‌ها، کارت‌ها و خدمات الکترونیکی.",

        "loans_credits":
            "💰 تسهیلات و اعتبارات\n\n"
            "آشنایی با انواع تسهیلات، اعتبارسنجی و مفاهیم اعتباری.",

        "aml":
            "🔐 مبارزه با پولشویی\n\n"
            "آشنایی با مفاهیم پایه مبارزه با پولشویی و شناخت مشتری.",

        "bank_management":
            "📊 مدیریت بانک\n\n"
            "آشنایی با مدیریت منابع، مصارف، ریسک و عملکرد بانک.",

        "banking_exam":
            "📝 آزمون بانکداری\n\n"
            "سوالات آموزشی بانکداری و قوانین بانکی در این بخش قرار می‌گیرند.",

        "exam_management":
            "📚 آزمون مدیریت\n\n"
            "بخش سوالات مدیریت.",

        "exam_trade":
            "🌍 آزمون تجارت بین‌الملل\n\n"
            "بخش سوالات تجارت بین‌الملل.",

        "exam_marketing":
            "📈 آزمون بازاریابی\n\n"
            "بخش سوالات بازاریابی و فروش.",

        "exam_economy":
            "💰 آزمون اقتصاد\n\n"
            "بخش سوالات اقتصاد.",

        "exam_banking":
            "🏦 آزمون بانکداری\n\n"
            "بخش سوالات بانکداری و قوانین بانکی.",

        "exam_iq":
            "🧠 هوش و استعداد\n\n"
            "تمرین‌ها و سوالات هوش و استعداد در این بخش قرار می‌گیرند.",

        "exam_english":
            "🇬🇧 زبان انگلیسی\n\n"
            "تمرین‌های زبان انگلیسی عمومی و تخصصی.",

        "files_management":
            "📕 جزوات مدیریت\n\n"
            "فایل‌های آموزشی مدیریت در این بخش قرار می‌گیرند.",

        "files_trade":
            "🌍 جزوات تجارت بین‌الملل\n\n"
            "فایل‌های آموزشی تجارت بین‌الملل در این بخش قرار می‌گیرند.",

        "files_marketing":
            "📈 جزوات بازاریابی\n\n"
            "فایل‌های آموزشی بازاریابی و فروش در این بخش قرار می‌گیرند.",

        "files_economy":
            "💰 جزوات اقتصاد\n\n"
            "فایل‌های آموزشی اقتصاد در این بخش قرار می‌گیرند.",

        "files_banking":
            "🏦 جزوات بانکداری\n\n"
            "فایل‌های آموزشی بانکداری در این بخش قرار می‌گیرند.",

        "files_exam":
            "📝 منابع آزمون\n\n"
            "منابع و فایل‌های آمادگی آزمون در این بخش قرار می‌گیرند.",

        "instagram":
            "📸 اینستاگرام\n\n"
            "صفحه رسمی اندیشکده مدیریت و بازار.",

        "youtube":
            "▶️ یوتیوب\n\n"
            "کانال یوتیوب اندیشکده مدیریت و بازار.",

        "whatsapp":
            "💬 واتساپ\n\n"
            "ارتباط با اندیشکده مدیریت و بازار از طریق واتساپ.",

        "telegram_channel":
            "📢 کانال تلگرام\n\n"
            "کانال رسمی اندیشکده مدیریت و بازار.",

        "website":
            "🌐 وب‌سایت\n\n"
            "وب‌سایت اندیشکده مدیریت و بازار.",

        "proforma_invoice":
            "📄 پروفرما اینویس\n\n"
            "پروفرما اینویس یا پیش‌فاکتور، سندی است که فروشنده "
            "قبل از انجام معامله برای خریدار صادر می‌کند.\n\n"
            "📌 معمولاً شامل:\n"
            "• مشخصات فروشنده و خریدار\n"
            "• شرح کالا\n"
            "• مقدار و قیمت\n"
            "• شرایط پرداخت\n"
            "• شرایط تحویل\n"
            "• اعتبار پیش‌فاکتور",

        "commercial_invoice":
            "🧾 فاکتور تجاری\n\n"
            "فاکتور تجاری سند اصلی معامله است که اطلاعات فروش کالا "
            "و مبلغ معامله را مشخص می‌کند.",

        "packing_list":
            "📦 پکینگ لیست\n\n"
            "Packing List اطلاعات مربوط به بسته‌بندی و محتویات محموله "
            "را مشخص می‌کند.",

        "bill_of_lading":
            "🚢 بارنامه\n\n"
            "بارنامه سند حمل کالا است و اطلاعات مربوط به فرستنده، "
            "گیرنده، کالا و حمل‌کننده را مشخص می‌کند.",

        "certificate_origin":
            "🛃 گواهی مبدأ\n\n"
            "گواهی مبدأ سندی است که کشور یا محل تولید کالا را مشخص می‌کند.",

        "international_contract":
            "📜 قرارداد فروش بین‌المللی\n\n"
            "قرارداد فروش بین‌المللی توافق میان طرفین معامله درباره "
            "شرایط خرید و فروش کالا یا خدمات در سطح بین‌المللی است.",

        "contract_legal":
            "⚖️ نکات حقوقی قراردادها\n\n"
            "در قراردادهای بین‌المللی باید موضوعاتی مانند قانون حاکم، "
            "شرایط پرداخت، تحویل، مسئولیت طرفین و روش حل اختلاف "
            "به‌صورت دقیق مشخص شود.",

        "documents_exam":
            "📝 آزمون اسناد تجاری\n\n"
            "سوالات و آزمون‌های اسناد تجاری در این بخش قرار می‌گیرند.",
    }

    text = contents.get(
        query.data,
        "گزینه موردنظر پیدا نشد."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ]
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# HOME BUTTON
# =========================

async def home_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = """
🎓 اندیشکده مدیریت و بازار

👇 از منوی زیر یک بخش را انتخاب کنید:
"""

    await query.edit_message_text(
        text,
        reply_markup=main_menu()
    )


# =========================
# FLASK
# =========================

def run_flask():
    app.run(
        host="0.0.0.0",
        port=PORT
    )


# =========================
# MAIN
# =========================

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است.")

    Thread(
        target=run_flask,
        daemon=True
    ).start()

    telegram_app = Application.builder().token(TOKEN).build()

    telegram_app.add_handler(
        CommandHandler("start", start)
    )

    telegram_app.add_handler(
        CommandHandler("help", help_command)
    )

    telegram_app.add_handler(
        CallbackQueryHandler(
            home_button,
            pattern="^home$"
        )
    )

    telegram_app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    telegram_app.run_polling()


if __name__ == "__main__":
    main()
