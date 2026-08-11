"""
Andishkadeh Market Bot - Render Webhook Runner
این فایل bot.py فعلی شما را تغییر نمی‌دهد؛ تمام handlerهای آن را استفاده می‌کند
و اجرای Polling را به Webhook روی Render منتقل می‌کند.

Render در لایه عمومی HTTPS ارائه می‌دهد و برنامه روی PORT داخلی گوش می‌دهد.
"""

import logging
import os

from telegram import Update
from telegram.error import BadRequest, TelegramError
from telegram.ext import Application

from bot import TOKEN, register_handlers

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("andishkadeh")

# Render این دو مقدار را برای Web Service فراهم می‌کند.
PORT = int(os.getenv("PORT", "10000"))
PUBLIC_URL = os.getenv("RENDER_EXTERNAL_URL", "").rstrip("/")

# مسیر Webhook را عمومی و حدس‌زدنی نمی‌کنیم.
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "telegram-webhook-2026")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "change-this-secret")

if not PUBLIC_URL:
    raise RuntimeError(
        "RENDER_EXTERNAL_URL پیدا نشد. این فایل باید روی Render Web Service اجرا شود."
    )

if not WEBHOOK_SECRET or WEBHOOK_SECRET == "change-this-secret":
    raise RuntimeError(
        "لطفاً در Render متغیر WEBHOOK_SECRET را به یک مقدار تصادفی و امن تغییر دهید."
    )


async def error_handler(update: object, context) -> None:
    """خطاهای callback منقضی را از کاربر مخفی می‌کند و لاگ را تمیز نگه می‌دارد."""
    error = context.error
    message = str(error)

    if (
        "Query is too old" in message
        or "query id is invalid" in message
        or "response timeout expired" in message
    ):
        logger.warning("Expired callback query ignored: %s", message)
        return

    logger.exception("Unhandled bot error", exc_info=error)


def main() -> None:
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # تمام handlerهای bot.py حفظ می‌شوند.
    register_handlers(application)

    application.add_error_handler(error_handler)

    webhook_url = f"{PUBLIC_URL}/{WEBHOOK_PATH}"

    logger.info("🏛️ Andishkadeh Market Bot is starting in WEBHOOK mode...")
    logger.info("🌐 Public webhook: %s", webhook_url)
    logger.info("🔌 Internal port: %s", PORT)

    # پاک کردن updateهای قدیمی مهم است؛ مخصوصاً callbackهای منقضی.
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_PATH,
        webhook_url=webhook_url,
        secret_token=WEBHOOK_SECRET,
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
    )


if __name__ == "__main__":
    main()
