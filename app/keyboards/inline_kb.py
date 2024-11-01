import json
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


# Загружаем JSON с кнопками
with open("configs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Извлекаем кнопки из JSON
general_buttons = data["buttons"]["general_kb"]
services_buttons = data["buttons"]["services_kb"]
contact_button = data["buttons"]["contact"]
back_button = data["buttons"]["back"]

# Функция для создания inline-клавиатуры
async def create_general_kb():
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки из раздела "general_kb"
    for key, text in general_buttons.items():
        if text:
            builder.add(InlineKeyboardButton(text=text, callback_data=key))
    return builder.adjust(1).as_markup()

# Создаем клавиатуру услуг (services)
async def create_services_kb():
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки из раздела "services_kb"
    for key, text in services_buttons.items():
        if text:
            builder.add(InlineKeyboardButton(text=text, callback_data=key))
    # Добавляем кнопку "back"
    builder.add(InlineKeyboardButton(text=back_button, callback_data="back"))
    
    # Выставляем кнопки в два столбика
    return builder.adjust(1).as_markup()

# Создаем клавиатуру аренды помещения (rental)
async def create_rental_kb():
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text=contact_button, callback_data="contact"))
    # Добавляем кнопку "back"
    builder.add(InlineKeyboardButton(text=back_button, callback_data="back"))
    
    # Выставляем кнопки в два столбика
    return builder.adjust(1).as_markup()
