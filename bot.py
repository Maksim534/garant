from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re, asyncio

bot = Bot(token='7692626473:AAEgJxf5PS_RG0_geBIqP3V8UU1uKlzmwl8', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
vip = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
	executor.start_polling(vip)
