from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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
                "📂 فایل و جزوات",
                callback_data="files"
            ),
            InlineKeyboardButton(
                "📱 شبکه‌های اجتماعی",
                callback_data="social"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def trade_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📘 آموزش تجارت بین‌الملل",
                callback_data="trade_learning"
            )
        ],
        [
            InlineKeyboardButton(
                "🚢 واردات و صادرات",
                callback_data="trade_import_export"
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
                "🌐 اینکوترمز",
                callback_data="trade_incoterms"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 پرداخت‌های بین‌المللی",
                callback_data="trade_payment"
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
                "📝 آزمون تجارت بین‌الملل",
                callback_data="trade_exam"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت به منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def back_to_home():
    keyboard = [
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
