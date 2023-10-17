from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.users_keyboard import phone_number_share, user_main_menu, user_location
from loader import dp, db_manager
from states.register import Register


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    if db_manager.get_user(message):
        text = "Botga xush kelibsiz. 😊"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Iltimos to'liq ismingizni kiriting."
        await message.answer(text=text)
        await Register.full_name.set()


@dp.message_handler(state=Register.full_name)
async def full_name_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "full_name": message.text
    })

    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text=text, reply_markup=phone_number_share)
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number
    })

    text = "Iltimos ish yoki uy joyingizni kiriting.\n Agar tashlamoqchi bolmasamgiz pasdagi o`tkazib yuborish tugmasini bosin!"
    await message.answer(text=text, reply_markup=user_location)
    await Register.location.set()


@dp.message_handler(state=Register.location)
async def user_location_buttons_handler(message: types.Message, state: FSMContext):
    message_text = message.text
    if message_text == "◀️ Otkazib yuborish":
        await state.update_data({
            "location": None
        })
        text = "Yoshingizni kiriting!"
        await message.answer(text=text)
        await Register.age.set()
    elif message_text == "👨‍💻 Ishlash joyini kiritish":
        text = "Iltimos ishhonangizni lokatsiyasini tashlang!"
        await message.answer(text=text)
        await Register.work_longitude.set()
    elif message_text == "🏘 Uy joyini kiritish":
        text = "Iltimos uyingizni lokatsiyasini tashlang!"
        await message.answer(text=text)
        await Register.home_longitude.set()
    else:
        await message.answer(text=message_text)


@dp.message_handler(state=Register.work_longitude, content_types=types.ContentType.LOCATION)
async def get_work_location_state(message: types.Message, state: FSMContext):
    longitude = message.location.longitude
    latitude = message.location.latitude
    await state.update_data({
        "work_longitude": longitude,
        "work_latitude": latitude
    })

    text = "Iltimos yoshingizni kiriting."
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await Register.age.set()


@dp.message_handler(state=Register.home_longitude, content_types=types.ContentType.LOCATION)
async def get_home_location_state(message: types.Message, state: FSMContext):
    longitude = message.location.longitude
    latitude = message.location.latitude
    await state.update_data({
        "home_longitude": longitude,
        "home_latitude": latitude
    })
    text = "Iltimos yoshingizni kiriting."
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await Register.age.set()


@dp.message_handler(state=Register.age)
async def age_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "age": message.text,
        "user_id": message.chat.id,
    })
    data = await state.get_data()
    if db_manager.append_user(data):
        text = "Siz muvofaqqiyatli ro'yxatdan o'tdingiz. ✅"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Botda muommo mavjud, biz bilan bog'laning!"
        await message.answer(text=text)
    await state.finish()
