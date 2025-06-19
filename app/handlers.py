# базовые импорты
from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

db = Database("database.db")
rt = Router()

# импорт с/мз модулей
from db import Database
from app import keyboards as kb
from translate_module import t


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if not db.user_exists(message.from_user.id):
        await message.answer("Выберите язык:", reply_markup=kb.langMenu)
    else:
        await message.answer("Добро пожаловать!")

@rt.callback_query(F.data=="lang_en")
async def lang_en(callback: CallbackQuery):
    if not db.user_exists(callback.from_user.id):
        lang = callback.data[5:]
        db.add_user(callback.from_user.id,lang)
        await callback.message.answer(t("Вы успешно зарегистрировались!",lang))

        



@rt.message(Command("help"))
async def help(message:Message) -> None:
    await message.answer("It`s a help button\n@chzzaxuynya @shinoasa - devs")



