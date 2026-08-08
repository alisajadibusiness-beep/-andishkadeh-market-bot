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
