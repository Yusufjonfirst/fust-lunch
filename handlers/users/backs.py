from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.users_keyboard import phone_number_share, user_main_menu, user_location, user_snack_menu
from loader import dp, db_manager
from states.register import Register


@dp.message_handler(text="⬅️ Orqaga")
async def start_handler(message: types.Message):
    text = "Asosiy menuga xush kelibsiz. 😊"
    await message.answer(text=text, reply_markup=user_main_menu)
