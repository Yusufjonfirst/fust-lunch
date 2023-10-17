from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def user_product_buy_def(quantity, total):
    user_product_buy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="minus_product"),
                InlineKeyboardButton(text=f"{quantity}/{total}", callback_data="quantity"),
                InlineKeyboardButton(text="➕", callback_data="plus_product"),
            ],
            [
                InlineKeyboardButton(text="🛍 Savatni ko'rish", callback_data="show_basket"),
            ]
        ]
    )
    return user_product_buy

user_profile_updata = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ism", callback_data="user_name"),
            InlineKeyboardButton(text="Yosh", callback_data="user_age")
        ],
        [
            InlineKeyboardButton(text="Ish joyi", callback_data="work_location"),
            InlineKeyboardButton(text="Uy joyi", callback_data="home_location")
        ],
    ]
)
