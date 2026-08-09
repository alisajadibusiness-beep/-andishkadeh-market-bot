# ============================================================
# 🏦 بانک‌یار | ربات حرفه‌ای آمادگی آزمون‌های استخدامی بانک‌ها
# ============================================================
#
# امکانات:
# ✅ آموزش دروس
# ✅ آزمون موضوعی
# ✅ آزمون تصادفی
# ✅ آزمون زمان‌دار
# ✅ امتیاز و درصد
# ✅ پاسخ تشریحی
# ✅ سطح‌بندی کاربر
# ✅ تحلیل عملکرد
# ✅ نمایش نقاط قوت و ضعف
# ✅ ذخیره آمار کاربران در حافظه
# ✅ Flask Health Check برای Render
#
# Python 3.10+
# python-telegram-bot 20+
# Flask
# ============================================================

import os
import random
import threading
import time
from datetime import datetime

from flask import Flask

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
# تنظیمات
# ============================================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN تنظیم نشده است. "
        "در Render از بخش Environment Variables آن را اضافه کنید."
    )


# ============================================================
# Flask برای Render
# ============================================================

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "🏦 Bank Exam Bot is running!", 200


@web_app.route("/health")
def health():
    return "OK", 200


def run_web_server():
    port = int(os.environ.get("PORT", 10000))

    web_app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False,
    )


# ============================================================
# اطلاعات کاربران
# ============================================================

USERS = {}


def get_user(user_id):
    if user_id not in USERS:
        USERS[user_id] = {
            "name": "",
            "tests": 0,
            "questions": 0,
            "correct": 0,
            "wrong": 0,
            "score": 0,
            "subject_stats": {},
            "level": "🌱 تازه‌کار",
        }

    return USERS[user_id]


def calculate_level(user):
    score = user["score"]

    if score >= 5000:
        return "👑 استاد بانکداری"
    elif score >= 3000:
        return "💎 حرفه‌ای"
    elif score >= 1500:
        return "🥇 پیشرفته"
    elif score >= 700:
        return "🥈 متوسط"
    elif score >= 200:
        return "🥉 مبتدی"
    else:
        return "🌱 تازه‌کار"


def update_level(user):
    user["level"] = calculate_level(user)


# ============================================================
# بانک سوالات
# ============================================================

QUESTION_BANK = {

    "banking": [
        {
            "q": "کدام مورد یکی از وظایف اصلی بانک‌هاست؟",
            "options": [
                "واسطه‌گری مالی",
                "تولید کالا",
                "تولید مواد غذایی",
                "ساخت جاده"
            ],
            "answer": 0,
            "explanation": "بانک‌ها از مهم‌ترین نهادهای واسطه‌گر مالی هستند و منابع مالی را میان سپرده‌گذاران و متقاضیان منابع هدایت می‌کنند."
        },
        {
            "q": "کدام مورد از انواع سپرده‌های بانکی است؟",
            "options": [
                "سپرده قرض‌الحسنه",
                "سپرده صنعتی",
                "سپرده تولیدی",
                "سپرده تجاری"
            ],
            "answer": 0,
            "explanation": "سپرده‌های قرض‌الحسنه از انواع مهم سپرده‌های بانکی هستند."
        },
        {
            "q": "هدف اعتبارسنجی مشتری چیست؟",
            "options": [
                "بررسی توان بازپرداخت و ریسک مشتری",
                "افزایش تبلیغات بانک",
                "کاهش تعداد کارکنان",
                "تعیین رنگ کارت بانکی"
            ],
            "answer": 0,
            "explanation": "اعتبارسنجی برای ارزیابی وضعیت اعتباری و ریسک مشتری انجام می‌شود."
        },
        {
            "q": "کدام گزینه به بانکداری الکترونیک مربوط است؟",
            "options": [
                "خدمات غیرحضوری بانکی",
                "تولید خودرو",
                "تولید سیمان",
                "کشاورزی"
            ],
            "answer": 0,
            "explanation": "ارائه خدمات بانکی از طریق کانال‌های الکترونیکی مانند اینترنت‌بانک و همراه‌بانک از مصادیق بانکداری الکترونیک است."
        },
        {
            "q": "کدام مورد معمولاً جزء منابع بانک محسوب می‌شود؟",
            "options": [
                "سپرده مشتریان",
                "میز و صندلی",
                "ساختمان اداری به عنوان بدهی",
                "تبلیغات"
            ],
            "answer": 0,
            "explanation": "سپرده‌های مشتریان از منابع مهم بانک محسوب می‌شوند."
        },
    ],

    "laws": [
        {
            "q": "قانون عملیات بانکی بدون ربا با چه موضوعی ارتباط مستقیم دارد؟",
            "options": [
                "فعالیت‌های بانکی و عقود اسلامی",
                "قوانین راهنمایی و رانندگی",
                "قوانین ساختمان",
                "قوانین کشاورزی"
            ],
            "answer": 0,
            "explanation": "این قانون چارچوب عملیات بانکی در نظام بانکی بدون ربا را تعیین می‌کند."
        },
        {
            "q": "هدف اصلی قوانین مبارزه با پولشویی چیست؟",
            "options": [
                "جلوگیری از ورود درآمدهای نامشروع به چرخه اقتصادی",
                "افزایش تبلیغات",
                "افزایش فروش کالا",
                "توسعه گردشگری"
            ],
            "answer": 0,
            "explanation": "مبارزه با پولشویی برای شناسایی و جلوگیری از استفاده از نظام مالی برای تطهیر درآمدهای نامشروع انجام می‌شود."
        },
        {
            "q": "کدام مورد از موضوعات مهم مقررات بانکی است؟",
            "options": [
                "حقوق و تعهدات بانک و مشتری",
                "طراحی خودرو",
                "تولید پوشاک",
                "کشاورزی"
            ],
            "answer": 0,
            "explanation": "حقوق و تعهدات بانک و مشتری از موضوعات مهم مقررات بانکی است."
        },
        {
            "q": "مقررات مربوط به چک در کدام حوزه قرار می‌گیرد؟",
            "options": [
                "قوانین و مقررات بانکی",
                "بازاریابی",
                "مدیریت منابع انسانی",
                "اقتصاد خرد"
            ],
            "answer": 0,
            "explanation": "چک یکی از اسناد مهم تجاری و بانکی است و مقررات خاص خود را دارد."
        },
        {
            "q": "کدام مورد از اهداف مقررات بانکی است؟",
            "options": [
                "افزایش سلامت و شفافیت نظام مالی",
                "افزایش مصرف سوخت",
                "توسعه کشاورزی",
                "افزایش تولید خودرو"
            ],
            "answer": 0,
            "explanation": "مقررات بانکی با هدف حفظ سلامت، شفافیت و ثبات نظام مالی وضع می‌شوند."
        },
    ],

    "economy": [
        {
            "q": "کمیابی در علم اقتصاد به چه معناست؟",
            "options": [
                "محدود بودن منابع نسبت به نیازها",
                "نامحدود بودن منابع",
                "رایگان بودن همه کالاها",
                "نبود نیاز انسانی"
            ],
            "answer": 0,
            "explanation": "منابع محدود هستند و نیازهای انسان گسترده‌اند؛ بنابراین انتخاب و هزینه فرصت شکل می‌گیرد."
        },
        {
            "q": "هزینه فرصت چیست؟",
            "options": [
                "ارزش بهترین گزینه از دست‌رفته",
                "کل هزینه تولید",
                "هزینه حمل‌ونقل",
                "قیمت فروش"
            ],
            "answer": 0,
            "explanation": "هزینه فرصت ارزش بهترین گزینه‌ای است که به دلیل انتخاب گزینه دیگر از آن صرف‌نظر کرده‌ایم."
        },
        {
            "q": "در شرایط معمول، افزایش قیمت کالا چه اثری بر مقدار تقاضا دارد؟",
            "options": [
                "کاهش می‌یابد",
                "افزایش می‌یابد",
                "همیشه ثابت است",
                "صفر می‌شود"
            ],
            "answer": 0,
            "explanation": "طبق قانون تقاضا، در شرایط معمول افزایش قیمت باعث کاهش مقدار تقاضا می‌شود."
        },
        {
            "q": "کدام مورد از موضوعات اقتصاد کلان است؟",
            "options": [
                "تورم",
                "تصمیم یک مصرف‌کننده",
                "هزینه یک فروشگاه",
                "قیمت یک محصول خاص"
            ],
            "answer": 0,
            "explanation": "تورم یکی از متغیرهای مهم اقتصاد کلان است."
        },
        {
            "q": "کدام مورد ابزار سیاست مالی است؟",
            "options": [
                "مالیات",
                "نرخ ارز بازار",
                "تبلیغات",
                "بسته‌بندی"
            ],
            "answer": 0,
            "explanation": "مالیات و مخارج دولت دو ابزار اصلی سیاست مالی هستند."
        },
    ],

    "management": [
        {
            "q": "کدام گزینه یکی از وظایف اصلی مدیریت است؟",
            "options": [
                "برنامه‌ریزی",
                "تبلیغات",
                "حسابداری",
                "خرید"
            ],
            "answer": 0,
            "explanation": "وظایف کلاسیک مدیریت شامل برنامه‌ریزی، سازماندهی، رهبری و کنترل است."
        },
        {
            "q": "کدام وظیفه مدیریت به تعیین اهداف مربوط است؟",
            "options": [
                "کنترل",
                "رهبری",
                "برنامه‌ریزی",
                "سازماندهی"
            ],
            "answer": 2,
            "explanation": "در برنامه‌ریزی اهداف تعیین و مسیر رسیدن به آنها مشخص می‌شود."
        },
        {
            "q": "مقایسه عملکرد واقعی با اهداف مربوط به کدام وظیفه است؟",
            "options": [
                "برنامه‌ریزی",
                "سازماندهی",
                "رهبری",
                "کنترل"
            ],
            "answer": 3,
            "explanation": "کنترل شامل مقایسه عملکرد واقعی با استانداردها و اصلاح انحرافات است."
        },
        {
            "q": "کدام مهارت در سطوح عالی مدیریت اهمیت بیشتری دارد؟",
            "options": [
                "فنی",
                "ادراکی",
                "عملی",
                "حسابداری"
            ],
            "answer": 1,
            "explanation": "مهارت ادراکی به مدیر کمک می‌کند سازمان را به صورت یک کل و ارتباط میان بخش‌ها درک کند."
        },
        {
            "q": "مدیریت علمی بیشتر با کدام فرد مرتبط است؟",
            "options": [
                "ماکس وبر",
                "هنری فایول",
                "فردریک تیلور",
                "التون مایو"
            ],
            "answer": 2,
            "explanation": "فردریک تیلور از چهره‌های اصلی مدیریت علمی است."
        },
    ],

    "accounting": [
        {
            "q": "معادله اصلی حسابداری کدام است؟",
            "options": [
                "دارایی = بدهی + سرمایه",
                "دارایی = درآمد + هزینه",
                "سرمایه = دارایی + بدهی",
                "بدهی = درآمد + سرمایه"
            ],
            "answer": 0,
            "explanation": "معادله اساسی حسابداری عبارت است از: دارایی = بدهی + سرمایه."
        },
        {
            "q": "کدام مورد دارایی محسوب می‌شود؟",
            "options": [
                "وجه نقد",
                "وام دریافتی",
                "بدهی به فروشنده",
                "سرمایه"
            ],
            "answer": 0,
            "explanation": "وجه نقد یک منبع اقتصادی تحت کنترل واحد تجاری و در نتیجه دارایی است."
        },
        {
            "q": "سود چگونه محاسبه می‌شود؟",
            "options": [
                "درآمد منهای هزینه",
                "هزینه منهای درآمد",
                "دارایی منهای فروش",
                "بدهی منهای سرمایه"
            ],
            "answer": 0,
            "explanation": "در حالت ساده، سود برابر درآمد منهای هزینه است."
        },
        {
            "q": "کدام صورت مالی وضعیت دارایی‌ها و بدهی‌ها را نشان می‌دهد؟",
            "options": [
                "صورت وضعیت مالی",
                "صورت سود و زیان",
                "صورت جریان وجوه نقد",
                "صورت فروش"
            ],
            "answer": 0,
            "explanation": "صورت وضعیت مالی، دارایی‌ها، بدهی‌ها و حقوق مالکانه را در یک تاریخ مشخص نشان می‌دهد."
        },
        {
            "q": "بدهی نشان‌دهنده چیست؟",
            "options": [
                "تعهدات واحد تجاری",
                "دارایی‌های شرکت",
                "درآمد شرکت",
                "فروش شرکت"
            ],
            "answer": 0,
            "explanation": "بدهی بیانگر تعهدات فعلی واحد تجاری است."
        },
    ],

    "finance": [
        {
            "q": "ارزش زمانی پول به چه معناست؟",
            "options": [
                "پول امروز معمولاً ارزشی متفاوت از همان مبلغ در آینده دارد",
                "پول همیشه ارزش ثابتی دارد",
                "پول قابل سرمایه‌گذاری نیست",
                "پول فقط در بانک ارزش دارد"
            ],
            "answer": 0,
            "explanation": "به دلیل عواملی مانند بازده و تورم، یک مبلغ پول در زمان‌های مختلف ارزش اقتصادی متفاوتی دارد."
        },
        {
            "q": "ریسک و بازده معمولاً چه رابطه‌ای دارند؟",
            "options": [
                "با افزایش ریسک مورد انتظار، بازده مورد انتظار نیز می‌تواند افزایش یابد",
                "هیچ ارتباطی ندارند",
                "همیشه هر دو کاهش می‌یابند",
                "ریسک همیشه صفر است"
            ],
            "answer": 0,
            "explanation": "در نظریه مالی، سرمایه‌گذاران معمولاً برای پذیرش ریسک بیشتر بازده مورد انتظار بیشتری مطالبه می‌کنند."
        },
        {
            "q": "ارزش فعلی به چه معناست؟",
            "options": [
                "ارزش امروز جریان‌های نقدی آینده",
                "ارزش تاریخی دارایی",
                "هزینه تولید",
                "قیمت فروش"
            ],
            "answer": 0,
            "explanation": "ارزش فعلی جریان‌های نقدی آینده با استفاده از نرخ تنزیل به ارزش امروز تبدیل می‌شود."
        },
        {
            "q": "کدام مورد یکی از نسبت‌های مالی است؟",
            "options": [
                "نسبت جاری",
                "نسبت تبلیغات",
                "نسبت فروشگاه",
                "نسبت کارکنان"
            ],
            "answer": 0,
            "explanation": "نسبت جاری یکی از نسبت‌های نقدینگی و ابزار تحلیل صورت‌های مالی است."
        },
        {
            "q": "مدیریت مالی بیشتر بر چه موضوعی تمرکز دارد؟",
            "options": [
                "تصمیمات مالی و تخصیص منابع",
                "طراحی لوگو",
                "استخدام معلم",
                "تولید محتوا"
            ],
            "answer": 0,
            "explanation": "مدیریت مالی شامل تصمیمات سرمایه‌گذاری، تأمین مالی و مدیریت منابع مالی است."
        },
    ],

    "marketing": [
        {
            "q": "کدام گزینه یکی از عناصر 4P است؟",
            "options": [
                "Product",
                "Planning",
                "Performance",
                "People"
            ],
            "answer": 0,
            "explanation": "چهار عنصر کلاسیک 4P عبارت‌اند از Product، Price، Place و Promotion."
        },
        {
            "q": "در مدل STP حرف S به چه معناست؟",
            "options": [
                "Sales",
                "Strategy",
                "Segmentation",
                "Service"
            ],
            "answer": 2,
            "explanation": "S در مدل STP مخفف Segmentation یا بخش‌بندی بازار است."
        },
        {
            "q": "کدام مورد بر رفتار مصرف‌کننده اثر دارد؟",
            "options": [
                "عوامل روان‌شناختی",
                "نوع حسابداری شرکت",
                "ظرفیت انبار",
                "ساختار ساختمان"
            ],
            "answer": 0,
            "explanation": "انگیزه، ادراک، یادگیری و نگرش از عوامل روان‌شناختی مؤثر بر رفتار مصرف‌کننده هستند."
        },
        {
            "q": "فروش حرفه‌ای از چه چیزی شروع می‌شود؟",
            "options": [
                "شناخت نیاز مشتری",
                "فشار برای خرید",
                "نادیده گرفتن مشتری",
                "کاهش کیفیت"
            ],
            "answer": 0,
            "explanation": "شناخت نیاز مشتری پایه فروش حرفه‌ای و ارائه راه‌حل مناسب است."
        },
        {
            "q": "هدف اصلی جایگاه‌یابی چیست؟",
            "options": [
                "ایجاد جایگاه مشخص در ذهن مشتری",
                "افزایش تعداد کارکنان",
                "کاهش موجودی",
                "افزایش هزینه"
            ],
            "answer": 0,
            "explanation": "Positioning تلاش شرکت برای ایجاد تصویر و جایگاه مطلوب و متمایز در ذهن بازار هدف است."
        },
    ],

    "trade": [
        {
            "q": "صادرات به چه معناست؟",
            "options": [
                "خرید از خارج",
                "فروش کالا یا خدمات به خارج",
                "تولید داخلی",
                "حمل داخل کشور"
            ],
            "answer": 1,
            "explanation": "صادرات به فروش کالا یا خدمات به یک کشور دیگر گفته می‌شود."
        },
        {
            "q": "کدام سند کشور مبدأ کالا را مشخص می‌کند؟",
            "options": [
                "فاکتور تجاری",
                "بارنامه",
                "گواهی مبدأ",
                "پکینگ لیست"
            ],
            "answer": 2,
            "explanation": "Certificate of Origin یا گواهی مبدأ کشور مبدأ کالا را مشخص می‌کند."
        },
        {
            "q": "کدام قاعده اینکوترمز بیشترین مسئولیت را معمولاً برای فروشنده ایجاد می‌کند؟",
            "options": [
                "EXW",
                "FCA",
                "FOB",
                "DDP"
            ],
            "answer": 3,
            "explanation": "در DDP فروشنده مسئول تحویل کالا با انجام تشریفات و پرداخت حقوق و عوارض واردات طبق شرایط قاعده است."
        },
        {
            "q": "کدام سازمان قواعد اینکوترمز را منتشر می‌کند؟",
            "options": [
                "WTO",
                "ICC",
                "IMF",
                "World Bank"
            ],
            "answer": 1,
            "explanation": "Incoterms توسط اتاق بازرگانی بین‌المللی یا ICC منتشر می‌شود."
        },
        {
            "q": "بارنامه بیشتر با کدام موضوع ارتباط دارد؟",
            "options": [
                "حمل کالا",
                "حقوق کارکنان",
                "تبلیغات",
                "حسابداری"
            ],
            "answer": 0,
            "explanation": "Bill of Lading یا بارنامه سند مرتبط با حمل کالا است."
        },
    ],

    "iq": [
        {
            "q": "عدد بعدی را پیدا کنید: 2، 4، 8، 16، ؟",
            "options": [
                "20",
                "24",
                "32",
                "36"
            ],
            "answer": 2,
            "explanation": "هر عدد دو برابر عدد قبلی است؛ بنابراین عدد بعدی 32 است."
        },
        {
            "q": "عدد بعدی: 3، 6، 12، 24، ؟",
            "options": [
                "30",
                "36",
                "48",
                "60"
            ],
            "answer": 2,
            "explanation": "هر عدد در 2 ضرب شده است؛ پاسخ 48 است."
        },
        {
            "q": "اگر همه بانک‌ها مؤسسه مالی باشند و برخی مؤسسات مالی شرکت باشند، کدام نتیجه قطعی است؟",
            "options": [
                "همه بانک‌ها مؤسسه مالی هستند",
                "همه شرکت‌ها بانک هستند",
                "هیچ بانکی مؤسسه مالی نیست",
                "همه مؤسسات مالی بانک هستند"
            ],
            "answer": 0,
            "explanation": "این گزاره مستقیماً از فرض اول نتیجه می‌شود."
        },
        {
            "q": "عدد بعدی: 1، 4، 9، 16، ؟",
            "options": [
                "20",
                "24",
                "25",
                "30"
            ],
            "answer": 2,
            "explanation": "اعداد مربع کامل هستند: 1²، 2²، 3²، 4²؛ بنابراین عدد بعدی 5² یعنی 25 است."
        },
        {
            "q": "اگر علی از رضا بلندتر باشد و رضا از مهدی بلندتر باشد، چه نتیجه‌ای می‌گیریم؟",
            "options": [
                "علی از مهدی بلندتر است",
                "مهدی از علی بلندتر است",
                "قد آنها برابر است",
                "اطلاعات کافی نیست"
            ],
            "answer": 0,
            "explanation": "رابطه انتقالی نشان می‌دهد علی از مهدی بلندتر است."
        },
    ],

    "english": [
        {
            "q": "Choose the correct word: The bank ___ open at 8 a.m.",
            "options": [
                "open",
                "opens",
                "opening",
                "opened"
            ],
            "answer": 1,
            "explanation": "برای فاعل سوم شخص مفرد در زمان حال ساده از opens استفاده می‌شود."
        },
        {
            "q": "What is the opposite of 'increase'?",
            "options": [
                "rise",
                "grow",
                "decrease",
                "improve"
            ],
            "answer": 2,
            "explanation": "Decrease به معنی کاهش است و متضاد increase محسوب می‌شود."
        },
        {
            "q": "Choose the correct option: She ___ a bank account yesterday.",
            "options": [
                "opens",
                "open",
                "opened",
                "opening"
            ],
            "answer": 2,
            "explanation": "Yesterday نشان‌دهنده گذشته است و شکل گذشته open یعنی opened استفاده می‌شود."
        },
        {
            "q": "The word 'customer' means:",
            "options": [
                "مشتری",
                "مدیر",
                "کارمند",
                "بانک"
            ],
            "answer": 0,
            "explanation": "Customer به معنی مشتری است."
        },
        {
            "q": "Choose the correct preposition: He works ___ a bank.",
            "options": [
                "at",
                "on",
                "from",
                "to"
            ],
            "answer": 0,
            "explanation": "برای محل کار معمولاً از at استفاده می‌کنیم: He works at a bank."
        },
    ],

    "icdl": [
        {
            "q": "کدام نرم‌افزار برای پردازش متن استفاده می‌شود؟",
            "options": [
                "Word",
                "Excel",
                "PowerPoint",
                "Paint"
            ],
            "answer": 0,
            "explanation": "Microsoft Word نرم‌افزار پردازش متن است."
        },
        {
            "q": "Excel بیشتر برای چه کاری استفاده می‌شود؟",
            "options": [
                "صفحه گسترده و محاسبات",
                "ویرایش فیلم",
                "طراحی سه‌بعدی",
                "پخش موسیقی"
            ],
            "answer": 0,
            "explanation": "Excel برای صفحات گسترده، محاسبات، داده‌ها و تحلیل آنها کاربرد دارد."
        },
        {
            "q": "کدام نرم‌افزار برای ارائه استفاده می‌شود؟",
            "options": [
                "PowerPoint",
                "Excel",
                "Notepad",
                "Calculator"
            ],
            "answer": 0,
            "explanation": "PowerPoint نرم‌افزار ارائه و ساخت اسلاید است."
        },
        {
            "q": "کدام مورد یک مرورگر وب است؟",
            "options": [
                "Chrome",
                "Excel",
                "Word",
                "PowerPoint"
            ],
            "answer": 0,
            "explanation": "Google Chrome یک مرورگر وب است."
        },
        {
            "q": "برای کپی کردن فایل معمولاً از کدام میانبر استفاده می‌شود؟",
            "options": [
                "Ctrl+C",
                "Ctrl+V",
                "Ctrl+X",
                "Ctrl+Z"
            ],
            "answer": 0,
            "explanation": "Ctrl+C برای Copy، Ctrl+V برای Paste و Ctrl+X برای Cut استفاده می‌شود."
        },
    ],
}


# ============================================================
# نام دروس
# ============================================================

SUBJECTS = {
    "banking": "🏦 بانکداری",
    "laws": "⚖️ قوانین بانکی",
    "economy": "💰 اقتصاد",
    "management": "📊 مدیریت",
    "accounting": "🧾 حسابداری",
    "finance": "📈 مدیریت مالی",
    "marketing": "📣 بازاریابی و فروش",
    "trade": "🌍 تجارت بین‌الملل",
    "iq": "🧠 هوش و استعداد",
    "english": "🇬🇧 زبان انگلیسی",
    "icdl": "💻 ICDL",
}


# ============================================================
# متن درس‌ها
# ============================================================

LESSONS = {

    "banking": """
🏦 مبانی بانکداری

بانک‌ها از مهم‌ترین واسطه‌های مالی اقتصاد هستند.

📌 مهم‌ترین وظایف بانک‌ها:
• جذب سپرده
• اعطای تسهیلات
• انتقال وجوه
• ارائه خدمات پرداخت
• ارائه خدمات الکترونیکی
• مدیریت و ارزیابی ریسک

💰 سپرده‌ها
سپرده‌ها از مهم‌ترین منابع بانک محسوب می‌شوند و انواع مختلفی دارند.

💳 تسهیلات
بانک‌ها با استفاده از منابع خود و طبق مقررات، به متقاضیان تسهیلات ارائه می‌کنند.

⭐ نکته آزمونی:
بانک = واسطه مالی + ارائه‌دهنده خدمات مالی
""",

    "laws": """
⚖️ قوانین و مقررات بانکی

از مهم‌ترین مباحث آزمون‌های استخدامی بانک‌ها:

📜 قانون عملیات بانکی بدون ربا
📜 قوانین مبارزه با پولشویی
📜 مقررات مرتبط با چک
📜 مقررات بانک مرکزی
📜 حقوق بانک و مشتری
📜 مقررات تسهیلات و تعهدات

🎯 نکته آزمونی:
در مطالعه قوانین بانکی، تعریف اصطلاحات، اهداف قوانین و وظایف نهادهای مرتبط اهمیت زیادی دارد.
""",

    "economy": """
💰 اقتصاد

اقتصاد به بررسی تخصیص منابع محدود برای نیازهای مختلف می‌پردازد.

مباحث مهم:

📊 اقتصاد خرد
• عرضه و تقاضا
• تعادل
• کشش
• هزینه
• تولید
• ساختار بازار

📈 اقتصاد کلان
• تورم
• بیکاری
• رشد اقتصادی
• GDP
• نرخ بهره
• نرخ ارز
• سیاست پولی
• سیاست مالی

⭐ حفظی:
خرد → مصرف‌کننده و بنگاه
کلان → اقتصاد در سطح کلی
""",

    "management": """
📊 مبانی مدیریت

چهار وظیفه کلاسیک مدیریت:

1️⃣ برنامه‌ریزی
2️⃣ سازماندهی
3️⃣ رهبری
4️⃣ کنترل

🎯 مهارت‌های مدیر:
• فنی
• انسانی
• ادراکی

⭐ نکته مهم:
مهارت فنی → سطوح عملیاتی
مهارت انسانی → همه سطوح
مهارت ادراکی → سطوح عالی
""",

    "accounting": """
🧾 حسابداری

معادله اساسی حسابداری:

دارایی = بدهی + سرمایه

📌 دارایی:
منابع اقتصادی واحد تجاری.

📌 بدهی:
تعهدات واحد تجاری.

📌 سرمایه:
حقوق مالکانه صاحب یا صاحبان واحد تجاری.

📊 سود:
درآمد - هزینه

⭐ نکته آزمونی:
معادله حسابداری از مهم‌ترین مباحث پایه است.
""",

    "finance": """
📈 مدیریت مالی

مباحث مهم:

💰 ارزش زمانی پول
📊 ارزش فعلی
📈 ارزش آتی
⚖️ ریسک و بازده
💵 تصمیمات سرمایه‌گذاری
🏦 ساختار سرمایه
📋 نسبت‌های مالی

⭐ نکته:
ارزش زمانی پول یعنی یک مبلغ پول در زمان‌های مختلف ارزش اقتصادی یکسانی ندارد.
""",

    "marketing": """
📣 بازاریابی و فروش

بازاریابی فقط فروش نیست؛ بلکه فرآیند ایجاد و ارائه ارزش برای مشتری است.

4P:

1️⃣ Product → محصول
2️⃣ Price → قیمت
3️⃣ Place → توزیع
4️⃣ Promotion → ترفیع

STP:

S → بخش‌بندی
T → بازار هدف
P → جایگاه‌یابی

⭐ نکته:
فروش حرفه‌ای از شناخت نیاز مشتری شروع می‌شود.
""",

    "trade": """
🌍 تجارت بین‌الملل

مباحث مهم:

📦 صادرات
📦 واردات
📑 اسناد تجاری
🚢 حمل‌ونقل
💵 پرداخت بین‌المللی
🌐 Incoterms

⭐ نکات حفظی:

EXW → حداقل مسئولیت فروشنده

DDP → مسئولیت بیشتر فروشنده

ICC → منتشرکننده Incoterms

WTO → سازمان تجارت جهانی
""",

    "iq": """
🧠 هوش و استعداد

مباحث مهم:

🔢 هوش عددی
🔷 الگوها
🧩 روابط منطقی
📝 هوش کلامی
🎯 استدلال
⚡ سرعت و دقت

⭐ روش مطالعه:
ابتدا الگو را پیدا کن، سپس زمان حل را کاهش بده.
""",

    "english": """
🇬🇧 زبان انگلیسی

مباحث مهم:

📚 Vocabulary
📝 Grammar
⏳ Tenses
🔤 Prepositions
📖 Reading
🧩 Cloze Test
🔄 Synonyms & Antonyms

⭐ برای آزمون استخدامی:
واژگان پرتکرار و گرامر پایه اهمیت زیادی دارند.
""",

    "icdl": """
💻 ICDL

مباحث مهم:

🖥️ Windows
📝 Word
📊 Excel
📽️ PowerPoint
🌐 Internet
📧 Email
💾 File & Folder
🔐 امنیت اطلاعات

⭐ میانبرهای مهم:

Ctrl+C → Copy
Ctrl+V → Paste
Ctrl+X → Cut
Ctrl+Z → Undo
Ctrl+S → Save
""",
}


# ============================================================
# منوی اصلی
# ============================================================

def main_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "📝 آزمون‌ها",
                callback_data="exams"
            ),
            InlineKeyboardButton(
                "📚 آموزش",
                callback_data="lessons"
            )
        ],

        [
            InlineKeyboardButton(
                "📊 عملکرد من",
                callback_data="stats"
            ),
            InlineKeyboardButton(
                "🏆 سطح من",
                callback_data="level"
            )
        ],

        [
            InlineKeyboardButton(
                "🎯 آزمون تصادفی",
                callback_data="random_exam"
            )
        ],

        [
            InlineKeyboardButton(
                "⏱️ آزمون زمان‌دار",
                callback_data="timed_exam"
            )
        ],

        [
            InlineKeyboardButton(
                "💡 راهنما",
                callback_data="help"
            )
        ],

    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# منوی آموزش
# ============================================================

def lessons_menu():

    buttons = []

    for key, name in SUBJECTS.items():

        buttons.append(
            [
                InlineKeyboardButton(
                    name,
                    callback_data=f"lesson_{key}"
                )
            ]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="home"
            )
        ]
    )

    return InlineKeyboardMarkup(buttons)


# ============================================================
# منوی آزمون‌ها
# ============================================================

def exams_menu():

    buttons = []

    for key, name in SUBJECTS.items():

        buttons.append(
            [
                InlineKeyboardButton(
                    f"📝 {name} | آزمون",
                    callback_data=f"exam_{key}"
                )
            ]
        )

    buttons.extend(
        [
            [
                InlineKeyboardButton(
                    "🎲 آزمون تصادفی",
                    callback_data="random_exam"
                )
            ],
            [
                InlineKeyboardButton(
                    "⏱️ آزمون زمان‌دار",
                    callback_data="timed_exam"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 بازگشت",
                    callback_data="home"
                )
            ],
        ]
    )

    return InlineKeyboardMarkup(buttons)


# ============================================================
# شروع آزمون
# ============================================================

def start_exam(
    user_id,
    subject=None,
    random_exam=False,
    timed=False,
):

    user = get_user(user_id)

    if random_exam:

        all_questions = []

        for subject_key, questions in QUESTION_BANK.items():

            for question in questions:

                item = question.copy()
                item["subject"] = subject_key
                all_questions.append(item)

        random.shuffle(all_questions)

        questions = all_questions[:10]

    else:

        questions = []

        for question in QUESTION_BANK[subject]:

            item = question.copy()
            item["subject"] = subject
            questions.append(item)

        random.shuffle(questions)

        questions = questions[:5]

    user["exam"] = {
        "questions": questions,
        "index": 0,
        "correct": 0,
        "wrong": 0,
        "score": 0,
        "timed": timed,
        "started": time.time(),
        "duration": 180 if timed else 0,
    }

    return questions


# ============================================================
# نمایش سؤال
# ============================================================

async def send_question(
    query,
    user_id,
):

    user = get_user(user_id)

    if "exam" not in user:
        await query.edit_message_text(
            "❌ آزمونی فعال نیست.",
            reply_markup=main_menu(),
        )
        return

    exam = user["exam"]

    index = exam["index"]
    questions = exam["questions"]

    if index >= len(questions):

        await finish_exam(query, user_id)
        return

    # بررسی زمان
    if exam["timed"]:

        elapsed = int(time.time() - exam["started"])
        remaining = exam["duration"] - elapsed

        if remaining <= 0:

            await finish_exam(
                query,
                user_id,
                timeout=True,
            )
            return

    question = questions[index]

    keyboard = []

    for i, option in enumerate(question["options"]):

        keyboard.append(
            [
                InlineKeyboardButton(
                    f"{chr(65+i)}) {option}",
                    callback_data=f"answer_{i}",
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "❌ خروج",
                callback_data="cancel_exam"
            )
        ]
    )

    timer_text = ""

    if exam["timed"]:

        elapsed = int(time.time() - exam["started"])
        remaining = max(
            0,
            exam["duration"] - elapsed
        )

        minutes = remaining // 60
        seconds = remaining % 60

        timer_text = (
            f"\n⏱️ زمان باقی‌مانده: "
            f"{minutes:02d}:{seconds:02d}\n"
        )

    text = f"""
📝 آزمون استخدامی بانک‌ها

سؤال {index + 1} از {len(questions)}
{timer_text}

📚 درس:
{SUBJECTS.get(question["subject"], "عمومی")}

❓ {question["q"]}

👇 پاسخ خود را انتخاب کنید:
"""

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# پاسخ به سؤال
# ============================================================

async def answer_question(
    query,
    user_id,
    answer,
):

    user = get_user(user_id)

    if "exam" not in user:

        await query.answer(
            "آزمون فعال نیست.",
            show_alert=True,
        )

        return

    exam = user["exam"]

    index = exam["index"]

    question = exam["questions"][index]

    # بررسی زمان
    if exam["timed"]:

        elapsed = int(time.time() - exam["started"])

        if elapsed >= exam["duration"]:

            await finish_exam(
                query,
                user_id,
                timeout=True,
            )

            return

    correct = question["answer"] == answer

    if correct:

        exam["correct"] += 1
        exam["score"] += 100

        user["correct"] += 1
        user["score"] += 100

        result = "✅ پاسخ صحیح!"

    else:

        exam["wrong"] += 1

        user["wrong"] += 1

        result = "❌ پاسخ اشتباه!"

    user["questions"] += 1

    subject = question["subject"]

    if subject not in user["subject_stats"]:

        user["subject_stats"][subject] = {
            "correct": 0,
            "wrong": 0,
        }

    if correct:

        user["subject_stats"][subject]["correct"] += 1

    else:

        user["subject_stats"][subject]["wrong"] += 1

    update_level(user)

    explanation = question.get(
        "explanation",
        "توضیحی برای این سؤال ثبت نشده است."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "➡️ سؤال بعدی",
                callback_data="next_question"
            )
        ]
    ]

    text = f"""
{result}

━━━━━━━━━━━━━━━━━━

❓ سؤال:
{question["q"]}

✅ پاسخ صحیح:
{question["options"][question["answer"]]}

💡 توضیح:
{explanation}

━━━━━━━━━━━━━━━━━━

📊 امتیاز این آزمون:
{exam["score"]}
"""

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# سؤال بعدی
# ============================================================

async def next_question(
    query,
    user_id,
):

    user = get_user(user_id)

    if "exam" not in user:

        await query.edit_message_text(
            "❌ آزمون فعال نیست.",
            reply_markup=main_menu(),
        )

        return

    exam = user["exam"]

    exam["index"] += 1

    await send_question(
        query,
        user_id,
    )


# ============================================================
# پایان آزمون
# ============================================================

async def finish_exam(
    query,
    user_id,
    timeout=False,
):

    user = get_user(user_id)

    exam = user.get("exam")

    if not exam:

        await query.edit_message_text(
            "❌ آزمون فعال نیست.",
            reply_markup=main_menu(),
        )

        return

    total = len(exam["questions"])

    correct = exam["correct"]

    wrong = exam["wrong"]

    unanswered = max(
        0,
        total - correct - wrong
    )

    percentage = (
        correct / total * 100
        if total
        else 0
    )

    user["tests"] += 1

    update_level(user)

    if percentage >= 90:

        message = "🏆 فوق‌العاده! عملکرد شما عالی است."

    elif percentage >= 70:

        message = "🥇 بسیار خوب! ادامه بده."

    elif percentage >= 50:

        message = "🥈 قابل قبول است؛ با مرور بیشتر بهتر می‌شوی."

    else:

        message = "📚 نیاز به مرور و تمرین بیشتری داری."

    timeout_text = ""

    if timeout:
        timeout_text = "\n⏰ زمان آزمون به پایان رسید."

    text = f"""
🏁 پایان آزمون

{timeout_text}

━━━━━━━━━━━━━━━━━━

📊 نتیجه نهایی

📝 تعداد سؤال: {total}

✅ صحیح: {correct}

❌ غلط: {wrong}

⚪ بدون پاسخ: {unanswered}

🎯 درصد: {percentage:.1f}٪

⭐ امتیاز: {exam["score"]}

🏅 سطح فعلی:
{user["level"]}

━━━━━━━━━━━━━━━━━━

{message}
"""

    # حذف آزمون فعال
    del user["exam"]

    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 آزمون جدید",
                callback_data="exams"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 تحلیل عملکرد",
                callback_data="stats"
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
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# صفحه آمار
# ============================================================

async def show_stats(
    query,
    user_id,
):

    user = get_user(user_id)

    total = user["questions"]

    percentage = (
        user["correct"] / total * 100
        if total
        else 0
    )

    text = f"""
📊 تحلیل عملکرد شما

━━━━━━━━━━━━━━━━━━

📝 تعداد آزمون‌ها:
{user["tests"]}

❓ تعداد سؤالات:
{total}

✅ پاسخ صحیح:
{user["correct"]}

❌ پاسخ غلط:
{user["wrong"]}

🎯 درصد کلی:
{percentage:.1f}٪

⭐ امتیاز:
{user["score"]}

🏅 سطح:
{user["level"]}

━━━━━━━━━━━━━━━━━━
📚 عملکرد دروس
"""

    if not user["subject_stats"]:

        text += "\nهنوز آزمونی انجام نداده‌ای."

    else:

        for subject, stats in user[
            "subject_stats"
        ].items():

            total_subject = (
                stats["correct"]
                + stats["wrong"]
            )

            percent_subject = (
                stats["correct"]
                / total_subject
                * 100
                if total_subject
                else 0
            )

            text += (
                f"\n\n{SUBJECTS[subject]}"
                f"\n✅ {stats['correct']}"
                f" | ❌ {stats['wrong']}"
                f"\n🎯 {percent_subject:.1f}٪"
            )

    keyboard = [
        [
            InlineKeyboardButton(
                "📝 آزمون جدید",
                callback_data="exams"
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
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# سطح کاربر
# ============================================================

async def show_level(
    query,
    user_id,
):

    user = get_user(user_id)

    score = user["score"]

    if score < 200:

        next_level = 200 - score

    elif score < 700:

        next_level = 700 - score

    elif score < 1500:

        next_level = 1500 - score

    elif score < 3000:

        next_level = 3000 - score

    elif score < 5000:

        next_level = 5000 - score

    else:

        next_level = 0

    text = f"""
🏅 سطح کاربری

━━━━━━━━━━━━━━━━━━

سطح فعلی:

{user["level"]}

⭐ امتیاز:
{score}

🎯 تعداد پاسخ صحیح:
{user["correct"]}

📝 تعداد آزمون:
{user["tests"]}

━━━━━━━━━━━━━━━━━━

"""

    if next_level:

        text += (
            f"🔥 برای رسیدن به سطح بعدی "
            f"{next_level} امتیاز دیگر نیاز داری."
        )

    else:

        text += "👑 شما به بالاترین سطح رسیده‌ای!"

    keyboard = [
        [
            InlineKeyboardButton(
                "📝 شروع آزمون",
                callback_data="exams"
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
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# نمایش درس
# ============================================================

async def show_lesson(
    query,
    subject,
):

    text = LESSONS.get(
        subject,
        "❌ درس پیدا نشد."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "📝 آزمون این درس",
                callback_data=f"exam_{subject}"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 آموزش",
                callback_data="lessons"
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
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# ============================================================
# /start
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = get_user(
        update.effective_user.id
    )

    user["name"] = (
        update.effective_user.first_name
        or ""
    )

    text = f"""
🏦 سلام {user["name"]} 👋

به «بانک‌یار» خوش آمدی.

🎯 مرکز تخصصی آمادگی آزمون‌های استخدامی بانک‌ها

اینجا می‌توانی:

📚 درس بخوانی
📝 آزمون بدهی
⏱️ آزمون زمان‌دار انجام دهی
🎲 سؤال تصادفی حل کنی
📊 عملکردت را تحلیل کنی
🏆 سطح خودت را ارتقا بدهی

━━━━━━━━━━━━━━━━━━

🏦 بانکداری
⚖️ قوانین بانکی
💰 اقتصاد
📊 مدیریت
🧾 حسابداری
📈 مدیریت مالی
📣 بازاریابی
🌍 تجارت بین‌الملل
🧠 هوش
🇬🇧 زبان
💻 ICDL
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu(),
    )


# ============================================================
# Callback Handler
# ============================================================

async def callback_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    data = query.data

    # -----------------------------
    # خانه
    # -----------------------------

    if data == "home":

        text = """
🏦 بانک‌یار

🎯 آمادگی حرفه‌ای آزمون‌های استخدامی بانک‌ها

از منوی زیر انتخاب کن:
"""

        await query.edit_message_text(
            text,
            reply_markup=main_menu(),
        )

        return

    # -----------------------------
    # آموزش
    # -----------------------------

    if data == "lessons":

        await query.edit_message_text(
            "📚 آموزش\n\nدرس موردنظر را انتخاب کن:",
            reply_markup=lessons_menu(),
        )

        return

    # -----------------------------
    # نمایش درس
    # -----------------------------

    if data.startswith("lesson_"):

        subject = data.replace(
            "lesson_",
            "",
            1,
        )

        await show_lesson(
            query,
            subject,
        )

        return

    # -----------------------------
    # آزمون‌ها
    # -----------------------------

    if data == "exams":

        await query.edit_message_text(
            "📝 آزمون‌ها\n\nنوع آزمون را انتخاب کن:",
            reply_markup=exams_menu(),
        )

        return

    # -----------------------------
    # آزمون موضوعی
    # -----------------------------

    if data.startswith("exam_"):

        subject = data.replace(
            "exam_",
            "",
            1,
        )

        if subject not in QUESTION_BANK:

            await query.edit_message_text(
                "❌ این درس هنوز آزمون ندارد.",
                reply_markup=exams_menu(),
            )

            return

        start_exam(
            user_id,
            subject=subject,
            random_exam=False,
            timed=False,
        )

        await send_question(
            query,
            user_id,
        )

        return

    # -----------------------------
    # آزمون تصادفی
    # -----------------------------

    if data == "random_exam":

        start_exam(
            user_id,
            random_exam=True,
            timed=False,
        )

        await send_question(
            query,
            user_id,
        )

        return

    # -----------------------------
    # آزمون زمان‌دار
    # -----------------------------

    if data == "timed_exam":

        start_exam(
            user_id,
            random_exam=True,
            timed=True,
        )

        await send_question(
            query,
            user_id,
        )

        return

    # -----------------------------
    # پاسخ
    # -----------------------------

    if data.startswith("answer_"):

        try:

            answer = int(
                data.replace(
                    "answer_",
                    "",
                    1,
                )
            )

        except ValueError:

            return

        await answer_question(
            query,
            user_id,
            answer,
        )

        return

    # -----------------------------
    # سؤال بعدی
    # -----------------------------

    if data == "next_question":

        await next_question(
            query,
            user_id,
        )

        return

    # -----------------------------
    # خروج آزمون
    # -----------------------------

    if data == "cancel_exam":

        user = get_user(user_id)

        if "exam" in user:

            del user["exam"]

        await query.edit_message_text(
            "❌ آزمون لغو شد.",
            reply_markup=main_menu(),
        )

        return

    # -----------------------------
    # آمار
    # -----------------------------

    if data == "stats":

        await show_stats(
            query,
            user_id,
        )

        return

    # -----------------------------
    # سطح
    # -----------------------------

    if data == "level":

        await show_level(
            query,
            user_id,
        )

        return

    # -----------------------------
    # راهنما
    # -----------------------------

    if data == "help":

        text = """
💡 راهنمای بانک‌یار

━━━━━━━━━━━━━━━━━━

📝 آزمون موضوعی
از هر درس آزمون اختصاصی بده.

🎲 آزمون تصادفی
سؤالات از تمام دروس به صورت تصادفی انتخاب می‌شوند.

⏱️ آزمون زمان‌دار
یک آزمون ۱۰ سؤالی با زمان محدود.

📊 عملکرد من
درصد، تعداد پاسخ صحیح، غلط و عملکرد هر درس.

🏆 سطح کاربر
با پاسخ صحیح امتیاز می‌گیری و سطح خود را ارتقا می‌دهی.

💡 پاسخ تشریحی
بعد از هر سؤال، پاسخ صحیح و توضیح آن نمایش داده می‌شود.

━━━━━━━━━━━━━━━━━━

🎯 پیشنهاد:
هر روز حداقل ۲۰ سؤال حل کن.
"""

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
            reply_markup=InlineKeyboardMarkup(
                keyboard
            ),
        )

        return


# ============================================================
# خطاها
# ============================================================

async def error_handler(
    update,
    context,
):

    print(
        "ERROR:",
        context.error,
    )


# ============================================================
# اجرای ربات
# ============================================================

def main():

    # سرور Flask برای Render
    threading.Thread(
        target=run_web_server,
        daemon=True,
    ).start()

    print(
        "🌐 Web server started."
    )

    print(
        "🏦 Bank Exam Bot starting..."
    )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    application.add_handler(
        CallbackQueryHandler(
            callback_handler,
        )
    )

    application.add_error_handler(
        error_handler
    )

    print(
        "✅ Bot is running."
    )

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()
