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
# INTERNATIONAL TRADE
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
# EMPLOYMENT
# =========================================================
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
# FLASK
# =========================================================
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
                "📝 استخدام بانک‌ها",
                callback_data="employment"
            ),
            InlineKeyboardButton(
                "📂 فایل و جزوات",
                callback_data="files"
            ),
        ],
        [
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
📝 آزمون‌های استخدامی بانک‌ها
🎓 آزمون و منابع آموزشی
━━━━━━━━━━━━━━━━━━
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
📚 راهنمای اندیشکده مدیریت و بازار
/start
نمایش منوی اصلی
/help
نمایش راهنما
از منوی اصلی می‌توانید به بخش‌های آموزشی، آزمون‌ها و استخدامی بانک‌ها دسترسی داشته باشید.
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
# EMPLOYMENT BANK MENU
# =========================================================
def employment_bank_menu(bank_id):
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 درسنامه تخصصی",
                callback_data=f"emp_lesson_{bank_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 نمونه سؤالات",
                callback_data=f"emp_questions_{bank_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "⏱️ آزمون زمان‌دار",
                callback_data=f"emp_exam_{bank_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 نکات مهم آزمون",
                callback_data=f"emp_tips_{bank_id}"
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
                callback_data="home"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# BANK INFORMATION
# =========================================================
BANKS = {
    "melli": "🏛️ بانک ملی ایران",
    "mellat": "🔵 بانک ملت",
    "tejarat": "🟢 بانک تجارت",
    "saderat": "🔴 بانک صادرات ایران",
    "refah": "🟠 بانک رفاه کارگران",
    "shahr": "🔷 بانک شهر",
    "maskan": "🟦 بانک مسکن",
    "keshavarzi": "🌾 بانک کشاورزی",
    "sepah": "🟣 بانک سپه",
    "mehr": "💚 بانک قرض‌الحسنه مهر ایران",
}
# =========================================================
# BANK LESSON TEXT
# =========================================================
def bank_lesson_text(bank_name):
    return f"""
📖 درسنامه استخدامی {bank_name}
در این بخش مطالب مهم و کاربردی برای آمادگی آزمون استخدامی بانک‌ها ارائه می‌شود.
━━━━━━━━━━━━━━━━━━
🏦 بانکداری
• مبانی بانکداری
• وظایف بانک‌ها
• انواع بانک‌ها
• سپرده‌ها
• تسهیلات
• اعتبارسنجی
• بانکداری الکترونیک
• خدمات بانکی
• بانکداری اسلامی
━━━━━━━━━━━━━━━━━━
⚖️ قوانین بانکی
• قانون عملیات بانکی بدون ربا
• قانون مبارزه با پولشویی
• تأمین مالی تروریسم
• قوانین چک
• مقررات بانک مرکزی
• حقوق بانک و مشتری
━━━━━━━━━━━━━━━━━━
💰 اقتصاد
• عرضه و تقاضا
• تورم
• بیکاری
• نرخ بهره
• نرخ ارز
• نقدینگی
• سیاست پولی
• سیاست مالی
• اقتصاد خرد
• اقتصاد کلان
━━━━━━━━━━━━━━━━━━
📊 مدیریت
• برنامه‌ریزی
• سازماندهی
• رهبری
• کنترل
• تصمیم‌گیری
• رفتار سازمانی
• منابع انسانی
• مدیریت استراتژیک
━━━━━━━━━━━━━━━━━━
🧾 حسابداری
• اصول حسابداری
• دارایی
• بدهی
• سرمایه
• درآمد
• هزینه
• سود و زیان
• صورت‌های مالی
• حسابداری بانکی
━━━━━━━━━━━━━━━━━━
🧠 هوش و استعداد
• دنباله‌ها
• الگوها
• استدلال
• هوش عددی
• هوش کلامی
• حل مسئله
• سرعت و دقت
━━━━━━━━━━━━━━━━━━
🇬🇧 زبان انگلیسی
• واژگان
• گرامر
• درک مطلب
• کلوز تست
• مترادف و متضاد
━━━━━━━━━━━━━━━━━━
💻 ICDL
• Word
• Excel
• PowerPoint
• Internet
• Windows
• مفاهیم فناوری اطلاعات
━━━━━━━━━━━━━━━━━━
🎯 هدف:
آمادگی علمی و تستی برای آزمون استخدامی {bank_name}.
"""
# =========================================================
# BANK QUESTIONS TEXT
# =========================================================
def bank_questions_text(bank_name):
    return f"""
📝 نمونه سؤالات استخدامی
🏦 {bank_name}
در این بخش مجموعه‌ای از سؤالات تمرینی مرتبط با آزمون‌های استخدامی بانک‌ها قرار می‌گیرد.
━━━━━━━━━━━━━━━━━━
📚 محورهای سؤال:
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
━━━━━━━━━━━━━━━━━━
🎯 پیشنهاد مطالعه:
ابتدا درسنامه را مطالعه کنید.
سپس تست‌های آموزشی را حل کنید.
در مرحله بعد تست زمان‌دار بزنید.
در پایان آزمون جامع را انجام دهید.
"""
# =========================================================
# BANK TIPS
# =========================================================
def bank_tips_text(bank_name):
    return f"""
🎯 نکات مهم آزمون استخدامی
🏦 {bank_name}
━━━━━━━━━━━━━━━━━━
⭐ نکته 1
قبل از تست‌زنی، مفاهیم اصلی هر درس را یاد بگیرید.
⭐ نکته 2
سؤالات اشتباه را علامت‌گذاری کنید.
⭐ نکته 3
برای هوش و زبان زمان مشخص روزانه داشته باشید.
⭐ نکته 4
تست‌های زمان‌دار را جدی بگیرید.
⭐ نکته 5
در هفته‌های پایانی، آزمون جامع برگزار کنید.
━━━━━━━━━━━━━━━━━━
⏱️ مدیریت زمان
اگر سؤال سخت بود، بیش از حد روی آن توقف نکنید.
به سؤالات ساده‌تر پاسخ دهید و سپس به سؤالات دشوار برگردید.
━━━━━━━━━━━━━━━━━━
🎯 هدف:
افزایش دقت + افزایش سرعت + کاهش خطا
"""
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
    # =====================================================
    # MANAGEMENT ANSWERS
    # =====================================================
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
                reply_markup=InlineKeyboardMarkup([
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
                ])
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
    # =====================================================
    # TRADE ANSWERS
    # =====================================================
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
                reply_markup=InlineKeyboardMarkup([
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
                ])
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
    # =====================================================
    # MARKETING ANSWERS
    # =====================================================
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
                reply_markup=InlineKeyboardMarkup([
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
                ])
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
    # =====================================================
    # ECONOMY ANSWERS
    # =====================================================
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
                reply_markup=InlineKeyboardMarkup([
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
                ])
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
    # EMPLOYMENT
    # =====================================================
    if data == "employment":
        await query.edit_message_text(
            employment_banks_text(),
            reply_markup=employment_menu()
        )
        return
    # =====================================================
    # EMPLOYMENT BANKS
    # =====================================================
    if data.startswith("employment_"):
        bank_id = data.replace(
            "employment_",
            ""
        )
        if bank_id in BANKS:
            bank_name = BANKS[bank_id]
            await query.edit_message_text(
                employment_bank_text(
                    bank_name
                ),
                reply_markup=employment_bank_menu(
                    bank_id
                )
            )
            return
    # =====================================================
    # EMPLOYMENT SUBJECTS
    # =====================================================
    if data == "employment_subjects":
        await query.edit_message_text(
            employment_subjects_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 آزمون‌های استخدامی",
                        callback_data="employment"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ],
            ])
        )
        return
    # =====================================================
    # EMPLOYMENT IQ
    # =====================================================
    if data == "employment_iq":
        await query.edit_message_text(
            employment_iq_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 آزمون‌های استخدامی",
                        callback_data="employment"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ],
            ])
        )
        return
    # =====================================================
    # EMPLOYMENT ENGLISH
    # =====================================================
    if data == "employment_english":
        await query.edit_message_text(
            employment_english_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 آزمون‌های استخدامی",
                        callback_data="employment"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ],
            ])
        )
        return
    # =====================================================
    # EMPLOYMENT FULL EXAM
    # =====================================================
    if data == "employment_full_exam":
        await query.edit_message_text(
            employment_full_exam_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 آزمون‌های استخدامی",
                        callback_data="employment"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ],
            ])
        )
        return
    # =====================================================
    # EMPLOYMENT INTERVIEW
    # =====================================================
    if data == "employment_interview":
        await query.edit_message_text(
            employment_interview_text(),
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔙 آزمون‌های استخدامی",
                        callback_data="employment"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="home"
                    )
                ],
            ])
        )
        return
    # =====================================================
    # EMPLOYMENT BANK LESSON
    # =====================================================
    if data.startswith("emp_lesson_"):
        bank_id = data.replace(
            "emp_lesson_",
            ""
        )
        bank_name = BANKS.get(
            bank_id,
            "بانک موردنظر"
        )
        await query.edit_message_text(
            bank_lesson_text(
                bank_name
            ),
            reply_markup=employment_bank_menu(
                bank_id
            )
        )
        return
    # =====================================================
    # EMPLOYMENT BANK QUESTIONS
    # =====================================================
    if data.startswith("emp_questions_"):
        bank_id = data.replace(
            "emp_questions_",
            ""
        )
        bank_name = BANKS.get(
            bank_id,
            "بانک موردنظر"
        )
        await query.edit_message_text(
            bank_questions_text(
                bank_name
            ),
            reply_markup=employment_bank_menu(
                bank_id
            )
        )
        return
    # =====================================================
    # EMPLOYMENT BANK TIPS
    # =====================================================
    if data.startswith("emp_tips_"):
        bank_id = data.replace(
            "emp_tips_",
            ""
        )
        bank_name = BANKS.get(
            bank_id,
            "بانک موردنظر"
        )
        await query.edit_message_text(
            bank_tips_text(
                bank_name
            ),
            reply_markup=employment_bank_menu(
                bank_id
            )
        )
        return
    # =====================================================
    # EMPLOYMENT BANK EXAM
    # =====================================================
    if data.startswith("emp_exam_"):
        bank_id = data.replace(
            "emp_exam_",
            ""
        )
        bank_name = BANKS.get(
            bank_id,
            "بانک موردنظر"
        )
        await query.edit_message_text(
            f"""
🏆 آزمون استخدامی
{bank_name}
━━━━━━━━━━━━━━━━━━
⏱️ آزمون زمان‌دار
این بخش برای اجرای آزمون‌های تخصصی و شبیه‌سازی شرایط آزمون استخدامی طراحی شده است.
📚 محورهای آزمون:
🏦 بانکداری
⚖️ قوانین بانکی
💰 اقتصاد
📊 مدیریت
🧾 حسابداری
📈 مدیریت مالی
🧠 هوش
🇬🇧 زبان
💻 ICDL
🚧 بانک سؤال اختصاصی این آزمون در حال توسعه است.
""",
            reply_markup=employment_bank_menu(
                bank_id
            )
        )
        return
    # =====================================================
    # OTHER SECTIONS
    # =====================================================
    if data == "banking":
        await generic_message(
            query,
            "🏦 بانکداری",
            """
در این بخش مطالب تخصصی بانکداری قرار می‌گیرد.
📚 مبانی بانکداری
💰 سپرده‌ها
🏦 تسهیلات
⚖️ قوانین بانکی
💳 خدمات بانکی
💻 بانکداری الکترونیک
📊 اعتبارسنجی
🛡️ مدیریت ریسک
"""
        )
        return
    if data == "exam":
        await generic_message(
            query,
            "🎓 آزمون و تست",
            """
📝 آزمون‌های آموزشی اندیشکده
📚 مدیریت
🌍 تجارت بین‌الملل
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
📝 استخدامی بانک‌ها
آزمون‌های تخصصی بیشتر به‌تدریج اضافه می‌شوند.
"""
        )
        return
    if data == "files":
        await generic_message(
            query,
            "📂 فایل و جزوات",
            """
📂 مرکز فایل و جزوات آموزشی
در این بخش می‌توان جزوات، خلاصه درس‌ها، نمونه سؤالات و منابع آموزشی را قرار داد.
"""
        )
        return
    if data == "social":
        await generic_message(
            query,
            "📱 شبکه‌های اجتماعی",
            """
📱 شبکه‌های اجتماعی اندیشکده مدیریت و بازار
محتوای آموزشی جدید را در شبکه‌های اجتماعی اندیشکده دنبال کنید.
📚 مدیریت
🌍 تجارت
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
📝 استخدامی بانک‌ها
"""
        )
        return
    # =====================================================
    # MANAGEMENT OTHER SECTIONS
    # =====================================================
    if data == "organizational_behavior":
        await generic_message(
            query,
            "📊 رفتار سازمانی",
            """
📊 رفتار سازمانی
موضوعات اصلی:
👥 رفتار فردی
👥 رفتار گروهی
🧠 انگیزش
🎯 رهبری
💬 ارتباطات
⚡ تعارض
🏢 فرهنگ سازمانی
"""
        )
        return
    if data == "strategic_management":
        await generic_message(
            query,
            "🎯 مدیریت استراتژیک",
            """
🎯 مدیریت استراتژیک
موضوعات اصلی:
🔎 تحلیل محیط
🎯 مأموریت و چشم‌انداز
📊 SWOT
🏆 مزیت رقابتی
🧭 استراتژی
📈 اجرای استراتژی
📊 کنترل استراتژیک
"""
        )
        return
    if data == "human_resources":
        await generic_message(
            query,
            "👥 مدیریت منابع انسانی",
            """
👥 مدیریت منابع انسانی
موضوعات اصلی:
📋 برنامه‌ریزی نیروی انسانی
👤 جذب و استخدام
🎓 آموزش
📊 ارزیابی عملکرد
💰 جبران خدمات
🎯 انگیزش
🏆 توسعه کارکنان
"""
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
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home"
                )
            ]
        ])
    )
# =========================================================
# MAIN
# =========================================================
def main():
    if not TOKEN:
        raise ValueError(
            "BOT_TOKEN تنظیم نشده است."
        )
    # Flask
    Thread(
        target=run_flask,
        daemon=True
    ).start()
    # Telegram Application
    telegram_app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )
    # Commands
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
    # Callback buttons
    telegram_app.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )
    # Start polling
    telegram_app.run_polling(
        drop_pending_updates=True
    )
# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    main()
