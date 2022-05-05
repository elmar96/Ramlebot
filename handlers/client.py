from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from keyboards import client_kb
from config import bot
from database import bot_db
from parser import scrapy


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.full_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1.Старт /start\n"
                        "2.Опросы /survey\n"
                        "3.Дата и время /times\n"
                        "За ненормативные лексики бот может банить или удалить сообщение!")


async def info(message: types.Message):
    await message.reply("hello friend! Happy to see you,bot designed 06.04.2022.\n"
                        "Admin and developer of the bot is: Elmar Abdyramanov")


async def times(message: types.Message):
    await message.reply(f"Время {datetime.now()} \n")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Как перевести первый символ строки в верхний регистр"
    answers = ["update",
               "extend",
               "upper",
               "capitalize",

               ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Для этого есть метод capitalize",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,

    )


async def survey(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_survey_call_1 = InlineKeyboardButton("Отлично!",
                                                callback_data="button_survey_call_1")
    button_survey_call_2 = InlineKeyboardButton("Схватился за голову!",
                                                callback_data="button_survey_call_2")
    markup.add(button_survey_call_1, button_survey_call_2)
    await bot.send_message(message.chat.id, "как поживаете?",
                           reply_markup=markup)


async def get_all_tvshow(message: types.Message):
    await bot_db.sql_select(message)


async def parser_movies(message: types.Message):
    data = scrapy.scrapy_script()
    for i in data:
        await bot.send_message(message.chat.id, i)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(survey, commands=['survey'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(times, commands=['times'])
    dp.register_message_handler(get_all_tvshow, commands=['tvshow'])
    dp.register_message_handler(parser_movies, commands=["scrapy"])
