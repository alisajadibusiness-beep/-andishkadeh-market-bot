from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def management_basics_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📖 تعریف و مفهوم مدیریت",
                callback_data="management_definition"
            )
        ],
        [
            InlineKeyboardButton(
                "🎯 وظایف اصلی مدیریت",
                callback_data="management_functions"
            )
        ],
        [
            InlineKeyboardButton(
                "🏢 سطوح مدیریت",
                callback_data="management_levels"
            )
        ],
        [
            InlineKeyboardButton(
                "👤 نقش‌های مدیر",
                callback_data="management_roles"
            )
        ],
        [
            InlineKeyboardButton(
                "🧩 مهارت‌های مدیریتی",
                callback_data="management_skills"
            )
        ],
        [
            InlineKeyboardButton(
                "⚙️ کارایی و اثربخشی",
                callback_data="efficiency_effectiveness"
            )
        ],
        [
            InlineKeyboardButton(
                "🧠 مکاتب مدیریت",
                callback_data="management_schools"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 آزمون مبانی مدیریت",
                callback_data="management_basics_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="management"
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
def management_definition_text():
    return """
📖 تعریف و مفهوم مدیریت
مدیریت فرآیندی است که طی آن مدیر با استفاده از منابع انسانی، مالی، اطلاعاتی و فیزیکی، فعالیت‌های سازمان را برای دستیابی به اهداف مشخص برنامه‌ریزی و هدایت می‌کند.
🎯 هدف اصلی مدیریت
هدف مدیریت این است که منابع سازمان به شکلی مناسب استفاده شوند تا سازمان بتواند با کمترین اتلاف و بیشترین نتیجه به اهداف خود برسد.
⚙️ چهار وظیفه اصلی مدیریت
1️⃣ برنامه‌ریزی
تعیین اهداف و مشخص کردن مسیر رسیدن به آنها.
2️⃣ سازماندهی
تقسیم وظایف، تعیین مسئولیت‌ها و ایجاد ساختار مناسب.
3️⃣ رهبری و هدایت
ایجاد انگیزه و هدایت کارکنان برای انجام بهتر وظایف.
4️⃣ کنترل
مقایسه عملکرد واقعی با اهداف و اصلاح انحرافات.
📌 نکته مهم آزمونی
چهار وظیفه کلاسیک مدیریت عبارت‌اند از:
برنامه‌ریزی ← سازماندهی ← رهبری ← کنترل
💡 مثال کاربردی
فرض کنید یک فروشگاه قصد دارد فروش خود را افزایش دهد.
ابتدا هدف فروش مشخص می‌شود.
سپس وظایف کارکنان تقسیم می‌شود.
مدیر کارکنان را هدایت و انگیزه‌دهی می‌کند.
در نهایت میزان فروش بررسی و با هدف تعیین‌شده مقایسه می‌شود.
📚 نتیجه
مدیریت فقط «دستور دادن» نیست؛ بلکه فرآیندی برای استفاده صحیح از منابع و هماهنگ کردن فعالیت‌ها جهت رسیدن به اهداف سازمان است.
"""
def management_definition_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📝 آزمون این درس",
                callback_data="management_definition_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت به مبانی مدیریت",
                callback_data="management_basics"
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
# =========================
# آزمون مبانی مدیریت
# =========================
QUESTIONS = [
    {
        "question": "مدیریت چیست؟",
        "options": [
            "فقط نظارت بر کارکنان",
            "هماهنگی منابع برای دستیابی به اهداف",
            "فقط برنامه‌ریزی مالی",
            "فقط کنترل عملکرد کارکنان",
        ],
        "correct": 1,
    },
    {
        "question": "کدام گزینه یکی از وظایف اصلی مدیریت است؟",
        "options": [
            "برنامه‌ریزی",
            "تبلیغات",
            "حسابداری",
            "فروش",
        ],
        "correct": 0,
    },
    {
        "question": "کدام وظیفه مدیریت به تعیین اهداف و مسیر رسیدن به آنها مربوط است؟",
        "options": [
            "کنترل",
            "رهبری",
            "برنامه‌ریزی",
            "سازماندهی",
        ],
        "correct": 2,
    },
    {
        "question": "مقایسه عملکرد واقعی با اهداف تعیین‌شده مربوط به کدام وظیفه مدیریت است؟",
        "options": [
            "برنامه‌ریزی",
            "سازماندهی",
            "رهبری",
            "کنترل",
        ],
        "correct": 3,
    },
    {
        "question": "کدام گزینه بهترین تعریف برای سازماندهی است؟",
        "options": [
            "تعیین اهداف سازمان",
            "تقسیم وظایف و تعیین مسئولیت‌ها",
            "ایجاد انگیزه در کارکنان",
            "مقایسه عملکرد با اهداف",
        ],
        "correct": 1,
    },
]
def exam_question(index, score=0):
    question = QUESTIONS[index]
    keyboard = []
    for i, option in enumerate(question["options"]):
        keyboard.append(
            [
                InlineKeyboardButton(
                    f"{chr(65 + i)}) {option}",
                    callback_data=f"mg_answer_{index}_{i}_{score}"
                )
            ]
        )
    keyboard.append(
        [
            InlineKeyboardButton(
                "❌ خروج از آزمون",
                callback_data="management_basics"
            )
        ]
    )
    text = f"""
📝 آزمون مبانی مدیریت
سؤال {index + 1} از {len(QUESTIONS)}
{question["question"]}
لطفاً پاسخ صحیح را انتخاب کنید:
"""
    return text, InlineKeyboardMarkup(keyboard)
