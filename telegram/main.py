import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from telegram.heandlers import routers_list


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(*routers_list)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

