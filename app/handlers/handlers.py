import os

from dotenv import load_dotenv
from aiogram import Router, F # F alias for MagicFilter in aiogram
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile

from aiogram.filters.command import CommandStart, Command


from app.utils.send import send
# from app.utils.send import send

import app.keyboards.inline_kb as kb

router = Router()

# Чтение из .env и JSON-config файла
load_dotenv()
config_path = os.getenv("CONFIG_PATH")
images_path = os.getenv("IMAGES")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
whatsapp_link = f"https://wa.me/{WHATSAPP_NUMBER}"
free_tg_group = os.getenv("FREE_CHANNEL")
# about_image_path = os.getenv("ABOUT_IMAGE")

# # Доступ к разделам и кнопкам    
# data = load_data()
# sections = data["sections"]



@router.message(CommandStart())
async def cmd_welcome(message: Message):
    # Создаем клавиатуру
    general_keyboard = await kb.create_general_kb()  # Убедитесь, что эта функция асинхронная

    # Отправляем сообщение
    await send(message, "about", general_keyboard)

@router.callback_query(F.data.in_({"services", "rental", "free", "price", "back"}))
async def callback_handler(callback: CallbackQuery):
    # Сопоставление значений F.data с ключами и функциями создания клавиатур
    data_to_section = {
        "services": ("services", kb.create_services_kb),
        "rental": ("rental", kb.create_rental_kb),
        "free": ("free", kb.create_free_kb),
        "price": ("price", kb.create_price_kb),
        "back": ("about", kb.create_general_kb),
    }

    section_key, keyboard_func = data_to_section[callback.data]
    
    # Создаем клавиатуру и отправляем сообщение
    inline_keyboard = await keyboard_func()
    await send(callback, section_key, inline_keyboard)
