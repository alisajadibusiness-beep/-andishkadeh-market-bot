# =========================================================
# 🎓 ANDISHKADEH - PROFESSIONAL EXAM ENGINE
# =========================================================
#
# Central exam engine
#
# امکانات:
# 🔀 سوالات تصادفی
# 🎯 آزمون موضوعی
# 🏆 آزمون جامع
# 📊 محاسبه درصد
# ⭐ امتیاز
# 💡 پاسخ صحیح
# 👤 Session مستقل برای هر کاربر
# 🔄 آزمون مجدد
#
# =========================================================
import random
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
# =========================================================
# QUESTION BANKS
# =========================================================
from management import QUESTIONS as MANAGEMENT_QUESTIONS
from trade import TRADE_QUESTIONS
from marketing import MARKETING_QUESTIONS
from economy import ECONOMY_QUESTIONS
from banking import (
    BANKING_QUESTIONS,
    BANKING_FULL_EXAM_QUESTIONS,
)
# =========================================================
# CONSTANTS
# =========================================================
SEPARATOR = "━━━━━━━━━━━━━━━━━━"
DEFAULT_QUESTION_COUNT = 5
MIN_QUESTION_COUNT = 3
MAX_QUESTION_COUNT = 20
# =========================================================
# EXAM DATABASE
# =========================================================
EXAM_DATABASE = {
    "management": {
        "title": "📚 مدیریت",
        "questions": MANAGEMENT_QUESTIONS,
    },
    "trade": {
        "title": "🌍 تجارت بین‌الملل",
        "questions": TRADE_QUESTIONS,
    },
    "marketing": {
        "title": "📈 بازاریابی و فروش",
        "questions": MARKETING_QUESTIONS,
    },
    "economy": {
        "title": "💰 اقتصاد و بازار",
        "questions": ECONOMY_QUESTIONS,
    },
    "banking": {
        "title": "🏦 بانکداری",
        "questions": BANKING_QUESTIONS,
    },
    "banking_full": {
        "title": "🏆 آزمون جامع بانکداری",
        "questions": BANKING_FULL_EXAM_QUESTIONS,
    },
}
# =========================================================
# USER EXAM SESSIONS
# =========================================================
# ساختار:
#
# user_id: {
#     "exam": "management",
#     "questions": [...],
#     "current": 0,
#     "score": 0,
#     "correct": 0,
#     "wrong": 0,
#     "started_at": timestamp,
#     "question_count": 5,
#     "answered": False,
# }
USER_SESSIONS = {}
# =========================================================
# USER STATISTICS
# =========================================================
USER_STATS = {}
def get_user_stats(user_id):
    if user_id not in USER_STATS:
        USER_STATS[user_id] = {
            "exams": 0,
            "questions": 0,
            "correct": 0,
            "wrong": 0,
            "total_score": 0,
            "best_percentage": 0,
        }
    return USER_STATS[user_id]
# =========================================================
# MAIN EXAM MENU
# =========================================================
def exams_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 مدیریت",
                callback_data="exam_management"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 تجارت بین‌الملل",
                callback_data="exam_trade"
            )
        ],
        [
            InlineKeyboardButton(
                "📈 بازاریابی و فروش",
                callback_data="exam_marketing"
            )
        ],
        [
            InlineKeyboardButton(
                "💰 اقتصاد و بازار",
                callback_data="exam_economics"
            )
        ],
        [
            InlineKeyboardButton(
                "🏦 بانکداری",
                callback_data="exam_banking"
            )
        ],
        [
            InlineKeyboardButton(
                "🏆 آزمون جامع بانکداری",
                callback_data="exam_banking_full"
            )
        ],
        [
            InlineKeyboardButton(
                "🎲 آزمون تصادفی",
                callback_data="exam_random"
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
# EXAM INTRO
# =========================================================
def exams_intro_text():
    return f"""
🎓 <b>مرکز آزمون اندیشکده</b>
اینجا فقط تست نمی‌زنید؛
بلکه میزان آمادگی واقعی خود را می‌سنجید.
{SEPARATOR}
📚 مدیریت
🌍 تجارت بین‌الملل
📈 بازاریابی و فروش
💰 اقتصاد و بازار
🏦 بانکداری
{SEPARATOR}
🎯 <b>ویژگی‌های آزمون</b>
🔀 سوالات تصادفی
📊 محاسبه درصد
⭐ امتیاز
🏆 سطح عملکرد
💡 نمایش پاسخ صحیح
📈 ثبت عملکرد کاربر
🔄 امکان آزمون مجدد
{SEPARATOR}
👇 حوزه آزمون را انتخاب کنید.
"""
# =========================================================
# QUESTION COUNT MENU
# =========================================================
def question_count_menu(exam_key):
    keyboard = [
        [
            InlineKeyboardButton(
                "5️⃣ ۵ سؤال",
                callback_data=f"count_{exam_key}_5"
            ),
            InlineKeyboardButton(
                "🔟 ۱۰ سؤال",
                callback_data=f"count_{exam_key}_10"
            ),
        ],
        [
            InlineKeyboardButton(
                "1️⃣5️⃣ ۱۵ سؤال",
                callback_data=f"count_{exam_key}_15"
            ),
            InlineKeyboardButton(
                "2️⃣0️⃣ ۲۰ سؤال",
                callback_data=f"count_{exam_key}_20"
            ),
        ],
        [
            InlineKeyboardButton(
                "🎲 تعداد تصادفی",
                callback_data=f"count_{exam_key}_random"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز آزمون",
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
    return InlineKeyboardMarkup(keyboard)
# =========================================================
# START EXAM MENU
# =========================================================
def exam_start_menu(exam_key):
    exam = EXAM_DATABASE.get(exam_key)
    if not exam:
        return exams_menu()
    total = len(exam["questions"])
    return question_count_menu(exam_key)
# =========================================================
# GET RANDOM QUESTIONS
# =========================================================
def prepare_questions(exam_key, count):
    exam = EXAM_DATABASE.get(exam_key)
    if not exam:
        return []
    questions = list(exam["questions"])
    if not questions:
        return []
    random.shuffle(questions)
    if count == "random":
        count = min(
            random.randint(
                MIN_QUESTION_COUNT,
                min(
                    MAX_QUESTION_COUNT,
                    len(questions)
                )
            ),
            len(questions)
        )
    else:
        count = int(count)
        count = min(
            count,
            len(questions)
        )
    selected = questions[:count]
    # کپی مستقل از سوالات
    result = []
    for question in selected:
        copied = {
            "question": question["question"],
            "options": list(question["options"]),
            "correct": question["correct"],
        }
        result.append(copied)
    return result
# =========================================================
# CREATE SESSION
# =========================================================
def create_exam_session(
    user_id,
    exam_key,
    count
):
    questions = prepare_questions(
        exam_key,
        count
    )
    if not questions:
        return None
    USER_SESSIONS[user_id] = {
        "exam": exam_key,
        "questions": questions,
        "current": 0,
        "score": 0,
        "correct": 0,
        "wrong": 0,
        "started_at": time.time(),
        "question_count": len(questions),
        "answered": False,
    }
    return USER_SESSIONS[user_id]
# =========================================================
# CURRENT SESSION
# =========================================================
def get_session(user_id):
    return USER_SESSIONS.get(user_id)
# =========================================================
# DELETE SESSION
# =========================================================
def clear_session(user_id):
    USER_SESSIONS.pop(
        user_id,
        None
    )
# =========================================================
# FORMAT QUESTION
# =========================================================
def format_question(
    user_id,
    question,
    current,
    total,
    score
):
    session = get_session(user_id)
    exam_key = session["exam"]
    title = EXAM_DATABASE[
        exam_key
    ]["title"]
    text = f"""
{title}
{SEPARATOR}
📝 <b>سؤال {current + 1} از {total}</b>
⭐ امتیاز فعلی: <b>{score}</b>
{SEPARATOR}
<b>{question["question"]}</b>
{SEPARATOR}
👇 <b>گزینه صحیح را انتخاب کنید:</b>
"""
    keyboard = []
    letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
    ]
    for i, option in enumerate(
        question["options"]
    ):
        keyboard.append(
            [
                InlineKeyboardButton(
                    f"{letters[i]}) {option}",
                    callback_data=(
                        f"answer_{user_id}_{i}"
                    )
                )
            ]
        )
    keyboard.append(
        [
            InlineKeyboardButton(
                "❌ خروج از آزمون",
                callback_data="exam_exit"
            )
        ]
    )
    return (
        text,
        InlineKeyboardMarkup(keyboard)
    )
# =========================================================
# START FIRST QUESTION
# =========================================================
def start_question(
    user_id,
    exam_key,
    count
):
    session = create_exam_session(
        user_id,
        exam_key,
        count
    )
    if not session:
        return (
            "⚠️ برای این آزمون سؤال کافی وجود ندارد.",
            exams_menu()
        )
    question = session[
        "questions"
    ][0]
    return format_question(
        user_id,
        question,
        0,
        session["question_count"],
        0
    )
# =========================================================
# ANSWER QUESTION
# =========================================================
def process_answer(
    user_id,
    selected_answer
):
    session = get_session(user_id)
    if not session:
        return {
            "status": "no_session"
        }
    if session["answered"]:
        return {
            "status": "already_answered"
        }
    current = session["current"]
    questions = session["questions"]
    if current >= len(questions):
        return {
            "status": "finished"
        }
    question = questions[current]
    correct_answer = question["correct"]
    session["answered"] = True
    is_correct = (
        selected_answer
        == correct_answer
    )
    if is_correct:
        session["score"] += 1
        session["correct"] += 1
    else:
        session["wrong"] += 1
    return {
        "status": "answered",
        "correct": is_correct,
        "correct_index": correct_answer,
        "correct_text": question["options"][
            correct_answer
        ],
        "question": question,
    }
# =========================================================
# NEXT QUESTION
# =========================================================
def next_question(user_id):
    session = get_session(user_id)
    if not session:
        return None
    session["current"] += 1
    session["answered"] = False
    current = session["current"]
    questions = session["questions"]
    if current >= len(questions):
        return None
    return format_question(
        user_id,
        questions[current],
        current,
        session["question_count"],
        session["score"]
    )
# =========================================================
# RESULT CALCULATION
# =========================================================
def calculate_result(
    user_id
):
    session = get_session(user_id)
    if not session:
        return None
    total = session[
        "question_count"
    ]
    correct = session[
        "correct"
    ]
    wrong = session[
        "wrong"
    ]
    percentage = (
        round(
            (correct / total) * 100
        )
        if total
        else 0
    )
    elapsed = int(
        time.time()
        - session["started_at"]
    )
    stats = get_user_stats(
        user_id
    )
    stats["exams"] += 1
    stats["questions"] += total
    stats["correct"] += correct
    stats["wrong"] += wrong
    stats["total_score"] += correct
    stats["best_percentage"] = max(
        stats["best_percentage"],
        percentage
    )
    return {
        "exam": session["exam"],
        "total": total,
        "correct": correct,
        "wrong": wrong,
        "percentage": percentage,
        "elapsed": elapsed,
    }
# =========================================================
# PERFORMANCE LEVEL
# =========================================================
def performance_level(
    percentage
):
    if percentage >= 90:
        return (
            "🏆 استاد",
            "تسلط بسیار بالا"
        )
    if percentage >= 80:
        return (
            "🔥 حرفه‌ای",
            "آمادگی بسیار خوب"
        )
    if percentage >= 70:
        return (
            "⭐ خوب",
            "سطح مناسب"
        )
    if percentage >= 50:
        return (
            "📚 متوسط",
            "نیازمند مرور و تمرین"
        )
    return (
        "🔄 نیازمند تقویت",
        "پیشنهاد می‌شود درسنامه را مرور کنید"
    )
# =========================================================
# RESULT TEXT
# =========================================================
def result_text(
    user_id,
    result
):
    title = EXAM_DATABASE[
        result["exam"]
    ]["title"]
    level, description = (
        performance_level(
            result["percentage"]
        )
    )
    minutes = (
        result["elapsed"]
        // 60
    )
    seconds = (
        result["elapsed"]
        % 60
    )
    return f"""
🏆 <b>نتیجه آزمون</b>
{title}
{SEPARATOR}
🎯 تعداد سؤالات:
<b>{result["total"]}</b>
✅ پاسخ صحیح:
<b>{result["correct"]}</b>
❌ پاسخ غلط:
<b>{result["wrong"]}</b>
📊 درصد:
<b>{result["percentage"]}٪</b>
🏅 سطح عملکرد:
<b>{level}</b>
⏱️ زمان:
<b>{minutes:02d}:{seconds:02d}</b>
{SEPARATOR}
💡 <b>ارزیابی:</b>
{description}
{SEPARATOR}
📌 <b>تحلیل کوتاه:</b>
{
    "عملکرد عالی؛ آماده ورود به آزمون‌های سخت‌تر هستید."
    if result["percentage"] >= 90
    else
    "عملکرد خوب است؛ با مرور اشتباهات می‌توانید درصد را بالاتر ببرید."
    if result["percentage"] >= 70
    else
    "پیشنهاد می‌شود ابتدا درسنامه مرتبط را مرور کرده و سپس آزمون را تکرار کنید."
}
"""
# =========================================================
# RESULT MENU
# =========================================================
def result_menu(
    exam_key
):
    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 آزمون مجدد",
                callback_data=f"restart_{exam_key}"
            )
        ],
        [
            InlineKeyboardButton(
                "🎓 مرکز آزمون",
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
    return InlineKeyboardMarkup(
        keyboard
    )
# =========================================================
# EXAM SELECTION CALLBACK
# =========================================================
async def exam_selection_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    data = query.data
    mapping = {
        "exam_management":
            "management",
        "exam_trade":
            "trade",
        "exam_marketing":
            "marketing",
        "exam_economics":
            "economy",
        "exam_banking":
            "banking",
        "exam_banking_full":
            "banking_full",
    }
    exam_key = mapping.get(data)
    if not exam_key:
        return
    exam = EXAM_DATABASE[
        exam_key
    ]
    total = len(
        exam["questions"]
    )
    await query.edit_message_text(
        f"""
{exam["title"]}
{SEPARATOR}
📚 تعداد سوالات موجود:
<b>{total}</b>
🔀 سوالات آزمون به صورت تصادفی
انتخاب می‌شوند.
🎯 تعداد سوالات را انتخاب کنید:
""",
        reply_markup=question_count_menu(
            exam_key
        ),
        parse_mode="HTML",
    )
# =========================================================
# RANDOM EXAM
# =========================================================
async def random_exam_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton(
                "🎲 شروع آزمون تصادفی",
                callback_data="random_start"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 مرکز آزمون",
                callback_data="exams"
            )
        ],
    ]
    await query.edit_message_text(
        f"""
🎲 <b>آزمون تصادفی</b>
{SEPARATOR}
سیستم به صورت تصادفی یکی از
حوزه‌های تخصصی زیر را انتخاب می‌کند:
📚 مدیریت
🌍 تجارت
📈 بازاریابی
💰 اقتصاد
🏦 بانکداری
سپس سوالات به صورت تصادفی
برای شما انتخاب می‌شوند.
🎯 آماده‌ای؟
""",
        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),
        parse_mode="HTML",
    )
# =========================================================
# RANDOM START
# =========================================================
async def random_start_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    exam_key = random.choice(
        list(EXAM_DATABASE.keys())[
            :5
        ]
    )
    text, keyboard = start_question(
        user_id,
        exam_key,
        "random"
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# QUESTION COUNT CALLBACK
# =========================================================
async def question_count_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    if len(parts) != 3:
        return
    exam_key = parts[1]
    count = parts[2]
    user_id = query.from_user.id
    if exam_key not in EXAM_DATABASE:
        return
    if count != "random":
        try:
            count = int(count)
        except ValueError:
            return
    text, keyboard = start_question(
        user_id,
        exam_key,
        count
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# ANSWER CALLBACK
# =========================================================
async def answer_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split("_")
    if len(parts) != 3:
        return
    try:
        user_id = int(
            parts[1]
        )
        selected = int(
            parts[2]
        )
    except ValueError:
        return
    # امنیت: فقط صاحب Session
    if query.from_user.id != user_id:
        return
    result = process_answer(
        user_id,
        selected
    )
    if result["status"] == "no_session":
        await query.edit_message_text(
            "⚠️ آزمون فعالی برای شما وجود ندارد.",
            reply_markup=exams_menu()
        )
        return
    if result["status"] == "already_answered":
        await query.answer(
            "⚠️ این سؤال قبلاً پاسخ داده شده است.",
            show_alert=True
        )
        return
    question = result["question"]
    if result["correct"]:
        feedback = (
            "✅ <b>پاسخ صحیح!</b>\n\n"
            "🎯 امتیاز شما ثبت شد."
        )
    else:
        feedback = (
            "❌ <b>پاسخ اشتباه</b>\n\n"
            f"✅ پاسخ صحیح:\n"
            f"<b>{result['correct_text']}</b>"
        )
    keyboard = [
        [
            InlineKeyboardButton(
                "➡️ سؤال بعدی",
                callback_data="next_exam_question"
            )
        ],
        [
            InlineKeyboardButton(
                "❌ خروج از آزمون",
                callback_data="exam_exit"
            )
        ],
    ]
    await query.edit_message_text(
        f"""
{feedback}
{SEPARATOR}
💡 <b>سؤال:</b>
{question["question"]}
""",
        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),
        parse_mode="HTML",
    )
# =========================================================
# NEXT CALLBACK
# =========================================================
async def next_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    session = get_session(
        user_id
    )
    if not session:
        await query.edit_message_text(
            "⚠️ آزمون شما پیدا نشد.",
            reply_markup=exams_menu()
        )
        return
    next_data = next_question(
        user_id
    )
    if next_data is None:
        result = calculate_result(
            user_id
        )
        if not result:
            await query.edit_message_text(
                "⚠️ امکان محاسبه نتیجه وجود ندارد.",
                reply_markup=exams_menu()
            )
            return
        text = result_text(
            user_id,
            result
        )
        exam_key = result["exam"]
        clear_session(
            user_id
        )
        await query.edit_message_text(
            text,
            reply_markup=result_menu(
                exam_key
            ),
            parse_mode="HTML",
        )
        return
    text, keyboard = next_data
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# EXIT EXAM
# =========================================================
async def exit_exam_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    clear_session(
        user_id
    )
    await query.edit_message_text(
        """
🚪 <b>از آزمون خارج شدید.</b>
نتیجه این آزمون ثبت نشد.
هر زمان آماده بودید،
می‌توانید دوباره آزمون را شروع کنید.
""",
        reply_markup=exams_menu(),
        parse_mode="HTML",
    )
# =========================================================
# RESTART
# =========================================================
async def restart_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    parts = query.data.split(
        "_",
        1
    )
    if len(parts) != 2:
        return
    exam_key = parts[1]
    if exam_key not in EXAM_DATABASE:
        return
    user_id = query.from_user.id
    text, keyboard = start_question(
        user_id,
        exam_key,
        "random"
    )
    await query.edit_message_text(
        text,
        reply_markup=keyboard,
        parse_mode="HTML",
    )
# =========================================================
# PROFILE STATS
# =========================================================
async def profile_stats_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    stats = get_user_stats(
        user_id
    )
    questions = stats[
        "questions"
    ]
    correct = stats[
        "correct"
    ]
    percentage = (
        round(
            correct / questions * 100
        )
        if questions
        else 0
    )
    level, _ = performance_level(
        percentage
    )
    keyboard = [
        [
            InlineKeyboardButton(
                "🎓 مرکز آزمون",
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
        f"""
👤 <b>عملکرد من</b>
{SEPARATOR}
🎓 تعداد آزمون‌ها:
<b>{stats["exams"]}</b>
📝 تعداد سوالات:
<b>{questions}</b>
✅ پاسخ صحیح:
<b>{correct}</b>
❌ پاسخ غلط:
<b>{stats["wrong"]}</b>
📊 میانگین عملکرد:
<b>{percentage}٪</b>
🏆 بهترین رکورد:
<b>{stats["best_percentage"]}٪</b>
🎯 سطح فعلی:
<b>{level}</b>
{SEPARATOR}
💡 با ادامه آزمون‌ها و مرور پاسخ‌های اشتباه،
سطح عملکرد خود را افزایش دهید.
""",
        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),
        parse_mode="HTML",
    )
# =========================================================
# REGISTER HANDLERS
# =========================================================
def register_exam_handlers(
    application
):
    # ---------------------------------
    # MAIN EXAM MENU
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exams_callback,
            pattern=r"^exams$"
        )
    )
    # ---------------------------------
    # EXAM SELECTION
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exam_selection_callback,
            pattern=(
                r"^exam_"
                r"(management|trade|marketing|"
                r"economics|banking|banking_full)$"
            )
        )
    )
    # ---------------------------------
    # RANDOM EXAM
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            random_exam_callback,
            pattern=r"^exam_random$"
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            random_start_callback,
            pattern=r"^random_start$"
        )
    )
    # ---------------------------------
    # QUESTION COUNT
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            question_count_callback,
            pattern=r"^count_.+_(5|10|15|20|random)$"
        )
    )
    # ---------------------------------
    # ANSWER
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            answer_callback,
            pattern=r"^answer_\d+_\d+$"
        )
    )
    # ---------------------------------
    # NEXT QUESTION
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            next_callback,
            pattern=r"^next_exam_question$"
        )
    )
    # ---------------------------------
    # EXIT
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            exit_exam_callback,
            pattern=r"^exam_exit$"
        )
    )
    # ---------------------------------
    # RESTART
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            restart_callback,
            pattern=r"^restart_.+$"
        )
    )
    # ---------------------------------
    # PROFILE
    # ---------------------------------
    application.add_handler(
        CallbackQueryHandler(
            profile_stats_callback,
            pattern=r"^profile_stats$"
        )
    )
# =========================================================
# MAIN EXAMS CALLBACK
# =========================================================
async def exams_callback(
    update,
    context
):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        exams_intro_text(),
        reply_markup=exams_menu(),
        parse_mode="HTML",
    )
# =========================================================
# END
# =========================================================
