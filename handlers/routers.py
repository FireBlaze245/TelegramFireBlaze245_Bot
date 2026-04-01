from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()


def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Старт"), KeyboardButton(text="Помощь")]
    ])


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("You're welcome!\n\nНапиши /help для помощи")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Команды:\n/start - запуск бота\n/help - комманды\n/about - о нас")
    
@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Этот бот мой, {message.from_user.first_name}")

@router.message()
async def hello(message):
    await message.answer("Hello!")
#






