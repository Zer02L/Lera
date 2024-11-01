import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загрузка JSON-файла с названиями кнопок
with open("configs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Извлекаем данные для кнопок
buttons = data["buttons"]
general_buttons = buttons["general"]
section_buttons = buttons["section_buttons"]

# Создаем главную клавиатуру с кнопками из общего раздела
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=general_buttons["free"])],
        [
            KeyboardButton(text=general_buttons["services"]),
            KeyboardButton(text=general_buttons["rental"])
        ],
        [
            KeyboardButton(text=general_buttons["online_training"]),
            KeyboardButton(text=general_buttons["pricing"])
        ],
        [
            KeyboardButton(text=general_buttons["contacts"]),
            KeyboardButton(text=general_buttons["back"])
        ]
    ],
    resize_keyboard=True
)

# Создаем клавиатуру для раздела "Тренировки"
training_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=section_buttons["training"])],
        [
            KeyboardButton(text=section_buttons["adults"]),
            KeyboardButton(text=section_buttons["kids"])
        ]
    ],
    resize_keyboard=True
)


# # Создаем главную клавиатуру
# main_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text=general_buttons["free"]),
#             KeyboardButton(text=general_buttons["services"])
#         ],
#         [
#             KeyboardButton(text=general_buttons["rental"]),
#             KeyboardButton(text=general_buttons["online_training"]),
#         ],
#         [
#             KeyboardButton(text=general_buttons["services"]),
#             KeyboardButton(text=general_buttons["contacts"])
#         ]
#     ],
#     resize_keyboard=True
# )

# # Создаем клавиатуру для тренировок
# training_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text=training_buttons["adults"]),
#             KeyboardButton(text=training_buttons["kids"])
#         ],
#         [
#             KeyboardButton(text=general_buttons["back"])
#         ]
#     ],
#     resize_keyboard=True
# )
