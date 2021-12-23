import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot('5070941689:AAFxR5Z4A0agIeEb1IyrKHbf2XvHcB9fYoo')
dp = Dispatcher(bot, storage=storage)