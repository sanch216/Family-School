from aiogram import Bot, Dispatcher, html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

rt = Router()

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\nWe are a Family School!")

@rt.message(Command("help"))
async def help(message:Message) -> None:
    await message.answer("It`s a help button\n@chzzaxuynya @shinoasa - devs")



