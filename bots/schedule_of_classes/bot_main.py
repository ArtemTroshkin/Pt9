from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from config import schedule
import datetime
import logging
from buttons import user_kb
import os

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer('Привет, я бот, который подскажет тебе расписание занятий', reply_markup=user_kb)


@dp.message_handler(Text(equals=schedule.keys(), ignore_case=True))
async def send_schedule(message: types.Message):
    msg = schedule[message.text]
    await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals='сегодня', ignore_case=True))
async def today(message: types.Message):
    msg = schedule[
        list(schedule.keys())[datetime.datetime.now().weekday()]
    ]
    await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


@dp.message_handler(Text(equals='завтра', ignore_case=True))
async def today(message: types.Message):
    if datetime.datetime.now().weekday() + 1 > 6:
        msg = schedule[
            list(schedule.keys())[0]
        ]
        await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)
    else:
        msg = schedule[
            list(schedule.keys())[datetime.datetime.now().weekday() + 1]
        ]
        await message.answer(f'<b>{msg}</b>', parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
