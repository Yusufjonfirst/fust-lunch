from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    location = State()
    work_longitude = State()
    work_latitude = State()
    home_longitude = State()
    home_latitude = State()
