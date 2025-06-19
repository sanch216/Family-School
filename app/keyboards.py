from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

langMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Русский", callback_data='lang_ru')],
    [InlineKeyboardButton(text="English", callback_data='lang_en')],
    [InlineKeyboardButton(text="Кыргызча", callback_data='lang_kg')]
])
