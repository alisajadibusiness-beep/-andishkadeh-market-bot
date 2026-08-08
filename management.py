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
                callback_data="management"
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
