from aiogram import types, Dispatcher
from config import bot

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def survey_one_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_7 = InlineKeyboardButton("Я стал отцом!",
                                                callback_data="button_survey_call_7")

    button_survey_call_8 = InlineKeyboardButton("Едем отдыхать!",
                                                callback_data="button_survey_call_8")
    markup.add(button_survey_call_7, button_survey_call_8)
    await bot.send_message(call.message.chat.id, "Что вас так порадовал(а)?", reply_markup=markup)


async def survey_one_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_9 = InlineKeyboardButton("мальчик",
                                                callback_data="button_survey_call_9")
    button_survey_call_10 = InlineKeyboardButton("девочка",
                                                 callback_data="button_survey_call_10")
    markup.add(button_survey_call_9, button_survey_call_10)
    await bot.send_message(call.message.chat.id,
                           "Поздравляю очень раз за вас,мальчик или девочка?", reply_markup=markup)


async def survey_ome_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_11 = InlineKeyboardButton("Мухаммад",
                                                 callback_data="button_survey_call_11")
    markup.add(button_survey_call_11)
    await bot.send_message(call.message.chat.id, "Как вы его назавете?", reply_markup=markup)


async def survey_ome_4(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Отличная имя, Желаю к вашему ребенку долгих"
                                                 " лет и лёгкой жизни")


async def survey_ome_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_12 = InlineKeyboardButton("Фатима",
                                                 callback_data="button_survey_call_12")
    markup.add(button_survey_call_12)
    await bot.send_message(call.message.chat.id, "Как вы её назавете?", reply_markup=markup)


async def survey_one_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_13 = InlineKeyboardButton("в Иссик-Куль",
                                                 callback_data="button_survey_call_13")
    button_survey_call_14 = InlineKeyboardButton("в Турцию",
                                                 callback_data="button_survey_call_14")
    markup.add(button_survey_call_13, button_survey_call_14)
    await bot.send_message(call.message.chat.id,
                           "Круто,а куда вы едете?", reply_markup=markup)


async def survey_ome_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    await bot.send_message(call.message.chat.id,
                           "Иссык-Куль - это одно из красивейших мест,хорошего отдыха", reply_markup=markup)


async def survey_one_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_survey_call_15 = InlineKeyboardButton("Фетхие",
                                                 callback_data="button_survey_call_15")
    button_survey_call_16 = InlineKeyboardButton("Ичмелер",
                                                 callback_data="button_survey_call_16")
    markup.add(button_survey_call_15, button_survey_call_16)
    await bot.send_message(call.message.chat.id,
                           "Какой курорт выбрали?", reply_markup=markup)


async def survey_ome_9(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    await bot.send_message(call.message.chat.id,
                           "хороший выбор, в основном дорогие отели 4-5* с большой территорией, "
                           "спа, гольф-клубами и прочими элементами роскошного отдыха", reply_markup=markup)


async def survey_ome_10(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    await bot.send_message(call.message.chat.id,
                           "Время тут тягучее, как местный сосновый мед, который непременно стоит попробовать. "
                           "В общем, лучший курорт в Турции для расслабленного пляжного отдыха!", reply_markup=markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(survey_one_1,
                                       lambda call: call.data == "button_survey_call_1")
    dp.register_callback_query_handler(survey_one_2,
                                       lambda call: call.data == "button_survey_call_7")
    dp.register_callback_query_handler(survey_ome_3,
                                       lambda call: call.data == "button_survey_call_9")
    dp.register_callback_query_handler(survey_ome_4,
                                       lambda call: call.data == "button_survey_call_11")
    dp.register_callback_query_handler(survey_ome_5,
                                       lambda call: call.data == "button_survey_call_10")
    dp.register_callback_query_handler(survey_ome_4,
                                       lambda call: call.data == "button_survey_call_12")
    dp.register_callback_query_handler(survey_one_6,
                                       lambda call: call.data == "button_survey_call_8")
    dp.register_callback_query_handler(survey_ome_7,
                                       lambda call: call.data == "button_survey_call_13")
    dp.register_callback_query_handler(survey_one_8,
                                       lambda call: call.data == "button_survey_call_14")
    dp.register_callback_query_handler(survey_ome_9,
                                       lambda call: call.data == "button_survey_call_15")
    dp.register_callback_query_handler(survey_ome_10,
                                       lambda call: call.data == "button_survey_call_16")




