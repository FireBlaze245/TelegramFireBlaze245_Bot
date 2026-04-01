from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup, callback_query, CallbackQuery)

router = Router()


def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Старт"), KeyboardButton(text="Помощь")]
    ],resize_keyboard=True)
    return keyboard


def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text = "Открыть сайт", url="http://google.com")],
            [InlineKeyboardButton(text = "/start", callback_data="start")],
        ]
    )
    return keyboard


@router.callback_query(lambda c: c.data == "start")
async def callback_start(callback: CallbackQuery):
    await callback.message.answer("Хахахахахахах")
    await callback.answer()

@router.message(F.text.lower() == "старт")
@router.message(Command("start"))
async def start(message: Message):
    await message.answer("You're welcome!\n\nНапиши /help для помощи")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Команды:\n/start - запуск бота\n/help - комманды\n/about - о нас",
                         reply_markup=get_main_reply_keyboard())
    
@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Этот бот мой, {message.from_user.first_name}", reply_markup=get_main_inline_keyboard())

@router.message()
async def hello(message):
    await message.answer("Hello!")
#






