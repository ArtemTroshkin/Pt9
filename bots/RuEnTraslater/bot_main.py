from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from translater import RuEnTranslater

bot = Bot('5804822411:AAEBghq0pjxI0MTQqtT9yC43Z5eEuOugj18')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer('Привет, я бот который может преобразовать русский текст, написанный английской раскладкой')


@dp.message_handler()
async def translate(message: types.Message):
    try:
        text = RuEnTranslater(message.text)
        await message.reply(str(text))
    except Exception as ex:
        await message.reply(str(repr(ex)))


if __name__ == '__main__':
    print('bot started')
    executor.start_polling(dp, skip_updates=True)
