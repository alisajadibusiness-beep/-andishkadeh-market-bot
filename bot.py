import os
import random
import sqlite3
import time
from datetime import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# ============================================================
# ربات حرفه‌ای آموزش و آزمون استخدامی بانک‌ها
# نیازمندی: python-telegram-bot >= 20
# توکن را در متغیر محیطی BOT_TOKEN قرار دهید.
# ============================================================

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DB_PATH = os.getenv("BOT_DB", "bank_exam_bot.db")

SUBJECTS = {
    "banking": ("🏦 بانکداری", "بانکداری و عملیات بانکی"),
    "laws": ("⚖️ قوانین بانکی", "قوانین و مقررات بانکی"),
    "economy": ("💰 اقتصاد", "اقتصاد و بازار"),
    "management": ("📊 مدیریت", "مبانی مدیریت"),
    "accounting": ("🧾 حسابداری", "اصول حسابداری"),
    "finance": ("📈 مدیریت مالی", "مدیریت مالی"),
    "marketing": ("📣 بازاریابی", "بازاریابی و فروش"),
    "trade": ("🌍 تجارت بین‌الملل", "تجارت بین‌الملل"),
    "iq": ("🧠 هوش", "هوش و استعداد"),
    "english": ("🇬🇧 زبان", "زبان انگلیسی"),
    "icdl": ("💻 ICDL", "مهارت‌های ICDL"),
}

QUESTIONS = [
    # banking
    ("banking", "مهم‌ترین وظیفه بانک تجاری چیست؟", ["جذب سپرده و اعطای تسهیلات", "تولید کالا", "تعیین مالیات", "صدور شناسنامه"], 0, "بانک‌های تجاری عمدتاً منابع را جذب و در قالب تسهیلات در اختیار متقاضیان قرار می‌دهند."),
    ("banking", "سپرده دیداری معمولاً چه ویژگی دارد؟", ["قابل برداشت طبق شرایط حساب", "فقط برای ده سال", "غیرقابل برداشت", "فقط برای دولت"], 0, "سپرده دیداری برای انجام پرداخت‌ها و برداشت طبق مقررات حساب قابل استفاده است."),
    ("banking", "اعتبارسنجی مشتری با چه هدفی انجام می‌شود؟", ["ارزیابی توان و ریسک بازپرداخت", "افزایش مالیات", "تعیین نرخ ارز جهانی", "محاسبه تولید ناخالص داخلی"], 0, "اعتبارسنجی برای ارزیابی ریسک اعتباری و توان بازپرداخت مشتری کاربرد دارد."),

    # laws
    ("laws", "قانون عملیات بانکی بدون ربا بر چه موضوعی تمرکز دارد؟", ["چارچوب عملیات بانکی منطبق با موازین مربوط", "تعیین قیمت خودرو", "قوانین رانندگی", "مالیات بر ارزش افزوده"], 0, "این قانون چارچوب عملیات بانکی بدون ربا و روابط مرتبط با آن را تعیین می‌کند."),
    ("laws", "پولشویی به طور کلی به چه معناست؟", ["پنهان یا مشروع‌نمایی منشأ عواید حاصل از جرم", "افزایش سرمایه بانک", "پرداخت حقوق کارکنان", "خرید سهام"], 0, "پولشویی فرایندی برای پنهان کردن منشأ غیرقانونی عواید و مشروع جلوه دادن آن است."),

    # economy
    ("economy", "هزینه فرصت چیست؟", ["ارزش بهترین گزینه از دست‌رفته", "کل هزینه تولید", "قیمت فروش", "مالیات"], 0, "هزینه فرصت ارزش بهترین گزینه‌ای است که به دلیل انتخاب گزینه دیگر از آن صرف‌نظر می‌کنیم."),
    ("economy", "در شرایط معمول، افزایش قیمت چه اثری بر مقدار تقاضا دارد؟", ["کاهش", "افزایش", "همیشه صفر", "بدون هیچ رابطه‌ای"], 0, "طبق قانون تقاضا، در شرایط معمول افزایش قیمت باعث کاهش مقدار تقاضا می‌شود."),
    ("economy", "تورم به کدام مفهوم نزدیک‌تر است؟", ["افزایش مستمر سطح عمومی قیمت‌ها", "کاهش یک قیمت خاص", "افزایش تولید", "کاهش بیکاری"], 0, "تورم افزایش عمومی و مستمر سطح قیمت‌ها در طول زمان است."),
    ("economy", "سیاست مالی بیشتر با کدام ابزارها مرتبط است؟", ["مالیات و مخارج دولت", "نرخ ارز جهانی", "تبلیغات", "بسته‌بندی"], 0, "سیاست مالی به تصمیمات دولت درباره درآمدها و مخارج عمومی مربوط است."),

    # management
    ("management", "کدام گزینه یکی از وظایف اصلی مدیریت است؟", ["برنامه‌ریزی", "تبلیغات", "خرید", "حسابداری"], 0, "چهار وظیفه کلاسیک مدیریت شامل برنامه‌ریزی، سازماندهی، رهبری و کنترل است."),
    ("management", "مقایسه عملکرد واقعی با اهداف مربوط به کدام وظیفه است؟", ["کنترل", "برنامه‌ریزی", "رهبری", "سازماندهی"], 0, "کنترل شامل سنجش عملکرد، مقایسه با معیارها و اصلاح انحرافات است."),
    ("management", "کدام مهارت در سطوح عالی مدیریت اهمیت بیشتری دارد؟", ["ادراکی", "فنی", "اجرایی", "حسابداری"], 0, "مهارت ادراکی برای درک سازمان به‌عنوان یک کل در سطوح عالی اهمیت بیشتری دارد."),

    # accounting
    ("accounting", "معادله اساسی حسابداری کدام است؟", ["دارایی = بدهی + سرمایه", "دارایی = درآمد - هزینه", "بدهی = دارایی + سرمایه", "سرمایه = هزینه + بدهی"], 0, "معادله اساسی حسابداری: دارایی برابر مجموع بدهی و سرمایه است."),
    ("accounting", "کدام مورد دارایی محسوب می‌شود؟", ["وجه نقد", "وام پرداختنی", "سرمایه", "درآمد"], 0, "وجه نقد یک منبع اقتصادی تحت کنترل واحد تجاری و در نتیجه دارایی است."),

    # finance
    ("finance", "ارزش زمانی پول بر چه ایده‌ای استوار است؟", ["پول امروز معمولاً ارزش متفاوتی از همان مبلغ در آینده دارد", "پول همیشه بی‌ارزش است", "تورم وجود ندارد", "ریسک همیشه صفر است"], 0, "به دلیل امکان سرمایه‌گذاری، ریسک و تورم، ارزش پول به زمان وابسته است."),
    ("finance", "رابطه ریسک و بازده در سرمایه‌گذاری معمولاً چگونه بیان می‌شود؟", ["ریسک بیشتر می‌تواند با بازده مورد انتظار بیشتر همراه باشد", "همیشه معکوس", "هیچ ارتباطی ندارد", "هر دو همیشه صفرند"], 0, "در تحلیل سرمایه‌گذاری، سرمایه‌گذار معمولاً برای پذیرش ریسک بیشتر بازده مورد انتظار بیشتری مطالبه می‌کند."),

    # marketing
    ("marketing", "کدام گزینه یکی از عناصر 4P است؟", ["Product", "Planning", "Performance", "People"], 0, "چهار عنصر کلاسیک 4P عبارت‌اند از Product، Price، Place و Promotion."),
    ("marketing", "در مدل STP حرف S نشان‌دهنده چیست؟", ["Segmentation", "Sales", "Strategy", "Service"], 0, "S در STP به معنای Segmentation یا بخش‌بندی بازار است."),
    ("marketing", "فروش حرفه‌ای بهتر است از چه چیزی آغاز شود؟", ["شناخت نیاز مشتری", "فشار برای خرید", "نادیده گرفتن اعتراض", "پایان مذاکره"], 0, "شناخت نیاز مشتری پایه ارائه راه‌حل مناسب و فروش حرفه‌ای است."),

    # trade
    ("trade", "صادرات به چه معناست؟", ["فروش کالا یا خدمات به خارج", "خرید کالا از خارج", "تولید داخلی", "حمل داخلی"], 0, "صادرات فروش کالا یا خدمات به بازار خارجی است."),
    ("trade", "کدام سند کشور مبدأ کالا را مشخص می‌کند؟", ["گواهی مبدأ", "بارنامه", "فاکتور تجاری", "پکینگ لیست"], 0, "Certificate of Origin کشور مبدأ کالا را مشخص می‌کند."),
    ("trade", "کدام قاعده اینکوترمز معمولاً بیشترین مسئولیت را برای فروشنده ایجاد می‌کند؟", ["DDP", "EXW", "FCA", "FOB"], 0, "در DDP فروشنده مسئول تحویل و انجام تشریفات واردات و پرداخت حقوق و عوارض طبق قاعده است."),

    # iq
    ("iq", "عدد بعدی را پیدا کنید: 2، 4، 8، 16، ؟", ["24", "30", "32", "36"], 2, "هر عدد دو برابر عدد قبلی است؛ بنابراین پاسخ 32 است."),
    ("iq", "اگر همه بانک‌ها سازمان باشند و بعضی سازمان‌ها دیجیتال باشند، کدام نتیجه قطعی است؟", ["همه بانک‌ها دیجیتال‌اند", "هیچ بانکی سازمان نیست", "بانک‌ها سازمان‌اند", "همه سازمان‌ها بانک‌اند"], 2, "از فرض اول فقط می‌توان نتیجه گرفت بانک‌ها در مجموعه سازمان‌ها قرار دارند."),
    ("iq", "کدام مورد با بقیه متفاوت است؟", ["مربع", "مثلث", "دایره", "کتاب"], 3, "سه مورد شکل هندسی‌اند و کتاب شکل هندسی نیست."),

    # english
    ("english", "Choose the correct option: She ___ to work every day.", ["go", "goes", "going", "gone"], 1, "برای فاعل سوم‌شخص مفرد در زمان حال ساده، فعل go به goes تبدیل می‌شود."),
    ("english", "The opposite of 'increase' is:", ["reduce", "improve", "grow", "raise"], 0, "reduce به معنی کاهش دادن/کاهش یافتن است."),

    # icdl
    ("icdl", "کدام نرم‌افزار برای کار با صفحات گسترده مناسب است؟", ["Excel", "Word", "PowerPoint", "Paint"], 0, "Microsoft Excel برای صفحات گسترده، محاسبات و تحلیل داده‌ها استفاده می‌شود."),
    ("icdl", "میانبر رایج Copy در ویندوز چیست؟", ["Ctrl+C", "Ctrl+V", "Ctrl+X", "Ctrl+Z"], 0, "Ctrl+C برای کپی کردن استفاده می‌شود."),
]

# ------------------------- Database -------------------------

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        level INTEGER DEFAULT 1,
        xp INTEGER DEFAULT 0,
        exams INTEGER DEFAULT 0,
        correct INTEGER DEFAULT 0,
        answered INTEGER DEFAULT 0,
        created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        total INTEGER,
        correct INTEGER,
        percent REAL,
        duration INTEGER,
        created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS mistakes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_index INTEGER,
        subject TEXT,
        created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        question TEXT,
        options TEXT,
        correct INTEGER,
        explanation TEXT
    );
    """)
    # Seed questions once.
    count = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    if count == 0:
        import json
        conn.executemany(
            "INSERT INTO questions(subject,question,options,correct,explanation) VALUES(?,?,?,?,?)",
            [(s, q, json.dumps(o, ensure_ascii=False), c, e) for s, q, o, c, e in QUESTIONS]
        )
    conn.commit()
    conn.close()

def ensure_user(tg_user):
    conn = db()
    conn.execute("""
        INSERT INTO users(user_id, first_name, username, created_at)
        VALUES(?,?,?,?,?)
        ON CONFLICT(user_id) DO UPDATE SET first_name=excluded.first_name, username=excluded.username
    """, (tg_user.id, tg_user.first_name or "", tg_user.username or "", datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = db()
    row = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    conn.close()
    return row

def add_xp(user_id, amount):
    conn = db()
    row = conn.execute("SELECT xp, level FROM users WHERE user_id=?", (user_id,)).fetchone()
    xp = (row["xp"] if row else 0) + amount
    level = max(1, min(10, 1 + xp // 100))
    conn.execute("UPDATE users SET xp=?, level=? WHERE user_id=?", (xp, level, user_id))
    conn.commit()
    conn.close()

def save_result(user_id, subject, total, correct, duration):
    percent = round((correct / total) * 100, 1) if total else 0
    conn = db()
    conn.execute(
        "INSERT INTO results(user_id,subject,total,correct,percent,duration,created_at) VALUES(?,?,?,?,?,?,?)",
        (user_id, subject, total, correct, percent, duration, datetime.now().isoformat())
    )
    conn.execute(
        "UPDATE users SET exams=exams+1, correct=correct+?, answered=answered+? WHERE user_id=?",
        (correct, total, user_id)
    )
    conn.commit()
    conn.close()
    add_xp(user_id, int(correct * 10))
    return percent

def save_mistake(user_id, qid, subject):
    conn = db()
    conn.execute(
        "INSERT INTO mistakes(user_id,question_index,subject,created_at) VALUES(?,?,?,?)",
        (user_id, qid, subject, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

# ------------------------- UI -------------------------

def btn(text, data):
    return InlineKeyboardButton(text, callback_data=data)

def main_menu():
    return InlineKeyboardMarkup([
        [btn("🎓 شروع مطالعه", "subjects"), btn("🏆 آزمون‌ها", "exams")],
        [btn("📊 کارنامه من", "profile"), btn("🎯 تحلیل عملکرد", "analytics")],
        [btn("❌ سوالات غلط", "mistakes"), btn("🎤 مصاحبه", "interview")],
        [btn("ℹ️ راهنما", "help")],
    ])

def subjects_menu():
    rows = []
    items = list(SUBJECTS.items())
    for i in range(0, len(items), 2):
        row = [btn(items[i][1][0], f"lesson:{items[i][0]}")]
        if i + 1 < len(items):
            row.append(btn(items[i+1][1][0], f"lesson:{items[i+1][0]}"))
        rows.append(row)
    rows.append([btn("🔙 بازگشت", "home")])
    return InlineKeyboardMarkup(rows)

def exams_menu():
    return InlineKeyboardMarkup([
        [btn("🎯 آزمون سریع 10 سؤالی", "exam:all:10")],
        [btn("🎲 آزمون تصادفی", "exam:random:10")],
        [btn("🏦 بانکداری", "exam:banking:5"), btn("⚖️ قوانین", "exam:laws:5")],
        [btn("💰 اقتصاد", "exam:economy:5"), btn("📊 مدیریت", "exam:management:5")],
        [btn("🧾 حسابداری", "exam:accounting:5"), btn("📈 مالی", "exam:finance:5")],
        [btn("📣 بازاریابی", "exam:marketing:5"), btn("🌍 تجارت", "exam:trade:5")],
        [btn("🧠 هوش", "exam:iq:5"), btn("🇬🇧 زبان", "exam:english:5")],
        [btn("💻 ICDL", "exam:icdl:5")],
        [btn("🔙 بازگشت", "home")],
    ])

def exam_session(context, user_id):
    return context.user_data.setdefault("exam", {})

# ------------------------- Handlers -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ensure_user(update.effective_user)
    await update.message.reply_text(
        "🚀 *مرکز حرفه‌ای آموزش و آزمون استخدامی بانک‌ها*\n\n"
        "از آموزش شروع کنید، تست بزنید و با تحلیل عملکرد سطح خود را ارتقا دهید.\n\n"
        "⭐ هر پاسخ صحیح = XP\n"
        "📊 عملکرد شما ذخیره و تحلیل می‌شود.",
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    ensure_user(query.from_user)
    data = query.data

    if data == "home":
        await query.edit_message_text(
            "🏠 *داشبورد اصلی*\n\nیک بخش را انتخاب کنید:",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )
    elif data == "subjects":
        await query.edit_message_text("📚 *دروس آموزشی*\n\nدرس موردنظر را انتخاب کنید:", parse_mode="Markdown", reply_markup=subjects_menu())
    elif data == "exams":
        await query.edit_message_text("🏆 *مرکز آزمون*\n\nنوع آزمون را انتخاب کنید:", parse_mode="Markdown", reply_markup=exams_menu())
    elif data == "profile":
        await show_profile(query)
    elif data == "analytics":
        await show_analytics(query)
    elif data == "mistakes":
        await show_mistakes(query)
    elif data == "help":
        await query.edit_message_text(
            "ℹ️ *راهنمای ربات*\n\n"
            "📚 درس بخوانید → 📝 آزمون بدهید → 📊 نتیجه را تحلیل کنید.\n"
            "هر آزمون امتیاز XP می‌دهد و سطح شما را بالا می‌برد.\n"
            "سؤالات غلط در بخش «سؤالات غلط» ذخیره می‌شوند.",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[btn("🔙 بازگشت", "home")]]),
        )
    elif data == "interview":
        await interview(query)
    elif data.startswith("lesson:"):
        await lesson(query, data.split(":", 1)[1])
    elif data.startswith("exam:"):
        await start_exam(query, context, data)
    elif data.startswith("answer:"):
        await answer_question(query, context, data)
    elif data == "next":
        await next_question(query, context)
    elif data == "finish":
        await finish_exam(query, context)
    elif data == "cancel_exam":
        context.user_data.pop("exam", None)
        await query.edit_message_text("❌ آزمون لغو شد.", reply_markup=main_menu())

async def show_profile(query):
    u = get_user(query.from_user.id)
    avg = round((u["correct"] / u["answered"]) * 100, 1) if u["answered"] else 0
    text = (
        f"👤 *پروفایل شما*\n\n"
        f"⭐ سطح: {u['level']}\n"
        f"✨ XP: {u['xp']}\n"
        f"🏆 تعداد آزمون: {u['exams']}\n"
        f"📝 پاسخ‌ها: {u['answered']}\n"
        f"✅ پاسخ صحیح: {u['correct']}\n"
        f"📊 میانگین: {avg}%"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[btn("🔙 بازگشت", "home")]]))

async def show_analytics(query):
    u = get_user(query.from_user.id)
    conn = db()
    rows = conn.execute(
        "SELECT subject, ROUND(AVG(percent),1) avgp, COUNT(*) n FROM results WHERE user_id=? GROUP BY subject ORDER BY avgp ASC",
        (query.from_user.id,),
    ).fetchall()
    conn.close()
    lines = ["🎯 *تحلیل عملکرد*\n"]
    if not rows:
        lines.append("هنوز آزمونی ثبت نشده است.")
    else:
        for r in rows:
            name = SUBJECTS.get(r["subject"], (r["subject"],))[0]
            lines.append(f"{name}: {r['avgp']}٪  ({r['n']} آزمون)")
        weak = rows[0]
        lines.append(f"\n⚠️ نقطه قابل بهبود: {SUBJECTS.get(weak['subject'], (weak['subject'],))[0]}")
        lines.append("💡 پیشنهاد: قبل از آزمون بعدی یک درسنامه کوتاه و ۱۰ تست آموزشی انجام دهید.")
    await query.edit_message_text("\n".join(lines), parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[btn("🔙 بازگشت", "home")]]))

async def show_mistakes(query):
    conn = db()
    rows = conn.execute(
        "SELECT subject, COUNT(*) n FROM mistakes WHERE user_id=? GROUP BY subject ORDER BY n DESC",
        (query.from_user.id,),
    ).fetchall()
    conn.close()
    if not rows:
        text = "❌ *سؤالات غلط*\n\nهنوز سؤال غلطی ثبت نشده است. عالی پیش می‌روید! 🎉"
    else:
        text = "❌ *سؤالات غلط*\n\n" + "\n".join(
            f"{SUBJECTS.get(r['subject'], (r['subject'],))[0]}: {r['n']} مورد" for r in rows
        )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([[btn("🔙 بازگشت", "home")]]))

LESSON_TEXT = {
    "banking": "🏦 *بانکداری*\n\nمبانی بانکداری، سپرده‌ها، تسهیلات، اعتبارات، خدمات بانکی و بانکداری الکترونیک را مطالعه کنید.\n\n⭐ نکته: اعتبارسنجی برای ارزیابی ریسک بازپرداخت مشتری اهمیت دارد.",
    "laws": "⚖️ *قوانین بانکی*\n\nموضوعات مهم شامل عملیات بانکی، چک، مبارزه با پولشویی و مقررات مرتبط با بانک‌هاست.\n\n⭐ نکته: در آزمون‌های واقعی، دفترچه رسمی همان دوره ملاک نهایی مواد آزمون است.",
    "economy": "💰 *اقتصاد*\n\nکمیابی، هزینه فرصت، عرضه و تقاضا، تورم، سیاست پولی و مالی و اقتصاد کلان از مباحث مهم هستند.\n\n⭐ حفظی: کمیابی → انتخاب → هزینه فرصت",
    "management": "📊 *مدیریت*\n\nچهار وظیفه کلاسیک: برنامه‌ریزی، سازماندهی، رهبری و کنترل.\n\n⭐ نکته: مهارت ادراکی در سطوح عالی مدیریت اهمیت بیشتری دارد.",
    "accounting": "🧾 *حسابداری*\n\nمعادله اساسی: دارایی = بدهی + سرمایه.\n\n⭐ دارایی منابع اقتصادی تحت کنترل واحد تجاری است.",
    "finance": "📈 *مدیریت مالی*\n\nارزش زمانی پول، ریسک و بازده، سرمایه‌گذاری و ساختار سرمایه از مباحث کلیدی هستند.",
    "marketing": "📣 *بازاریابی و فروش*\n\n4P شامل محصول، قیمت، توزیع و ترفیع است. STP نیز شامل بخش‌بندی، هدف‌گذاری و جایگاه‌یابی است.",
    "trade": "🌍 *تجارت بین‌الملل*\n\nصادرات، واردات، اسناد تجاری، پرداخت بین‌المللی و اینکوترمز از مباحث اصلی هستند.",
    "iq": "🧠 *هوش و استعداد*\n\nدنباله‌ها، الگوها، استدلال، حل مسئله و سرعت و دقت را تمرین کنید.",
    "english": "🇬🇧 *زبان انگلیسی*\n\nواژگان، گرامر، زمان‌ها، درک مطلب و کلوز تست از محورهای اصلی هستند.",
    "icdl": "💻 *ICDL*\n\nWindows، Word، Excel، PowerPoint، اینترنت، فایل‌ها و امنیت اطلاعات را تمرین کنید.",
}

async def lesson(query, subject):
    name = SUBJECTS[subject][1]
    text = LESSON_TEXT.get(subject, f"📚 {name}\n\nدرسنامه در حال توسعه است.")
    await query.edit_message_text(
        text + "\n\n👇 برای سنجش یادگیری، آزمون این درس را شروع کنید.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [btn("📝 آزمون این درس", f"exam:{subject}:5")],
            [btn("🔙 دروس", "subjects")],
            [btn("🏠 خانه", "home")],
        ]),
    )

async def interview(query):
    await query.edit_message_text(
        "🎤 *آمادگی مصاحبه استخدامی*\n\n"
        "👤 معرفی خود\n"
        "🏦 سؤالات تخصصی بانکی\n"
        "🧠 سؤالات رفتاری\n"
        "🎯 سؤالات موقعیتی\n"
        "💬 مهارت پاسخ‌گویی\n"
        "😌 مدیریت استرس\n\n"
        "تمرکز مصاحبه باید روی پاسخ کوتاه، منطقی و مرتبط با سؤال باشد.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[btn("🔙 خانه", "home")]]),
    )

async def start_exam(query, context, data):
    _, mode, count_s = data.split(":")
    count = int(count_s)
    conn = db()

    if mode in SUBJECTS:
        rows = conn.execute("SELECT * FROM questions WHERE subject=?", (mode,)).fetchall()
        subject_label = SUBJECTS[mode][1]
    else:
        rows = conn.execute("SELECT * FROM questions").fetchall()
        subject_label = "آزمون تصادفی"

    conn.close()
    if not rows:
        await query.edit_message_text("⚠️ سؤال کافی برای این آزمون وجود ندارد.", reply_markup=exams_menu())
        return

    rows = list(rows)
    random.shuffle(rows)
    rows = rows[:min(count, len(rows))]
    context.user_data["exam"] = {
        "questions": [dict(r) for r in rows],
        "index": 0,
        "correct": 0,
        "answered": 0,
        "subject": mode if mode in SUBJECTS else "random",
        "subject_label": subject_label,
        "started": int(time.time()),
        "selected": None,
    }
    await render_question(query, context)

async def render_question(query, context):
    ex = context.user_data.get("exam")
    if not ex:
        await query.edit_message_text("آزمونی فعال نیست.", reply_markup=main_menu())
        return
    q = ex["questions"][ex["index"]]
    import json
    options = json.loads(q["options"])
    keyboard = [[btn(f"{chr(65+i)}) {o}", f"answer:{i}")] for i, o in enumerate(options)]
    keyboard.append([btn("❌ پایان آزمون", "finish")])
    remaining = max(0, 300 - (int(time.time()) - ex["started"]))
    text = (
        f"🏆 *{ex['subject_label']}*\n"
        f"سؤال {ex['index']+1} از {len(ex['questions'])}\n"
        f"⏱️ زمان: {remaining//60:02d}:{remaining%60:02d}\n\n"
        f"❓ {q['question']}\n\n"
        "گزینه صحیح را انتخاب کنید:"
    )
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def answer_question(query, context, data):
    ex = context.user_data.get("exam")
    if not ex:
        return
    choice = int(data.split(":")[1])
    q = ex["questions"][ex["index"]]
    correct = int(q["correct"])
    ex["answered"] += 1
    if choice == correct:
        ex["correct"] += 1
        add_xp(query.from_user.id, 10)
        feedback = "✅ *پاسخ صحیح!*"
    else:
        save_mistake(query.from_user.id, q["id"], q["subject"])
        feedback = "❌ *پاسخ نادرست*"

    import json
    opts = json.loads(q["options"])
    explanation = q["explanation"]
    await query.edit_message_text(
        f"{feedback}\n\n"
        f"🎯 پاسخ صحیح: {chr(65+correct)}) {opts[correct]}\n\n"
        f"💡 *توضیح:*\n{explanation}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [btn("➡️ سؤال بعدی", "next")],
            [btn("🏁 پایان آزمون", "finish")],
        ]),
    )

async def next_question(query, context):
    ex = context.user_data.get("exam")
    if not ex:
        await query.edit_message_text("آزمونی فعال نیست.", reply_markup=main_menu())
        return
    if int(time.time()) - ex["started"] >= 300:
        await finish_exam(query, context)
        return
    ex["index"] += 1
    if ex["index"] >= len(ex["questions"]):
        await finish_exam(query, context)
    else:
        await render_question(query, context)

async def finish_exam(query, context):
    ex = context.user_data.pop("exam", None)
    if not ex:
        await query.edit_message_text("آزمونی برای پایان وجود ندارد.", reply_markup=main_menu())
        return
    total = len(ex["questions"])
    duration = int(time.time()) - ex["started"]
    percent = save_result(query.from_user.id, ex["subject"], total, ex["correct"], duration)
    level = get_user(query.from_user.id)["level"]

    if percent >= 90:
        rank = "🏆 عالی"
        tip = "در سطح بسیار خوبی هستید؛ آزمون جامع را امتحان کنید."
    elif percent >= 70:
        rank = "⭐ خوب"
        tip = "با مرور نقاط ضعف می‌توانید به سطح عالی برسید."
    elif percent >= 50:
        rank = "📚 متوسط"
        tip = "یک دور درسنامه را مرور و دوباره تست بزنید."
    else:
        rank = "🔄 نیازمند تمرین"
        tip = "ابتدا درسنامه و تست آموزشی را انجام دهید."

    await query.edit_message_text(
        f"🏁 *کارنامه آزمون*\n\n"
        f"📚 {ex['subject_label']}\n"
        f"📝 تعداد سؤال: {total}\n"
        f"✅ صحیح: {ex['correct']}\n"
        f"❌ غلط/بی‌پاسخ: {total-ex['correct']}\n"
        f"📊 درصد: {percent}%\n"
        f"⏱️ زمان: {duration//60:02d}:{duration%60:02d}\n"
        f"⭐ سطح فعلی: {level}\n"
        f"{rank}\n\n"
        f"🎯 {tip}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [btn("🔁 آزمون جدید", "exams")],
            [btn("📊 تحلیل عملکرد", "analytics")],
            [btn("🏠 خانه", "home")],
        ]),
    )

async def error_handler(update, context):
    print("ERROR:", context.error)

def main():
    if not BOT_TOKEN:
        raise SystemExit(
            "BOT_TOKEN تنظیم نشده است. در Linux/macOS: export BOT_TOKEN='YOUR_TOKEN' "
            "و در Windows PowerShell: $env:BOT_TOKEN='YOUR_TOKEN'"
        )
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_error_handler(error_handler)
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
