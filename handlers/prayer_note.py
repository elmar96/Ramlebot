import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(message.chat.id, "got your id")


async def get_ready_for_prayer():
    await bot.send_message(chat_id=chat_id,
                           text="Brother, get ready for the juma namaz!🕌")


async def scheduler():
    aioschedule.every().day.at("12:00").do(get_ready_for_prayer)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_prayer(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'remind' in word.text)
