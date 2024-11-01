import os
import json

import requests

from dotenv import load_dotenv
from aiogram import Router, F # F alias for MagicFilter in aiogram
from aiogram.types import Message, CallbackQuery, InputMediaPhoto 
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.command import CommandStart, Command
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from keyboards.keyboards import main_keyboard #, training_keyboard
# from keyboards.inline_kb import inline_keyboard

import app.keyboards.inline_kb as kb

router = Router()



def is_valid_image_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.headers['Content-Type'].startswith('image/')
    except Exception:
        return False



# Чтение из .env файла
load_dotenv()

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
whatsapp_link = f"https://wa.me/{WHATSAPP_NUMBER}"


# Чтение из файла JSON (названия и кнопок)
with open("configs.json", "r", encoding="utf-8") as f:
    data = json.load(f)
 
# Доступ к разделам и кнопкам    
sections = data["sections"]

# Функция для проверки и редактирования сообщения с изображением или текстом
async def send(entity, about_description, about_image_url, inline_keyboard):
    try:
        if isinstance(entity, CallbackQuery):
            await edit_message(entity, about_description, about_image_url, inline_keyboard)
        elif isinstance(entity, Message):
            await send_message(entity, about_description, about_image_url, inline_keyboard)
    except TelegramBadRequest as e:
        if 'message media can\'t be edited' in str(e):
            # Если редактирование медиа невозможно, отправьте новое сообщение
            await entity.reply_photo(photo=about_image_url, caption=about_description, reply_markup=inline_keyboard)
        elif 'message is not modified' in str(e):
            # Если сообщение не изменилось, можно просто игнорировать
            pass
        else:
            raise e

async def edit_message(entity, description, image_url, inline_keyboard):
    media = InputMediaPhoto(media=image_url, caption=description)
    await entity.message.edit_media(media=media, reply_markup=inline_keyboard)

async def send_message(entity, description, image_url, inline_keyboard):
    await entity.reply_photo(photo=image_url, caption=description, reply_markup=inline_keyboard)




@router.message(CommandStart())
async def cmd_welcome(callback: CallbackQuery):
    # Получаем описание и изображение из секции about
    about_description = sections["about"]["description"]
    about_image_url = sections["about"]["image"]
    
    # Создаем клавиатуру
    general_keyboard = await kb.create_general_kb()  # Убедитесь, что это не асинхронная функция, если это не так, уберите await
    
    await send(callback, about_description, about_image_url, general_keyboard)

@router.callback_query(F.data == "services") # F.data == "services"
async def callback_services_info(callback: CallbackQuery):
		# Получаем описание и изображение из секции about
		services_description = sections["services"]["description"]
		services_image_url = sections["services"]["image"]
		
		# Создаем клавиатуру
		services_keyboard = await kb.create_services_kb()
		await send(callback, services_description, services_image_url, services_keyboard)

@router.callback_query(F.data == "rental") # F.data == "rental"
async def callback_rental_info(callback: CallbackQuery):
		# Получаем описание и изображение из секции about
		rental_description = sections["rental"]["description"]
		rental_image_url = sections["rental"]["image"]
		
		# Создаем клавиатуру
		rentail_keyboard = await kb.create_rental_kb()
		await send(callback, rental_description, rental_image_url, rentail_keyboard)

@router.callback_query(F.data == "back") # F.data == "back"
async def callback_back_info(callback: CallbackQuery):
		# Получаем описание и изображение из секции about
		about_description = sections["about"]["description"]
		about_image_url = sections["about"]["image"]
		
		# Создаем клавиатуру
		inline_keyboard = await kb.create_general_kb()
		await send(callback, about_description, about_image_url, inline_keyboard)
