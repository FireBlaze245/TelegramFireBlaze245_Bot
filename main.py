import asyncio
import logging
import tracemalloc
from os import getenv
from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession

from CheckProxy import CheckProxy

load_dotenv()
TOKEN = getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("Token not found!")
print(TOKEN)

dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message()
async def hello(message):
    await message.answer("Hello!")

async def main():
    # Асинхронно ищем рабочий прокси
    proxy_checker = await CheckProxy().find_working_proxy()

    if proxy_checker.proxy_status == 200:
        session = AiohttpSession(proxy=proxy_checker.proxy_url)
        bot = Bot(token=TOKEN, session=session, request_timeout=100)
        print(f"Запуск бота с прокси: {proxy_checker.proxy_url}")
    else:
        # Запускаем без прокси, если ни один не работает
        bot = Bot(token=TOKEN, request_timeout=10)
        print("Запуск бота без прокси")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    tracemalloc.start()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
