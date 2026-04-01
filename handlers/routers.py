from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup, callback_query, CallbackQuery)

from Forms.user import *


router = Router()


@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отклонена!")











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
            [InlineKeyboardButton(text = "Инфо", callback_data="strt")],
        ]
    )
    return keyboard


@router.callback_query(lambda c: c.data == "strt")
async def callback_start(callback: CallbackQuery):
    await callback.message.answer("Хахахахахахах")
    await callback.answer()

@router.message(F.text.lower() == "привет")
@router.message(Command("hello"))
async def hello(message: Message):
    await message.answer("You're welcome!\n\nНапиши /help для помощи")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Команды:\n/start - запуск бота\n/help - комманды\n/about - о нас",
                         reply_markup=get_main_reply_keyboard())
    
@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Этот бот мой, {message.from_user.first_name}", reply_markup=get_main_inline_keyboard())

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Давайте заполним анкету\nВведите ваше имя")
    await state.set_state(Form.name)



@router.message(Form.name, F.text)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично\nТеперь введите ваш возраст")
    await state.set_state(Form.age)

@router.message(Form.age, F.text)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.ansswer("Возраст должен быть числом")
        return
    if int(message.text) < 1 or int(message.text) > 150:
        await message.ansswer("Возраст должен от 1 до 150")
        return
    await state.update_data(age=int(message.text))
    await message.answer("Отлично\nТеперь введите ваш email")
    await state.set_state(Form.email)

@router.message(Form.email, F.text)
async def process_email(message: Message, state: FSMContext):
    email_text = message.text
    if "@" not in email_text or "."  not in email_text:
        await message.answer("Email не корректный")
    await state.update_data(email=email_text)
    await message.answer("Отлично\n")
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    email = data.get("email")
    await message.answer(f"Ваша анкета\nИмя: {name}\nВозраст: {age}\nПочта: {email}")
    await state.clear()



@router.message()
async def hello(message):
    await message.answer("Hello!")
#






