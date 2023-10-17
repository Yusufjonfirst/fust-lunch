from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💻 Ishlash joyini kiritish"),
            KeyboardButton(text="🏘 Uy joyini kiritish"),
        ],
        [
            KeyboardButton(text="◀️ Otkazib yuborish")
        ]
    ], resize_keyboard=True
)

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍱 Qisqa obed"),
            KeyboardButton(text="🍴 To`liq obed")
        ],
        [
            KeyboardButton(text="🥤 Suvlar"),
            KeyboardButton(text="🍰 Shiriliklar")
        ],
        [
            KeyboardButton(text="👤 Profil")
        ]
    ], resize_keyboard=True
)

user_snack_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍚 Guruch"),
            KeyboardButton(text="🍲 Kartoshkali pyure")
        ],
        [
            KeyboardButton(text="🥘 Grechka"),
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)

user_complete_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛 Osh"),
            KeyboardButton(text="🥘 Qozon kabob")
        ],
        [
            KeyboardButton(text="🍡 Kaboblar"),
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)

user_waters_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧃 Juice"),
            KeyboardButton(text="🍸 Sprite")
        ],
        [
            KeyboardButton(text="🍹 Fanta"),
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)

user_cakes_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍰 Vanli to`rt"),
            KeyboardButton(text="🍰 Shecoladli to`rt")
        ],
        [
            KeyboardButton(text="🍰 Bananli tort"),
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)
