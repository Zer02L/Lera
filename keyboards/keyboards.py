from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем главную клавиатуру
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обо мне"),
            KeyboardButton(text="Тренировки:")
        ],
        [
            KeyboardButton(text="Аренда помещение"),
            KeyboardButton(text="Каналы для самостоятельных онлайн тренировок")
        ],
        [
            KeyboardButton(text="Стоимость услуг"),
            KeyboardButton(text="Консультация (Ссылка на WhatsApp)")
        ]
    ],
    resize_keyboard=True
)

# Создаем клавиатуру для тренировок
training_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Для взрослых"),
            KeyboardButton(text="Для детей")
        ],
        [
            KeyboardButton(text="Назад в главное меню")
        ]
    ],
    resize_keyboard=True
)
