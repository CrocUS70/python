from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте! Вас приветствует бронетанковый музей-бот', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему /ссылка на бота/')
        
async def tour_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-пт 9:00-20:00')
    
async def tour_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'м.Бауманская')
    
async def tour_remove_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Успешно', reply_markup=ReplyKeyboardRemove())
    
async def tour_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)
    
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(tour_open_command, commands=['Режим_работы'])
    dp.register_message_handler(tour_place_command, commands=['Расположение'])
    dp.register_message_handler(tour_remove_command, commands=['Завершить'])
    dp.register_message_handler(tour_menu_command, commands=['Посмотреть_список_танков'])
