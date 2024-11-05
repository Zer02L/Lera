import json
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


# Загружаем JSON с кнопками
with open("configs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Извлекаем кнопки из JSON
button = data["buttons"]
general = button["general_kb"]
services = button["services_kb"]
extra_buttons = button["extra_buttons"]

price = services["price"]
free = extra_buttons["free_channel"]
contact = extra_buttons["contact"]
back = extra_buttons["back"]


async def create_kb(buttons, extra_buttons=None, columns=1):
    builder = InlineKeyboardBuilder()
    
    # Добавляем основные кнопки
    for key, text in buttons.items():
        if text:
            builder.add(InlineKeyboardButton(text=text, callback_data=key))
    
    # Добавляем дополнительные кнопки, если они есть
    if extra_buttons:
        for text, callback_data in extra_buttons:
            builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    
    # Настройка количества столбцов
    return builder.adjust(columns).as_markup()

# Функции для создания конкретных клавиатур
async def create_general_kb():
    return await create_kb(general, columns=1)

async def create_services_kb():
    return await create_kb(services, extra_buttons=[(contact, "contact"), (back, "back")], columns=1)

async def create_rental_kb():
    return await create_kb({}, extra_buttons=[(contact, "contact"), (back, "back")], columns=1)

async def create_free_kb():
    return await create_kb({}, extra_buttons=[(free, "free_channel"), (back, "back")], columns=1)

async def create_price_kb():
    return await create_kb({}, extra_buttons=[(price, "price"), (back, "back")], columns=1)
