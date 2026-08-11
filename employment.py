# =========================================================
# 🎯 ANDISHKADEH — BANK EMPLOYMENT CENTER
# =========================================================
#
# مرکز تخصصی آمادگی آزمون استخدامی بانک‌ها
#
# امکانات:
# 🏦 معرفی مسیر بانک‌ها
# 📚 دسته‌بندی دروس
# 🧠 هوش و استعداد
# 🇬🇧 زبان انگلیسی
# 💻 فناوری اطلاعات
# 📊 اقتصاد
# 🏦 بانکداری
# ⚖️ قوانین و مقررات
# 📝 آزمون جامع
# 🎤 مصاحبه استخدامی
#
# =========================================================
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# =========================================================
# CONSTANTS
# =========================================================
SEPARATOR = "━━━━━━━━━━━━━━━━━━"
# =========================================================
# BANK DATABASE
# =========================================================
BANKS = {
    "melli": {
        "name": "بانک ملی ایران",
        "emoji": "🏦",
    },
    "mellat": {
        "name": "بانک ملت",
        "emoji": "🏦",
    },
    "tejarat": {
        "name": "بانک تجارت",
        "emoji": "🏦",
    },
    "saderat": {
        "name": "بانک صادرات ایران",
        "emoji": "🏦",
    },
    "refah": {
        "name": "بانک رفاه کارگران",
        "emoji": "🏦",
    },
    "shahr": {
        "name": "بانک شهر",
        "emoji": "🏦",
    },
    "maskan": {
        "name": "بانک مسکن",
        "emoji": "🏦",
    },
    "keshavarzi": {
        "name": "بانک کشاورزی",
        "emoji": "🏦",
    },
    "sepah": {
        "name": "بانک سپه",
        "emoji": "🏦",
    },
    "mehr": {
        "name": "بانک قرض‌الحسنه مهر ایران",
        "emoji": "🏦",
    },
}
# =========================================================
# EMPLOYMENT SUBJECTS
# =========================================================
EMPLOYMENT_SUBJECTS = {
    "general": {
        "title": "📚 دروس عمومی",
        "items": [
            ("ادبیات فارسی", "employment_literature"),
            ("معارف و اطلاعات عمومی", "employment_general"),
            ("زبان انگلیسی", "employment_english"),
            ("فناوری اطلاعات", "employment_it"),
            ("هوش و استعداد", "employment_iq"),
        ],
    },
    "specialized": {
        "title": "🏦 دروس تخصصی",
        "items": [
            ("مبانی بانکداری", "employment_banking"),
            ("عملیات بانکی", "employment_operations"),
            ("اقتصاد", "employment_economics"),
            ("مدیریت", "employment_management"),
            ("حسابداری", "employment_accounting"),
            ("حقوق و قوانین بانکی", "employment_law"),
        ],
    },
}
# =========================================================
# MAIN EMPLOYMENT MENU
# =========================================================
def employment_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 بانک‌های هدف",
                callback_data="employment_banks"
            )
        ],
        [
            InlineKeyboardButton(
                "📚 دروس عمومی",
                callback_data="employment_general_subjects"
            ),
            InlineKeyboardButton(
                "🏦 دروس تخصصی",
                callback_data="employment_specialized_subjects"
            ),
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
                "💻 فناوری اطلاعات",
                callback_data="employment_it"
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
                "🎯 مسیر پیشنهادی مطالعه",
                callback_data="employment_roadmap"
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
# MAIN TEXT
# =========================================================
def employment_text():
    return f"""
🎯 <b>مرکز آمادگی آزمون استخدامی بانک‌ها</b>
جایی برای تبدیل مطالعه پراکنده
به یک مسیر منظم و هدفمند.
{SEPARATOR}
🏦 <b>بانک‌های هدف</b>
بانک ملی
بانک ملت
بانک تجارت
بانک صادرات
بانک رفاه
بانک شهر
بانک مسکن
بانک کشاورزی
بانک سپه
بانک مهر ایران
{SEPARATOR}
📚 <b>مسیر آمادگی</b>
1️⃣ دروس عمومی
2️⃣ دروس تخصصی
3️⃣ هوش و استعداد
4️⃣ آزمون‌های موضوعی
5️⃣ آزمون جامع
6️⃣ تحلیل عملکرد
7️⃣ آمادگی مصاحبه
{SEPARATOR}
🎯 هدف ما:
افزایش دانش تخصصی،
افزایش سرعت تست‌زنی،
شناخت نقاط ضعف،
و رسیدن به آمادگی واقعی آزمون.
👇 مسیر موردنظر خود را انتخاب کنید.
"""
# =========================================================
# BANKS MENU
# =========================================================
def banks_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏦 بانک ملی",
                callback_data="employment_bank_melli"
            ),
            InlineKeyboardButton(
                "🏦 بانک ملت",
                callback_data="employment_bank_mellat"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک تجارت",
                callback_data="employment_bank_tejarat"
            ),
            InlineKeyboardButton(
                "🏦 بانک صادرات",
                callback_data="employment_bank_saderat"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک رفاه",
                callback_data="employment_bank_refah"
            ),
            InlineKeyboardButton(
                "🏦 بانک شهر",
                callback_data="employment_bank_shahr"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک مسکن",
                callback_data="employment_bank_maskan"
            ),
            InlineKeyboardButton(
                "🏦 بانک کشاورزی",
                callback_data="employment_bank_keshavarzi"
            ),
        ],
        [
            InlineKeyboardButton(
                "🏦 بانک سپه",
                callback_data="employment_bank_sepah"
            ),
            InlineKeyboardButton(
                "🏦 بانک مهر ایران",
                callback_data="employment_bank_mehr"
            ),
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
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
# BANK DETAIL MENU
# =========================================================
def bank_detail_menu(bank_key):
    bank = BANKS.get(bank_key)
    if not bank:
        return employment_menu()
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 منابع و دروس",
                callback_data=f"bank_subjects_{bank_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 نمونه سؤالات",
                callback_data=f"bank_questions_{bank_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "⏱️ آزمون زمان‌دار",
                callback_data=f"bank_exam_{bank_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 نکات مهم آزمونی",
                callback_data=f"bank_tips_{bank_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "🎤 آمادگی مصاحبه",
                callback_data=f"bank_interview_{bank_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بانک‌های هدف",
                callback_data="employment_banks"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# BANK DETAIL TEXT
# =========================================================
def bank_detail_text(bank_key):
    bank = BANKS.get(bank_key)
    if not bank:
        return "⚠️ بانک موردنظر پیدا نشد."
    return f"""
{bank["emoji"]} <b>{bank["name"]}</b>
{SEPARATOR}
🎯 <b>مرکز آمادگی استخدامی</b>
در این بخش می‌توانید مسیر آمادگی
خود را برای این بانک دنبال کنید.
📚 منابع و دروس
📝 نمونه سؤالات
⏱️ آزمون زمان‌دار
🎯 نکات آزمونی
🎤 آمادگی مصاحبه
{SEPARATOR}
⚠️ توجه:
مواد آزمون و شرایط استخدامی ممکن است
بر اساس دفترچه و فراخوان هر دوره
تغییر کند.
برای مطالعه دقیق، همیشه آخرین
دفترچه رسمی آزمون را ملاک قرار دهید.
👇 بخش موردنظر را انتخاب کنید.
"""
# =========================================================
# SUBJECT CATEGORY MENU
# =========================================================
def subject_category_menu(category):
    data = EMPLOYMENT_SUBJECTS.get(
        category
    )
    if not data:
        return employment_menu()
    keyboard = []
    for title, callback in data["items"]:
        keyboard.append(
            [
                InlineKeyboardButton(
                    title,
                    callback_data=callback
                )
            ]
        )
    keyboard.extend(
        [
            [
                InlineKeyboardButton(
                    "🔙 مرکز استخدامی",
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
    )
    return InlineKeyboardMarkup(
        keyboard
    )
# =========================================================
# GENERAL SUBJECTS
# =========================================================
def general_subjects_menu():
    return subject_category_menu(
        "general"
    )
def general_subjects_text():
    return f"""
📚 <b>دروس عمومی آزمون استخدامی</b>
{SEPARATOR}
این بخش برای تقویت پایه‌های عمومی
آزمون طراحی شده است.
📖 ادبیات فارسی
🌐 زبان انگلیسی
🧠 هوش و استعداد
💻 فناوری اطلاعات
🌍 اطلاعات عمومی
{SEPARATOR}
🎯 پیشنهاد:
ابتدا نقاط ضعف خود را شناسایی کنید،
سپس با تست‌های موضوعی سرعت و دقت
خود را افزایش دهید.
👇 درس موردنظر را انتخاب کنید.
"""
# =========================================================
# SPECIALIZED SUBJECTS
# =========================================================
def specialized_subjects_menu():
    return subject_category_menu(
        "specialized"
    )
def specialized_subjects_text():
    return f"""
🏦 <b>دروس تخصصی آزمون استخدامی</b>
{SEPARATOR}
مباحث تخصصی پیشنهادی:
🏦 مبانی بانکداری
💳 عملیات بانکی
💰 اقتصاد
👔 مدیریت
📒 حسابداری
⚖️ حقوق و قوانین بانکی
{SEPARATOR}
🎯 این بخش برای داوطلبانی طراحی شده
که می‌خواهند علاوه بر تست‌زنی،
مفاهیم تخصصی بانکداری را نیز تقویت کنند.
👇 درس موردنظر را انتخاب کنید.
"""
# =========================================================
# IQ
# =========================================================
def iq_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔢 دنباله‌های عددی",
                callback_data="iq_numbers"
            )
        ],
        [
            InlineKeyboardButton(
                "🔷 استدلال منطقی",
                callback_data="iq_logic"
            )
        ],
        [
            InlineKeyboardButton(
                "🧩 الگوها",
                callback_data="iq_patterns"
            )
        ],
        [
            InlineKeyboardButton(
                "⏱️ آزمون هوش زمان‌دار",
                callback_data="iq_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
                callback_data="employment"
            )
        ],
    ]
    return InlineKeyboardMarkup(
        keyboard
    )
def iq_text():
    return f"""
🧠 <b>هوش و استعداد</b>
{SEPARATOR}
در آزمون‌های استخدامی،
سرعت تحلیل و دقت در حل مسئله
اهمیت بالایی دارد.
تمرکز این بخش:
🔢 دنباله‌های عددی
🧩 الگوها
🔷 استدلال منطقی
📐 حل مسئله
⏱️ مدیریت زمان
🎯 هدف:
افزایش سرعت تشخیص الگو
و کاهش زمان پاسخ‌گویی.
"""
# =========================================================
# ENGLISH
# =========================================================
def english_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 واژگان",
                callback_data="english_vocabulary"
            )
        ],
        [
            InlineKeyboardButton(
                "📚 گرامر",
                callback_data="english_grammar"
            )
        ],
        [
            InlineKeyboardButton(
                "📄 درک مطلب",
                callback_data="english_reading"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون زبان",
                callback_data="english_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
                callback_data="employment"
            )
        ],
    ]
    return InlineKeyboardMarkup(
        keyboard
    )
def english_text():
    return f"""
🇬🇧 <b>زبان انگلیسی</b>
{SEPARATOR}
تمرکز آزمونی:
📖 Vocabulary
📚 Grammar
📄 Reading Comprehension
📝 Test Techniques
🎯 پیشنهاد:
واژگان پرتکرار را مرور کنید،
سپس با تست زمان‌دار سرعت خواندن
و پاسخ‌گویی خود را افزایش دهید.
"""
# =========================================================
# IT
# =========================================================
def it_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "💻 مفاهیم پایه کامپیوتر",
                callback_data="it_basics"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 اینترنت و شبکه",
                callback_data="it_network"
            )
        ],
        [
            InlineKeyboardButton(
                "🔐 امنیت اطلاعات",
                callback_data="it_security"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون فناوری اطلاعات",
                callback_data="it_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
                callback_data="employment"
            )
        ],
    ]
    return InlineKeyboardMarkup(
        keyboard
    )
def it_text():
    return f"""
💻 <b>فناوری اطلاعات</b>
{SEPARATOR}
مباحث پیشنهادی:
🖥️ سخت‌افزار و نرم‌افزار
🌐 اینترنت و شبکه
🔐 امنیت اطلاعات
📊 نرم‌افزارهای عمومی
💾 مفاهیم داده
🎯 تمرکز اصلی:
شناخت مفاهیم پایه
و افزایش سرعت پاسخ‌گویی تستی.
"""
# =========================================================
# ROADMAP
# =========================================================
def roadmap_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📅 برنامه ۳۰ روزه",
                callback_data="roadmap_30"
            )
        ],
        [
            InlineKeyboardButton(
                "📅 برنامه ۶۰ روزه",
                callback_data="roadmap_60"
            )
        ],
        [
            InlineKeyboardButton(
                "🔥 برنامه فشرده",
                callback_data="roadmap_fast"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
                callback_data="employment"
            )
        ],
    ]
    return InlineKeyboardMarkup(
        keyboard
    )
def roadmap_text():
    return f"""
🎯 <b>مسیر پیشنهادی آمادگی آزمون</b>
{SEPARATOR}
1️⃣ <b>مرحله اول — یادگیری</b>
📚 مطالعه مفاهیم
📝 خلاصه‌نویسی
🔎 شناسایی نقاط ضعف
⬇️
2️⃣ <b>مرحله دوم — تست</b>
📝 تست موضوعی
⏱️ تست زمان‌دار
🔄 مرور پاسخ‌های غلط
⬇️
3️⃣ <b>مرحله سوم — آزمون جامع</b>
🎓 شبیه‌سازی شرایط آزمون
📊 محاسبه درصد
📈 تحلیل عملکرد
⬇️
4️⃣ <b>مرحله چهارم — تثبیت</b>
🔁 مرور اشتباهات
🎯 تمرکز روی نقاط ضعف
🏆 آزمون مجدد
{SEPARATOR}
💡 کیفیت مطالعه مهم‌تر از تعداد
ساعات مطالعه است.
"""
# =========================================================
# INTERVIEW
# =========================================================
def interview_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🎤 سوالات متداول مصاحبه",
                callback_data="interview_questions"
            )
        ],
        [
            InlineKeyboardButton(
                "👔 رفتار حرفه‌ای",
                callback_data="interview_behavior"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 سوالات تخصصی بانکی",
                callback_data="interview_banking"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 آمادگی روانی",
                callback_data="interview_mindset"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز استخدامی",
                callback_data="employment"
            )
        ],
    ]
    return InlineKeyboardMarkup(
        keyboard
    )
def interview_text():
    return f"""
🎤 <b>مرکز آمادگی مصاحبه استخدامی</b>
{SEPARATOR}
مصاحبه فقط پاسخ دادن به سؤال نیست؛
بلکه ترکیبی از دانش، رفتار حرفه‌ای،
اعتمادبه‌نفس و توانایی ارتباط است.
محورهای تمرین:
🎤 سوالات عمومی
🏦 سوالات بانکی
👔 رفتار حرفه‌ای
🧠 مدیریت استرس
💬 مهارت ارتباطی
{SEPARATOR}
🎯 قبل از مصاحبه:
✔️ درباره بانک هدف مطالعه کنید.
✔️ مفاهیم تخصصی را مرور کنید.
✔️ پاسخ‌های خود را تمرین کنید.
✔️ رزومه خود را به‌خوبی بشناسید.
✔️ آرام و حرفه‌ای پاسخ دهید.
"""
# =========================================================
# BANK INFORMATION
# =========================================================
def bank_info_text(bank_key):
    bank = BANKS.get(bank_key)
    if not bank:
        return "⚠️ اطلاعات بانک پیدا نشد."
    return f"""
{bank["emoji"]} <b>{bank["name"]}</b>
{SEPARATOR}
🎯 <b>مسیر پیشنهادی آمادگی</b>
📚 مطالعه دروس عمومی
🏦 مطالعه دروس تخصصی
🧠 تمرین هوش
📝 تست موضوعی
⏱️ آزمون زمان‌دار
📊 تحلیل عملکرد
🎤 آمادگی مصاحبه
{SEPARATOR}
⚠️ <b>یادآوری مهم</b>
شرایط، مواد امتحانی، ظرفیت و مراحل
استخدام می‌تواند در هر فراخوان تغییر کند.
برای اطلاعات قطعی، دفترچه رسمی همان
آزمون را بررسی کنید.
"""
# =========================================================
# CALLBACK HELPERS
# =========================================================
def employment_back_button():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 مرکز استخدامی",
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
    )
def banks_back_button():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 بانک‌های هدف",
                    callback_data="employment_banks"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="home"
                ),
            ],
        ]
    )
# =========================================================
# END
# =========================================================
