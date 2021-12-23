from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # ,ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Посмотреть_список_танков')
b4 = KeyboardButton('/Завершить')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2).row(b3, b4)