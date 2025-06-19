import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
from db import Database

dp = Dispatcher()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    from app.handlers import rt
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit...")
