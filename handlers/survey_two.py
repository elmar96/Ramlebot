from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def survey_two_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_3 = InlineKeyboardButton("Заболел",
                                                callback_data="button_survey_call_3")

    button_survey_call_4 = InlineKeyboardButton("Машину разбил!",
                                                callback_data="button_survey_call_4")
    markup.add(button_survey_call_3, button_survey_call_4)
    await bot.send_message(call.message.chat.id, "Почему?", reply_markup=markup)


async def survey_two_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_5 = InlineKeyboardButton("ОРВИ",
                                                callback_data="button_survey_call_5")
    markup.add(button_survey_call_5)
    await bot.send_message(call.message.chat.id, "Чем же вы болеете?", reply_markup=markup)


async def survey_two_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "предлогаю вам тёплое обильное питьё с лимоном или"
                                                 " чай с малиновым вареньем,поскорее выздоравливайте!👨‍⚕️ ")


async def survey_two_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_6 = InlineKeyboardButton("к счастью нет",
                                                callback_data="button_survey_call_6")
    markup.add(button_survey_call_6)
    await bot.send_message(call.message.chat.id, "вы не пострадали?", reply_markup=markup)


async def survey_two_5(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "берегите себя железа найдется,жизнь одна!")


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(survey_two_1,
                                       lambda call: call.data == "button_survey_call_2")
    dp.register_callback_query_handler(survey_two_2,
                                       lambda call: call.data == "button_survey_call_3")
    dp.register_callback_query_handler(survey_two_3,
                                       lambda call: call.data == "button_survey_call_5")
    dp.register_callback_query_handler(survey_two_4,
                                       lambda call: call.data == "button_survey_call_4")
    dp.register_callback_query_handler(survey_two_5,
                                       lambda call: call.data == "button_survey_call_6")
