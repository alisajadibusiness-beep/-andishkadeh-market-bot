# =========================================================
# 🏛️ ANDISHKADEH MANAGEMENT & MARKET BOT
# Central Menu System
# =========================================================
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# =========================================================
# CONSTANTS
# =========================================================
HOME = "home"
SEPARATOR = "━━━━━━━━━━━━━━━━━━"
# =========================================================
# 🏠 MAIN MENU
# =========================================================
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 مدیریت",
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
                callback_data="exams"
            ),
        ],
        [
            InlineKeyboardButton(
                "🎯 آزمون‌های استخدامی",
                callback_data="employment"
            ),
            InlineKeyboardButton(
                "📱 شبکه‌های اجتماعی",
                callback_data="social"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
def main_menu_text():
    return f"""
🏛️ <b>اندیشکده مدیریت و بازار</b>
مرکز تخصصی آموزش، آزمون و آمادگی حرفه‌ای
در حوزه‌های مدیریت، بازرگانی، اقتصاد،
بازاریابی و بانکداری
{SEPARATOR}
🎯 <b>مسیر حرفه‌ای یادگیری</b>
📖 آموزش مفهومی
📝 تست تخصصی
⏱️ آزمون
📊 تحلیل عملکرد
🏆 ارتقای سطح علمی
{SEPARATOR}
📚 <b>حوزه‌های تخصصی</b>
👔 مدیریت و سازمان
🌍 تجارت و بازرگانی بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
🏦 بانکداری
🎯 آزمون‌های استخدامی
{SEPARATOR}
👇 <b>بخش موردنظر خود را انتخاب کنید:</b>
"""
# =========================================================
# 📚 MANAGEMENT
# =========================================================
def management_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 مبانی مدیریت",
                callback_data="management_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون مدیریت",
                callback_data="management_basics_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 🌍 TRADE
# =========================================================
def trade_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📘 مفاهیم پایه تجارت",
                callback_data="trade_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "📑 اسناد و قراردادهای تجاری",
                callback_data="trade_documents"
            )
        ],
        [
            InlineKeyboardButton(
                "🚚 حمل‌ونقل و لجستیک",
                callback_data="trade_logistics"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 روش‌های پرداخت بین‌المللی",
                callback_data="trade_payment"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 اینکوترمز",
                callback_data="trade_incoterms"
            )
        ],
        [
            InlineKeyboardButton(
                "⚖️ قوانین و سازمان‌های تجارت",
                callback_data="trade_laws"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون تجارت بین‌الملل",
                callback_data="trade_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 📈 MARKETING
# =========================================================
def marketing_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 اصول و مفاهیم بازاریابی",
                callback_data="marketing_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 رفتار مصرف‌کننده",
                callback_data="consumer_behavior"
            )
        ],
        [
            InlineKeyboardButton(
                "🔎 تحقیقات بازار",
                callback_data="market_research"
            )
        ],
        [
            InlineKeyboardButton(
                "4️⃣ آمیخته بازاریابی 4P",
                callback_data="marketing_4p"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 STP و بخش‌بندی بازار",
                callback_data="marketing_stp"
            )
        ],
        [
            InlineKeyboardButton(
                "💎 برندینگ",
                callback_data="marketing_branding"
            )
        ],
        [
            InlineKeyboardButton(
                "🤝 فروش و مذاکره",
                callback_data="sales_negotiation"
            )
        ],
        [
            InlineKeyboardButton(
                "🔄 قیف فروش",
                callback_data="sales_funnel"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 بازاریابی دیجیتال",
                callback_data="digital_marketing"
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
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 💰 ECONOMY
# =========================================================
def economy_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📘 مبانی علم اقتصاد",
                callback_data="economy_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "⚖️ عرضه و تقاضا",
                callback_data="supply_demand"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 تورم و شاخص قیمت‌ها",
                callback_data="inflation"
            )
        ],
        [
            InlineKeyboardButton(
                "💱 نرخ ارز",
                callback_data="exchange_rate"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 سیاست پولی",
                callback_data="monetary_policy"
            )
        ],
        [
            InlineKeyboardButton(
                "🏛️ سیاست مالی",
                callback_data="fiscal_policy"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 اقتصاد کلان",
                callback_data="macroeconomics"
            )
        ],
        [
            InlineKeyboardButton(
                "🔬 اقتصاد خرد",
                callback_data="microeconomics"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 بازار سرمایه",
                callback_data="capital_market"
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
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 🏦 BANKING
# =========================================================
def banking_main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 مبانی بانکداری",
                callback_data="banking_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 سپرده‌ها و حساب‌ها",
                callback_data="banking_deposits"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 تسهیلات و اعتبارات",
                callback_data="banking_facilities"
            )
        ],
        [
            InlineKeyboardButton(
                "📑 عقود بانکی",
                callback_data="banking_contracts"
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
                "🧾 چک و اسناد بانکی",
                callback_data="banking_checks"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 مبارزه با پولشویی",
                callback_data="banking_aml"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 اعتبارسنجی مشتریان",
                callback_data="banking_credit"
            )
        ],
        [
            InlineKeyboardButton(
                "💻 بانکداری الکترونیک",
                callback_data="banking_electronic"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 مدیریت ریسک بانکی",
                callback_data="banking_risk"
            )
        ],
        [
            InlineKeyboardButton(
                "🏛️ بانک مرکزی و سیاست پولی",
                callback_data="banking_central"
            )
        ],
        [
            InlineKeyboardButton(
                "🕌 بانکداری اسلامی",
                callback_data="banking_islamic"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 تست تخصصی بانکداری",
                callback_data="banking_quiz"
            )
        ],
        [
            InlineKeyboardButton(
                "🏆 آزمون جامع بانکداری",
                callback_data="banking_full_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 🎓 EXAMS CENTER
# =========================================================
def exams_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 آزمون مدیریت",
                callback_data="exam_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 آزمون تجارت",
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
                callback_data="exam_economics"
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
                "🎯 آزمون استخدامی بانک‌ها",
                callback_data="employment"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
def exams_text():
    return f"""
🎓 <b>مرکز آزمون اندیشکده</b>
محیط تخصصی سنجش دانش و آمادگی آزمونی
{SEPARATOR}
📚 مدیریت
🌍 تجارت و بازرگانی
📈 بازاریابی و فروش
💰 اقتصاد و بازار
🏦 بانکداری
🎯 استخدامی بانک‌ها
{SEPARATOR}
🎯 <b>روش پیشنهادی</b>
📖 مطالعه
⬇️
📝 تست
⬇️
🔍 بررسی پاسخ
⬇️
📊 تحلیل عملکرد
⬇️
🏆 آزمون مجدد
👇 آزمون موردنظر را انتخاب کنید.
"""
# =========================================================
# 🎯 EMPLOYMENT
# =========================================================
def employment_main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 بانک ملی",
                callback_data="employment_melli"
            ),
            InlineKeyboardButton(
                "🏦 بانک ملت",
                callback_data="employment_mellat"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک تجارت",
                callback_data="employment_tejarat"
            ),
            InlineKeyboardButton(
                "🏦 بانک صادرات",
                callback_data="employment_saderat"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک رفاه",
                callback_data="employment_refah"
            ),
            InlineKeyboardButton(
                "🏦 بانک شهر",
                callback_data="employment_shahr"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک مسکن",
                callback_data="employment_maskan"
            ),
            InlineKeyboardButton(
                "🏦 بانک کشاورزی",
                callback_data="employment_keshavarzi"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک سپه",
                callback_data="employment_sepah"
            ),
            InlineKeyboardButton(
                "🏦 بانک مهر ایران",
                callback_data="employment_mehr"
            ),
        ],
        [
            InlineKeyboardButton(
                "📚 منابع و دروس",
                callback_data="employment_subjects"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 هوش و استعداد",
                callback_data="employment_iq"
            )
        ],
        [
            InlineKeyboardButton(
                "🇬🇧 زبان انگلیسی",
                callback_data="employment_english"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون جامع استخدامی",
                callback_data="employment_full_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🎤 آمادگی مصاحبه",
                callback_data="employment_interview"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 🏦 EMPLOYMENT BANK MENU
# =========================================================
def employment_bank_menu(bank_name=None):
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 درسنامه تخصصی",
                callback_data=f"bank_lesson_{bank_name or 'bank'}"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 نمونه سؤالات",
                callback_data=f"bank_questions_{bank_name or 'bank'}"
            )
        ],
        [
            InlineKeyboardButton(
                "⏱️ آزمون زمان‌دار",
                callback_data=f"bank_exam_{bank_name or 'bank'}"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 نکات مهم آزمونی",
                callback_data=f"bank_tips_{bank_name or 'bank'}"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 آزمون‌های استخدامی",
                callback_data="employment"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 📱 SOCIAL
# =========================================================
def social_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📸 اینستاگرام",
                callback_data="social_instagram"
            )
        ],
        [
            InlineKeyboardButton(
                "✈️ تلگرام",
                callback_data="social_telegram"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 واتساپ",
                callback_data="social_whatsapp"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 📂 FILES
# =========================================================
def files_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 جزوات مدیریت",
                callback_data="files_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 جزوات تجارت",
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
                "🎯 منابع استخدامی",
                callback_data="files_employment"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# 🔙 GENERIC BACK BUTTONS
# =========================================================
def back_to_home():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data=HOME
                )
            ]
        ]
    )
def back_to_exams():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 مرکز آزمون",
                    callback_data="exams"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data=HOME
                )
            ],
        ]
    )
def back_to_employment():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 آزمون‌های استخدامی",
                    callback_data="employment"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data=HOME
                )
            ],
        ]
    )
# =========================================================
# 📊 PROFILE — آماده برای مرحله بعد
# =========================================================
def profile_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📊 عملکرد من",
                callback_data="profile_stats"
            )
        ],
        [
            InlineKeyboardButton(
                "🏆 سطح و امتیاز",
                callback_data="profile_level"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 سابقه آزمون‌ها",
                callback_data="profile_history"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 نقاط قوت و ضعف",
                callback_data="profile_analysis"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data=HOME
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
