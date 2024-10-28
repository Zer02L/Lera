import os
from dotenv import load_dotenv
from aiogram import types
from aiogram import F # alias for MagicFilter in aiogram
from aiogram.filters.command import Command, CommandStart
from aiogram import Dispatcher
from keyboards.keyboards import main_keyboard, training_keyboard

load_dotenv()

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
whatsapp_link = f"https://wa.me/{WHATSAPP_NUMBER}"


def register_handlers(dp: Dispatcher):

    @dp.message(Command('start'))
    async def cmd_welcome(message: types.Message):
        await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=main_keyboard)

    # @dp.message()
    # async def process_any_message(message: types.Message):
    #     await message.reply(text=message.text)

    @dp.message(F.text == "Обо мне")
    async def about_me(message: types.Message):
        await message.answer("Здесь информация обо мне.", reply_markup=main_keyboard)

    @dp.message(F.text == "Тренировки:")
    async def trainings(message: types.Message):
        await message.answer("Выберите тип тренировки:", reply_markup=training_keyboard)

    @dp.message(F.text == "Для взрослых")
    async def adult_trainings(message: types.Message):
        await message.answer("Информация о тренировках для взрослых.", reply_markup=training_keyboard)

    @dp.message(F.text == "Для детей")
    async def kids_trainings(message: types.Message):
        await message.answer("Информация о тренировках для детей.", reply_markup=training_keyboard)

    @dp.message(F.text == "Аренда помещение")
    async def rental_info(message: types.Message):
        await message.answer("Информация о аренде помещения.", reply_markup=main_keyboard)

    @dp.message(F.text == "Каналы для самостоятельных онлайн тренировок")
    async def online_channels(message: types.Message):
        await message.answer("Список каналов для онлайн тренировок.", reply_markup=main_keyboard)

    @dp.message(F.text == "Стоимость услуг")
    async def service_pricing(message: types.Message):
        await message.answer("Стоимость услуг", parse_mode='Markdown', reply_markup=main_keyboard)

    @dp.message(F.text == "Консультация (Ссылка на WhatsApp)")
    async def consultation(message: types.Message):
        await message.answer(f"Запросите консультацию по следующей ссылке: [WhatsApp]({whatsapp_link})", parse_mode='Markdown', reply_markup=main_keyboard)

    # Обработчик для кнопки "Назад в главное меню"
    @dp.message(F.text == "Назад в главное меню")
    async def back_to_main_menu(message: types.Message):
        await message.answer("Вы вернулись в главное меню. Выберите опцию:", reply_markup=main_keyboard)
