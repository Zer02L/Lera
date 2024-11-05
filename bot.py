import asyncio
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv


from app.handlers.handlers import router

# Загружаем переменные окружения из .env файла
load_dotenv()

# Устанавливаем уровень логирования
logger = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
API_TOKEN = os.getenv("API_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Запуск бота
async def main():
    dp.include_router(router)
    logger.info("Starting bot")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
