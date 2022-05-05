from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_register = KeyboardButton('/user')
button_cancel = KeyboardButton('/cancel')


button_admin = ReplyKeyboardMarkup(
    resize_keyboard=True).row(button_register, button_cancel)

