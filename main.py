import asyncio
import logging
import tracemalloc
from os import getenv
from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy="http://95.213.217.168:52004")
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
    bot = Bot(token=TOKEN, session=session, request_timeout=30)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    tracemalloc.start()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
# hello from pc ggggg
