from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

drink_names = ['чай', 'кола', 'какао', 'фанта', 'боржоми']
drink_sizes = ['0.2 л', '0.5 л', '0.7 л', '1 л']


class DrinkStates(StatesGroup):
    drink_name = State()
    drink_size = State()


async def drink_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in drink_names:
        keyboard.add(name.title())

    await message.answer('Выберите тип напитка', reply_markup=keyboard)
    await state.set_state(DrinkStates.drink_name.state)


async def drink_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in drink_names:
        await message.answer('Пожалуйста, выберите напиток, используя клавиатуру ниже')
        return
    await state.update_data(chosen_drink=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in drink_sizes:
        keyboard.add(size)

    await message.answer('Выберите размер напитка', reply_markup=keyboard)
    await state.set_state(DrinkStates.drink_size.state)


async def drink_size_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in drink_sizes:
        await message.answer('Пожалуйста, выберите размер напитка, используя клавиатуру ниже')
        return

    user_data = await state.get_data()
    drink = user_data['chosen_drink']
    drink_size = message.text.lower()

    await message.answer(f'Вы заказали {drink}. Порция размером {drink_size}', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_drink(dp: Dispatcher):
    dp.register_message_handler(drink_start, commands='drink', state='*')
    dp.register_message_handler(drink_chose, state=DrinkStates.drink_name)
    dp.register_message_handler(drink_size_chose, state=DrinkStates.drink_size)
