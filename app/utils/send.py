import os

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto

from app.utils.config_loader import load_data

async def send(entity, section_key, inline_keyboard): 
    data = load_data()  # Загружаем данные из JSON
    section = data["sections"].get(section_key)

    if not section:
        response = "Ошибка: Раздел не найден."
        await (entity.reply(response) if isinstance(entity, Message) else entity.answer(response))
        return

    description = section.get("description", "Описание отсутствует")
    image_path = section.get("image")

    # Подтверждаем запрос обратного вызова (если требуется)
    if isinstance(entity, CallbackQuery):
        await entity.answer()

    # Определяем сообщение для редактирования или отправки
    message = entity.message if isinstance(entity, CallbackQuery) else entity

    # Проверяем наличие изображения
    if image_path:
        # Определяем media в зависимости от URL или файла
        if image_path.startswith(("http://", "https://")):
            media = InputMediaPhoto(media=image_path, caption=description)
        elif os.path.isfile(image_path):
            media = InputMediaPhoto(media=FSInputFile(image_path), caption=description)
        else:
            await message.reply("Ошибка: Изображение не найдено.")
            return

        # Попытка редактирования или отправки нового фото
        try:
            await message.edit_media(media, reply_markup=inline_keyboard)
        except TelegramBadRequest:
            await message.reply_photo(photo=media.media, caption=description, reply_markup=inline_keyboard)
        except Exception as e:
            response = "Ошибка отправки сообщения."
            await (entity.reply(response) if isinstance(entity, Message) else entity.answer(response))
            raise e
    else:
        # Отправка сообщения без изображения
        await message.reply(description, reply_markup=inline_keyboard)
