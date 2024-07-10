from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import db

menu_btn = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="menu")]],resize_keyboard=True)

add = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="add")]],resize_keyboard=True)


builder  = InlineKeyboardBuilder()

data = db.select_products()
if data:
    name = data[1]
    builder.button(text=f"{name}", callback_data=f"buy:{name}")

builder.adjust(2, 2)