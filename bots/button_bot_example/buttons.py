from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_good_morning = KeyboardButton('Пожелание доброго утра')
button_good_night = KeyboardButton('Пожелание доброй ночи')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_good_morning).add(
    button_good_night)

button_date = InlineKeyboardButton(text="Время и дата", callback_data='button_date')
button_url = InlineKeyboardButton(text='Ссылка на гитхаб', url='https://github.com/evil-kekc')

user_inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(button_date).add(button_url)
