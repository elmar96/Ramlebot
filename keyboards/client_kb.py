from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

help_button = KeyboardButton("/help")
info_button = KeyboardButton("/info")
survey_button = KeyboardButton("/survey")
quiz_button = KeyboardButton("/quiz")
tvshow_button = KeyboardButton('/tvshow')
times_button = KeyboardButton("/times")
user_button = KeyboardButton("/user")
location_button = KeyboardButton("Share Location", reguest_location=True)
share_info_button = KeyboardButton("Share Info", request_contact=True)
start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(help_button,
                 quiz_button,
                 location_button,
                 share_info_button,
                 survey_button,
                 info_button,
                 times_button,
                 user_button,
                 tvshow_button)
