from aiogram import Bot, Router, types, Dispatcher, F
from aiogram.filters import Command

from datetime import datetime, timedelta, timezone

from telegram.config_reader import config

dp = Dispatcher()
bot = Bot(token=config.bot_token.get_secret_value())

router = Router()


async def user_last_activity(time_now: int, time_last_activity: int):
    return int((time_now - time_last_activity).total_seconds() / 60)


@router.message(F.text)
async def last_activity(message: types.Message):
    time_now = int((datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=3)))).timestamp())
    print(time_now)


@router.message(Command("start"))
async def hello_world(message: types.Message):
    await message.answer("Hello world")

