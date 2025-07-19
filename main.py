import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 🎲 Список возможных ответов
REPLIES = [
    "Привет, как дела?",
    "Здорова!",
    "Рад тебя видеть!",
    "Йо, ты кто?",
    "Как жизнь, брат?",
]

# 🔑 Токен бота из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 📩 Обработка сообщений
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text(random.choice(REPLIES))

# 🚀 Запуск бота
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    print("✅ Бот работает!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())