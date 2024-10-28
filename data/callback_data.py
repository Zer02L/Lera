from aiogram.filters.callback_data import CallbackData

# Определение шаблона callback_data
class MenuCallbackData(CallbackData, prefix="menu"):
    action: str
