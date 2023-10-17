from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ReplyKeyboardRemove

from keyboards.default.users_keyboard import user_snack_menu, user_complete_menu, user_waters_menu, user_cakes_menu
from keyboards.inline.inline_keyboard import user_product_buy_def
from loader import dp, db_manager
# from states.register import Register


@dp.message_handler(text="🍱 Qisqa obed")
async def start_handler(message: types.Message):
    text = "Qisqa obed menusiga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_snack_menu)


@dp.message_handler(text="🍚 Guruch")
async def start_handler(message: types.Message):
    text = "Qisqa obeda guruch menusiga xush kelibsiz. 😊"
    order_name = "rice"
    rice_much = 15000
    quantity = 2
    await message.answer(text=text, reply_markup=await user_product_buy_def(quantity, rice_much))


@dp.message_handler(text="🍲 Kartoshkali pyure")
async def start_handler(message: types.Message):
    text = "Qisqa obeda kartoshkali pyure menusiga xush kelibsiz. 😊"
    pyure_much = 17000
    await message.answer(text=text, reply_markup=await user_product_buy_def(111, 111))


@dp.message_handler(text="🥘 Grechka")
async def start_handler(message: types.Message):
    text = "Qisqa obeda grechka menusiga xush kelibsiz. 😊"
    grechka_much = 12000
    await message.answer(text=text, reply_markup=await user_product_buy_def(111, 111))


@dp.message_handler(text="🍴 To`liq obed")
async def start_handler(message: types.Message):
    text = "To`liq obed menusiga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_complete_menu)


@dp.message_handler(text="🥤 Suvlar")
async def start_handler(message: types.Message):
    text = "Suvlar menusiga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_waters_menu)


@dp.message_handler(text="🍰 Shiriliklar")
async def start_handler(message: types.Message):
    text = "Suvlar menusiga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_cakes_menu)


@dp.message_handler(text="👤 Profil")
async def start_handler(message: types.Message):
    text = "Profilga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_cakes_menu)
