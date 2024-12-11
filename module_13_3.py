from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib. fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot,storage = MemoryStorage())

@dp.message_handler(text=["urban", "ff"])
async def all_messege(messege):
    print("Urban messege")
    await messege.answer("Urban messege!!")

@dp.message_handler(commands=["start"])
async def start_messege(messege):
    print("start messege")
    await messege.answer("Рады видеть Вас в нашем Боте")

@dp.message_handler()
async def all_message(messege):
    print("Вы получили сообщение.")
    await messege.answer(messege. text)




@dp.message_handler(commands=["start"])
async def start_messege(messege):
    print("Привет! Я бот помогающий твоему здоровью.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
