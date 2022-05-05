from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot


async def quize_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Найдите конструктор класса"
    answers = ["__def__",
               "__class__",
               "__init__",
               "self",
               "init",
               ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Для этого есть метод capitalize",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quize_3(call: types.CallbackQuery):
    question = "какой из вариантов принтует " \
               "вывод указанный выше действий:"
    answers = [
        "1",
        "2",
        "3",
        "Все варианты",
    ]

    photo = open("media/task_image2.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quize_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quize_3,
                                       lambda call: call.data == "button_call_2")
