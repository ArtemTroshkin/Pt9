import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from app.config_reader import load_config
from app.handlers import food_handlers, drink_handlers, common_handlers

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Начало работы'),
        BotCommand(command='/food', description='Выбор еды'),
        BotCommand(command='/drink', description='Выбор напитков'),
        BotCommand(command='/cancel', description='Отмена')
    ]

    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger.info('Starting bot')

    config = load_config(r'D:\PycharmProjects\Pt9\bots\food_bot\config\bot_config.ini')

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    """Регистрация хэндлеров"""
    common_handlers(dp)
    food_handlers(dp)
    drink_handlers(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
