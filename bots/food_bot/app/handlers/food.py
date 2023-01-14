from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


food_names = ['пицца', 'бургер', 'пельмени']
food_sizes = ['большая', 'средняя', 'маленькая']


class FoodStates(StatesGroup):
    food_name = State()
    food_size = State()


async def food_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in food_names:
        keyboard.add(name)

    await message.answer('Выберите тип блюда', reply_markup=keyboard)
    await state.set_state(FoodStates.food_name.state)


async def food_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in food_names:
        await message.answer('Пожалуйста, выберите блюдо, используя клавиатуру ниже')
        return
    await state.update_data(chosen_food=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in food_sizes:
        keyboard.add(size)

    await message.answer('Выберите размер порции', reply_markup=keyboard)
    await state.set_state(FoodStates.food_size.state)


async def food_size_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in food_sizes:
        await message.answer('Пожалуйста, выберите размер блюда, используя клавиатуру ниже')
        return

    user_data = await state.get_data()
    food = user_data['chosen_food']  # user_data.get('chosen_food')
    food_size = message.text.lower()

    await message.answer(f'Вы заказали {food}. Порция размером {food_size}', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(food_start, commands='food', state='*')
    dp.register_message_handler(food_chose, state=FoodStates.food_name)
    dp.register_message_handler(food_size_chose, state=FoodStates.food_size)
