from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

bot = Bot('5804822411:AAEBghq0pjxI0MTQqtT9yC43Z5eEuOugj18')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, я бот, который отправит в ответ любое твое сообщение')


@dp.message_handler()
async def echo(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)
    # await message.reply(message.text)
    await message.answer(message.text)

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)
