# =========================================================
# 🎯 ANDISHKADEH
# مرکز تخصصی آزمون استخدامی بانک‌ها
# =========================================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


SEPARATOR = "━━━━━━━━━━━━━━━━━━"


# =========================================================
# 🏦 BANKS
# =========================================================

BANKS = {
    "melli": "بانک ملی ایران",
    "mellat": "بانک ملت",
    "tejarat": "بانک تجارت",
    "saderat": "بانک صادرات ایران",
    "refah": "بانک رفاه کارگران",
    "shahr": "بانک شهر",
    "maskan": "بانک مسکن",
    "keshavarzi": "بانک کشاورزی",
    "sepah": "بانک سپه",
    "mehr": "بانک قرض‌الحسنه مهر ایران",
}


# =========================================================
# 🏠 MAIN EMPLOYMENT MENU
# =========================================================

def employment_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🏦 بانک‌های هدف",
                callback_data="employment_banks",
            )
        ],

        [
            InlineKeyboardButton(
                "📚 دروس و منابع",
                callback_data="employment_subjects",
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
                "🏆 آزمون جامع استخدامی",
                callback_data="employment_full_exam",
            )
        ],

        [
            InlineKeyboardButton(
                "📝 شروع آزمون استخدامی",
                callback_data="employment_exam",
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
                "🎯 مسیر پیشنهادی مطالعه",
                callback_data="employment_roadmap",
            )
        ],

        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# 🎯 MAIN TEXT
# =========================================================

def employment_banks_text():

    return f"""
🎯 <b>مرکز تخصصی آمادگی آزمون استخدامی بانک‌ها</b>

{SEPARATOR}

اینجا فقط یک مجموعه تست ساده نیست.

این بخش برای طراحی یک مسیر کامل
از <b>یادگیری → تمرین → تست → آزمون → تحلیل → مصاحبه</b>
ساخته شده است.

{SEPARATOR}

🏦 <b>بانک‌های هدف</b>

• بانک ملی ایران
• بانک ملت
• بانک تجارت
• بانک صادرات ایران
• بانک رفاه کارگران
• بانک شهر
• بانک مسکن
• بانک کشاورزی
• بانک سپه
• بانک قرض‌الحسنه مهر ایران

{SEPARATOR}

📚 <b>مسیر آمادگی</b>

1️⃣ یادگیری مفاهیم
2️⃣ مطالعه منابع
3️⃣ تست موضوعی
4️⃣ آزمون زمان‌دار
5️⃣ تحلیل پاسخ‌ها
6️⃣ شناسایی نقاط ضعف
7️⃣ آزمون جامع
8️⃣ آمادگی مصاحبه

{SEPARATOR}

⚠️ <b>نکته مهم</b>

مواد آزمون، شرایط استخدام، ظرفیت‌ها و
مراحل جذب ممکن است در هر فراخوان تغییر کنند.

بنابراین برای شرایط قطعی هر آزمون،
همیشه آخرین دفترچه رسمی همان فراخوان
باید ملاک قرار گیرد.

👇 مسیر موردنظر خود را انتخاب کنید.
"""


# =========================================================
# 🏦 BANKS MENU
# =========================================================

def employment_bank_menu(bank_name=None):

    keyboard = []

    bank_callbacks = [
        ("🏦 بانک ملی ایران", "employment_melli"),
        ("🏦 بانک ملت", "employment_mellat"),
        ("🏦 بانک تجارت", "employment_tejarat"),
        ("🏦 بانک صادرات ایران", "employment_saderat"),
        ("🏦 بانک رفاه کارگران", "employment_refah"),
        ("🏦 بانک شهر", "employment_shahr"),
        ("🏦 بانک مسکن", "employment_maskan"),
        ("🏦 بانک کشاورزی", "employment_keshavarzi"),
        ("🏦 بانک سپه", "employment_sepah"),
        ("🏦 بانک مهر ایران", "employment_mehr"),
    ]

    row = []

    for title, callback in bank_callbacks:

        row.append(
            InlineKeyboardButton(
                title,
                callback_data=callback,
            )
        )

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.extend(
        [
            [
                InlineKeyboardButton(
                    "🔙 مرکز استخدامی",
                    callback_data="employment",
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

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# 🏦 BANK DETAIL
# =========================================================

def employment_bank_text(bank_name):

    return f"""
🏦 <b>{bank_name}</b>

{SEPARATOR}

🎯 <b>مسیر آمادگی استخدامی</b>

در این بخش می‌توانید آمادگی خود را
برای آزمون و مراحل جذب این بانک
به‌صورت هدفمند دنبال کنید.

{SEPARATOR}

📚 <b>محورهای مطالعه</b>

• دروس عمومی
• مبانی بانکداری
• عملیات بانکی
• اقتصاد
• مدیریت
• حسابداری
• حقوق و قوانین بانکی
• هوش و استعداد
• زبان انگلیسی
• فناوری اطلاعات

{SEPARATOR}

📝 <b>مهارت‌های آزمونی</b>

⏱️ مدیریت زمان
🎯 افزایش دقت
🧠 تحلیل سؤال
📊 تحلیل عملکرد
🔄 مرور پاسخ‌های غلط

{SEPARATOR}

⚠️ شرایط و مواد امتحانی ممکن است
در هر فراخوان تغییر کند.

📌 آخرین دفترچه رسمی آزمون را
همیشه ملاک قرار دهید.
"""


# =========================================================
# 📚 SUBJECTS
# =========================================================

def employment_subjects_text():

    return f"""
📚 <b>دروس و منابع آزمون استخدامی</b>

{SEPARATOR}

🏦 <b>دروس تخصصی بانکی</b>

• مبانی بانکداری
• عملیات بانکی
• سپرده‌ها
• تسهیلات
• عقود بانکی
• اعتبارسنجی
• مدیریت ریسک
• بانکداری الکترونیک
• قوانین و مقررات بانکی
• مبارزه با پولشویی

{SEPARATOR}

💰 <b>اقتصاد</b>

• اقتصاد خرد
• اقتصاد کلان
• عرضه و تقاضا
• تورم
• نرخ ارز
• سیاست پولی
• سیاست مالی

{SEPARATOR}

👔 <b>مدیریت</b>

• اصول مدیریت
• برنامه‌ریزی
• سازماندهی
• رهبری
• کنترل
• تصمیم‌گیری
• رفتار سازمانی

{SEPARATOR}

📒 <b>حسابداری</b>

• اصول حسابداری
• صورت‌های مالی
• حسابداری بانکی
• مفاهیم بدهکار و بستانکار
• تجزیه و تحلیل مالی

{SEPARATOR}

⚖️ <b>حقوق و قوانین</b>

• قوانین بانکی
• مقررات مرتبط با چک
• قوانین پولشویی
• مقررات اعتباری
• مفاهیم حقوق تجارت

📌 محتوای مقرراتی باید متناسب با
آخرین مقررات و دفترچه آزمون به‌روزرسانی شود.
"""


# =========================================================
# 🧠 IQ
# =========================================================

def employment_iq_text():

    return f"""
🧠 <b>هوش و استعداد تحصیلی</b>

{SEPARATOR}

یکی از بخش‌های مهم بسیاری از
آزمون‌های استخدامی، توانایی تحلیل
و حل مسئله است.

🎯 محورهای تمرین:

🔢 دنباله‌های عددی

🔷 استدلال منطقی

🧩 تشخیص الگو

📐 حل مسئله

🧠 استدلال کلامی

📊 تحلیل داده

⏱️ مدیریت زمان

{SEPARATOR}

💡 <b>استراتژی پیشنهادی</b>

ابتدا نوع سؤال را سریع تشخیص دهید،
سپس روش حل مناسب را انتخاب کنید.

هدف فقط درست جواب دادن نیست؛

🎯 <b>درست + سریع + دقیق</b>
"""


# =========================================================
# 🇬🇧 ENGLISH
# =========================================================

def employment_english_text():

    return f"""
🇬🇧 <b>زبان انگلیسی آزمون استخدامی</b>

{SEPARATOR}

📖 <b>Vocabulary</b>

تمرکز روی واژگان پرتکرار،
واژگان عمومی و اصطلاحات کاربردی.

{SEPARATOR}

📚 <b>Grammar</b>

• زمان‌ها
• افعال
• ضمایر
• حروف اضافه
• جملات شرطی
• ساختار جمله

{SEPARATOR}

📄 <b>Reading Comprehension</b>

تمرین:

• Skimming
• Scanning
• پیدا کردن ایده اصلی
• تشخیص مفهوم از متن

{SEPARATOR}

🎯 <b>هدف</b>

افزایش سرعت خواندن و کاهش زمان
پاسخ‌گویی به سؤالات زبان.
"""


# =========================================================
# 💻 IT
# =========================================================

def employment_it_text():

    return f"""
💻 <b>فناوری اطلاعات</b>

{SEPARATOR}

🖥️ مفاهیم سخت‌افزار و نرم‌افزار

🌐 اینترنت و شبکه

🔐 امنیت اطلاعات

💾 داده و اطلاعات

📊 نرم‌افزارهای عمومی

🗂️ سیستم‌عامل‌ها

🧠 مفاهیم پایه فناوری اطلاعات

{SEPARATOR}

🎯 تمرکز آزمونی:

شناخت مفهوم + تشخیص گزینه صحیح
+ افزایش سرعت پاسخ‌گویی.
"""


# =========================================================
# 🏆 FULL EXAM
# =========================================================

def employment_full_exam_text():

    return f"""
🏆 <b>آزمون جامع استخدامی بانک‌ها</b>

{SEPARATOR}

🎯 <b>شبیه‌سازی آزمون واقعی</b>

این بخش برای ترکیب چند حوزه
و سنجش آمادگی کلی داوطلب طراحی شده است.

{SEPARATOR}

📚 محورهای آزمون:

🏦 بانکداری

💰 اقتصاد

👔 مدیریت

📒 حسابداری

⚖️ قوانین و مقررات

🧠 هوش و استعداد

🇬🇧 زبان انگلیسی

💻 فناوری اطلاعات

{SEPARATOR}

📊 <b>سیستم ارزیابی</b>

پس از تکمیل موتور آزمون:

✅ تعداد پاسخ صحیح
❌ تعداد پاسخ غلط
⚪ بدون پاسخ
📊 درصد
⏱️ زمان
🎯 سطح عملکرد
📈 تحلیل نقاط قوت و ضعف

{SEPARATOR}

🔥 هدف:

تبدیل مطالعه معمولی به
آمادگی واقعی آزمون استخدامی.

"""


# =========================================================
# 🎤 INTERVIEW
# =========================================================

def employment_interview_text():

    return f"""
🎤 <b>آمادگی مصاحبه استخدامی بانک</b>

{SEPARATOR}

مصاحبه فقط پاسخ دادن به سؤال نیست.

ترکیبی از:

🧠 دانش تخصصی
👔 رفتار حرفه‌ای
💬 مهارت ارتباطی
🎯 اعتمادبه‌نفس
⏱️ مدیریت استرس

{SEPARATOR}

🏦 <b>سؤالات تخصصی بانکی</b>

• سپرده چیست؟
• تسهیلات چیست؟
• تفاوت انواع عقود
• اعتبارسنجی چیست؟
• ریسک اعتباری چیست؟
• نقدینگی چیست؟
• بانک مرکزی چه نقشی دارد؟
• مبارزه با پولشویی چیست؟

{SEPARATOR}

👔 <b>رفتار حرفه‌ای</b>

✔️ پاسخ کوتاه و دقیق

✔️ حفظ آرامش

✔️ ارتباط چشمی مناسب

✔️ شناخت بانک هدف

✔️ شناخت دقیق رزومه

✔️ پرهیز از پاسخ‌های حفظی

"""


# =========================================================
# 🔙 BACK MENU
# =========================================================

def employment_back_menu():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔙 مرکز استخدامی",
                    callback_data="employment",
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


# =========================================================
# ALIASES / COMPATIBILITY
# =========================================================

def employment_menu_text():
    return employment_banks_text()


def employment_subjects_menu():
    return employment_back_menu()


def employment_iq_menu():
    return employment_back_menu()


def employment_english_menu():
    return employment_back_menu()


def employment_full_exam_menu():
    return employment_back_menu()


def employment_interview_menu():
    return employment_back_menu()


# =========================================================
# 📝 EMPLOYMENT EXAM ENGINE
# =========================================================
# سوالات این بخش «تمرینی» هستند و جایگزین دفترچه رسمی
# هیچ فراخوان استخدامی نیستند. مواد و شرایط هر فراخوان
# باید از آخرین دفترچه رسمی همان آزمون کنترل شود.
# =========================================================

import random

EMPLOYMENT_QUESTIONS = [
    {
        "category": "🏦 بانکداری",
        "question": "کدام گزینه بیشترین ارتباط را با مدیریت نقدینگی بانک دارد؟",
        "options": [
            "مدیریت جریان‌های ورودی و خروجی وجوه",
            "طراحی لوگوی بانک",
            "تغییر نام شعب",
            "افزایش تعداد فرم‌های اداری",
        ],
        "correct": 0,
        "explanation": "مدیریت نقدینگی بر توان بانک برای ایفای تعهدات و تنظیم جریان وجوه تمرکز دارد.",
    },
    {
        "category": "🏦 بانکداری",
        "question": "هدف اصلی اعتبارسنجی مشتری چیست؟",
        "options": [
            "ارزیابی توان و ریسک بازپرداخت تعهدات",
            "افزایش تعداد حساب‌های مشتری",
            "کاهش ساعات کاری شعبه",
            "تغییر نرخ ارز",
        ],
        "correct": 0,
        "explanation": "اعتبارسنجی برای ارزیابی ریسک اعتباری و توان ایفای تعهدات مشتری استفاده می‌شود.",
    },
    {
        "category": "💰 اقتصاد",
        "question": "در حالت عادی، افزایش قیمت یک کالا با ثابت بودن سایر عوامل چه اثری بر مقدار تقاضای آن دارد؟",
        "options": [
            "کاهش مقدار تقاضا",
            "افزایش قطعی مقدار تقاضا",
            "بدون هیچ رابطه‌ای",
            "همیشه دو برابر شدن تقاضا",
        ],
        "correct": 0,
        "explanation": "طبق قانون تقاضا، با ثابت بودن سایر شرایط، افزایش قیمت معمولاً با کاهش مقدار تقاضا همراه است.",
    },
    {
        "category": "💰 اقتصاد",
        "question": "تورم به طور کلی به چه معناست؟",
        "options": [
            "افزایش مستمر سطح عمومی قیمت‌ها",
            "کاهش یک‌باره قیمت یک کالا",
            "افزایش تولید یک بنگاه",
            "کاهش نرخ بیکاری",
        ],
        "correct": 0,
        "explanation": "تورم به افزایش مداوم سطح عمومی قیمت‌ها و کاهش قدرت خرید پول اشاره دارد.",
    },
    {
        "category": "👔 مدیریت",
        "question": "کدام مورد یکی از وظایف اصلی مدیریت است؟",
        "options": [
            "برنامه‌ریزی",
            "حذف کامل کنترل",
            "نادیده گرفتن منابع",
            "حذف تصمیم‌گیری",
        ],
        "correct": 0,
        "explanation": "برنامه‌ریزی، سازماندهی، هدایت و کنترل از کارکردهای کلاسیک مدیریت هستند.",
    },
    {
        "category": "👔 مدیریت",
        "question": "اثربخشی بیشتر به کدام مفهوم نزدیک است؟",
        "options": [
            "دستیابی به اهداف",
            "صرفاً کاهش هزینه",
            "افزایش تعداد کارکنان",
            "افزایش حجم اسناد",
        ],
        "correct": 0,
        "explanation": "اثربخشی بر میزان تحقق اهداف تمرکز دارد؛ کارایی بیشتر به نسبت خروجی به منابع مربوط است.",
    },
    {
        "category": "📒 حسابداری",
        "question": "کدام رابطه پایه‌ای در حسابداری صحیح است؟",
        "options": [
            "دارایی = بدهی + حقوق مالکانه",
            "دارایی = درآمد + هزینه",
            "بدهی = دارایی + حقوق مالکانه",
            "هزینه = دارایی + بدهی",
        ],
        "correct": 0,
        "explanation": "معادله اساسی حسابداری رابطه میان دارایی‌ها، بدهی‌ها و حقوق مالکانه را نشان می‌دهد.",
    },
    {
        "category": "📒 حسابداری",
        "question": "صورت وضعیت مالی معمولاً چه چیزی را در یک تاریخ مشخص نشان می‌دهد؟",
        "options": [
            "دارایی‌ها، بدهی‌ها و حقوق مالکانه",
            "فقط فروش ماهانه",
            "فقط هزینه حقوق",
            "فقط جریان وجوه نقد",
        ],
        "correct": 0,
        "explanation": "صورت وضعیت مالی تصویر وضعیت مالی واحد اقتصادی در یک تاریخ معین است.",
    },
    {
        "category": "⚖️ قوانین و مقررات",
        "question": "در امور بانکی، رعایت مقررات مبارزه با پولشویی بیشتر با کدام هدف مرتبط است؟",
        "options": [
            "شناسایی و کاهش ریسک استفاده مجرمانه از نظام مالی",
            "افزایش تبلیغات بانکی",
            "افزایش تعداد دستگاه‌های خودپرداز",
            "کاهش آموزش کارکنان",
        ],
        "correct": 0,
        "explanation": "مقررات AML برای کاهش ریسک سوءاستفاده از نظام مالی و شناسایی فعالیت‌های مشکوک طراحی شده‌اند.",
    },
    {
        "category": "🧠 هوش",
        "question": "اگر الگوی دنباله 2، 4، 8، 16 ادامه یابد، عدد بعدی چیست؟",
        "options": ["24", "32", "30", "36"],
        "correct": 1,
        "explanation": "هر عدد دو برابر عدد قبلی است؛ بنابراین عدد بعدی 32 است.",
    },
    {
        "category": "🧠 هوش",
        "question": "اگر همه Aها، B باشند و هیچ Bای C نباشد، کدام نتیجه قطعی است؟",
        "options": [
            "هیچ Aای C نیست",
            "همه Cها A هستند",
            "همه Bها A هستند",
            "هیچ Aای B نیست",
        ],
        "correct": 0,
        "explanation": "اگر A زیرمجموعه B باشد و B با C اشتراک نداشته باشد، A نیز با C اشتراک نخواهد داشت.",
    },
    {
        "category": "🇬🇧 زبان انگلیسی",
        "question": "Choose the correct option: 'The bank ___ the report yesterday.'",
        "options": ["complete", "completed", "completing", "has complete"],
        "correct": 1,
        "explanation": "با قید yesterday از گذشته ساده استفاده می‌شود: completed.",
    },
    {
        "category": "🇬🇧 زبان انگلیسی",
        "question": "The closest meaning of 'reliable' is:",
        "options": ["uncertain", "trustworthy", "expensive", "temporary"],
        "correct": 1,
        "explanation": "Reliable یعنی قابل اعتماد؛ نزدیک‌ترین گزینه trustworthy است.",
    },
    {
        "category": "💻 فناوری اطلاعات",
        "question": "کدام گزینه برای احراز هویت چندعاملی نمونه مناسبی است؟",
        "options": [
            "رمز عبور + کد یک‌بارمصرف",
            "دو بار وارد کردن رمز عبور یکسان",
            "نام کاربری بدون رمز",
            "فقط نام خانوادگی",
        ],
        "correct": 0,
        "explanation": "احراز هویت چندعاملی از بیش از یک عامل برای افزایش امنیت استفاده می‌کند.",
    },
    {
        "category": "💻 فناوری اطلاعات",
        "question": "Phishing معمولاً به چه نوع حمله‌ای گفته می‌شود؟",
        "options": [
            "فریب کاربر برای افشای اطلاعات",
            "افزایش سرعت اینترنت",
            "فشرده‌سازی فایل",
            "پشتیبان‌گیری خودکار",
        ],
        "correct": 0,
        "explanation": "فیشینگ با جعل هویت یا پیام‌های فریبنده تلاش می‌کند اطلاعات حساس کاربر را به دست آورد.",
    },
    {
        "category": "🏦 بانکداری",
        "question": "ریسک اعتباری به طور کلی به چه چیزی اشاره دارد؟",
        "options": [
            "احتمال عدم ایفای تعهد توسط طرف مقابل",
            "احتمال قطعی برق شعبه",
            "افزایش هزینه تبلیغات",
            "تغییر طراحی شعبه",
        ],
        "correct": 0,
        "explanation": "ریسک اعتباری از احتمال عدم ایفای تعهدات مالی توسط وام‌گیرنده یا طرف مقابل ناشی می‌شود.",
    },
    {
        "category": "📊 تحلیل داده",
        "question": "میانگین اعداد 10، 20 و 30 چند است؟",
        "options": ["15", "20", "25", "30"],
        "correct": 1,
        "explanation": "مجموع 60 است و با تقسیم بر 3، میانگین برابر 20 می‌شود.",
    },
    {
        "category": "🎯 آزمون استخدامی",
        "question": "در آزمون زمان‌دار، اگر یک سؤال بسیار دشوار باشد، راهبرد مناسب‌تر چیست؟",
        "options": [
            "مدیریت زمان و عبور موقت از سؤال",
            "صرف کل زمان آزمون روی همان سؤال",
            "پاسخ تصادفی به همه سؤالات",
            "ترک کامل آزمون",
        ],
        "correct": 0,
        "explanation": "در آزمون زمان‌دار، مدیریت زمان و برگشت به سؤالات دشوار در پایان معمولاً راهبرد مناسب‌تری است.",
    },
    {
        "category": "🎯 آزمون استخدامی",
        "question": "بهترین معیار برای تشخیص نقطه ضعف مطالعاتی چیست؟",
        "options": [
            "تحلیل منظم پاسخ‌های غلط و درصد هر مبحث",
            "فقط تعداد صفحات مطالعه‌شده",
            "فقط زمان حضور در کتابخانه",
            "تعداد پیام‌های آموزشی",
        ],
        "correct": 0,
        "explanation": "تحلیل پاسخ‌های غلط و عملکرد تفکیک‌شده بر اساس مبحث، تصویر دقیق‌تری از نقاط ضعف می‌دهد.",
    },
]

EMPLOYMENT_EXAM_SESSIONS = {}


def employment_exam_menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("5️⃣ ۵ سؤال", callback_data="employment_count_5"),
            InlineKeyboardButton("🔟 ۱۰ سؤال", callback_data="employment_count_10"),
        ],
        [
            InlineKeyboardButton("1️⃣5️⃣ ۱۵ سؤال", callback_data="employment_count_15"),
            InlineKeyboardButton("🎲 تصادفی", callback_data="employment_count_random"),
        ],
        [
            InlineKeyboardButton("🏠 منوی اصلی", callback_data="home"),
        ],
    ])


def employment_exam_intro_text():
    return f"""
📝 <b>آزمون استخدامی تخصصی</b>
{SEPARATOR}

🎯 بانک تمرینی چندحوزه‌ای:
🏦 بانکداری
💰 اقتصاد
👔 مدیریت
📒 حسابداری
⚖️ قوانین و مقررات
🧠 هوش
🇬🇧 زبان
💻 فناوری اطلاعات

{SEPARATOR}
🔀 سوالات هر آزمون به‌صورت تصادفی انتخاب می‌شوند.
📊 در پایان، امتیاز و درصد نمایش داده می‌شود.
💡 برای هر پاسخ، توضیح کوتاه ارائه می‌شود.

⚠️ این سوالات تمرینی‌اند و جایگزین دفترچه رسمی هیچ فراخوانی نیستند.

👇 تعداد سوالات را انتخاب کنید:
"""


def employment_exam_start(user_id, count=10, bank_key="general"):
    questions = list(EMPLOYMENT_QUESTIONS)
    random.shuffle(questions)

    if count == "random":
        count = min(random.randint(5, 15), len(questions))
    count = min(int(count), len(questions))

    EMPLOYMENT_EXAM_SESSIONS[user_id] = {
        "questions": questions[:count],
        "current": 0,
        "score": 0,
        "bank_key": bank_key,
    }


def employment_exam_question(user_id):
    session = EMPLOYMENT_EXAM_SESSIONS.get(user_id)
    if not session:
        return "❌ آزمون فعالی برای شما پیدا نشد.", employment_exam_menu()

    q = session["questions"][session["current"]]
    n = session["current"] + 1
    total = len(session["questions"])

    keyboard = []
    for i, option in enumerate(q["options"]):
        keyboard.append([
            InlineKeyboardButton(
                f"{chr(65+i)}) {option}",
                callback_data=f"employment_answer_{session['current']}_{i}",
            )
        ])

    keyboard.append([
        InlineKeyboardButton("🏠 منوی اصلی", callback_data="home"),
    ])

    text = f"""
📝 <b>آزمون استخدامی</b>
━━━━━━━━━━━━━━━━━━

📌 سؤال {n} از {total}
🏷️ {q["category"]}

❓ {q["question"]}

━━━━━━━━━━━━━━━━━━
⭐ امتیاز فعلی: {session["score"]}

👇 گزینه صحیح را انتخاب کنید:
"""
    return text, InlineKeyboardMarkup(keyboard)


def employment_exam_answer(user_id, selected):
    session = EMPLOYMENT_EXAM_SESSIONS.get(user_id)
    if not session:
        return None

    q = session["questions"][session["current"]]
    correct = q["correct"]

    if selected == correct:
        session["score"] += 1
        result = f"✅ صحیح!\n💡 {q['explanation']}"
    else:
        result = (
            f"❌ نادرست.\n"
            f"✅ پاسخ صحیح: {q['options'][correct]}\n"
            f"💡 {q['explanation']}"
        )

    session["current"] += 1

    if session["current"] >= len(session["questions"]):
        total = len(session["questions"])
        score = session["score"]
        percentage = round(score / total * 100)

        if percentage >= 80:
            level = "🏆 عالی"
        elif percentage >= 60:
            level = "🟢 خوب"
        elif percentage >= 40:
            level = "🟡 متوسط"
        else:
            level = "🔴 نیازمند تقویت"

        del EMPLOYMENT_EXAM_SESSIONS[user_id]

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔄 آزمون مجدد", callback_data="employment_exam"),
            ],
            [
                InlineKeyboardButton("🎯 مرکز استخدامی", callback_data="employment"),
            ],
            [
                InlineKeyboardButton("🏠 منوی اصلی", callback_data="home"),
            ],
        ])

        return (
            f"🏆 <b>آزمون به پایان رسید</b>\n"
            f"{SEPARATOR}\n"
            f"⭐ امتیاز: {score} از {total}\n"
            f"📊 درصد: {percentage}٪\n"
            f"🎯 سطح: {level}\n\n"
            f"{result}",
            keyboard,
        )

    text, keyboard = employment_exam_question(user_id)
    return f"{result}\n{SEPARATOR}\n{text}", keyboard
