from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import user_kb
from database import bot_db

from config import bot


class FSMADMIN(StatesGroup):
    id = State()
    user_name = State()
    first_name = State()
    last_name = State()


async def user_command(message: types.Message):
    global USER_ID
    USER_ID = message.chat.id
    await bot.send_message(message.chat.id, "Yes user!\n"
                                            "What dou you need?\n"
                                            "1.Start /register\n"
                                            "2.cancel /unregister\n",
                           reply_markup=user_kb.button_register)
    await message.delete()


async def cancel_command(message: types.Message,
                         state: FSMContext):
    if message.chat.id == USER_ID:
        current_state = await state.get_state()
        if current_state is None:
            return "State is None,Relax"
        await state.finish()
        await message.reply("Canceled Successfully")


async def fsm_start(message: types.Message):
    if message.chat.id == USER_ID:
        await FSMADMIN.id.set()
        await message.reply("to start registering write 'OK' and click 'Enter'")


async def load_id(message: types.Message,
                  state: FSMContext):
    async with state.proxy() as reg:
        reg['id'] = message.chat.id
    if message.chat.id == USER_ID:
        await FSMADMIN.next()
        await message.reply("your user_name")


async def load_user_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as reg:
        reg['user_name'] = message.text
    await FSMADMIN.next()
    await message.reply("your first_name")


async def load_first_name(message: types.Message,
                          state: FSMContext):
    async with state.proxy() as reg:
        reg['first_name'] = message.text
    await FSMADMIN.next()
    await message.reply("your last_name")


async def load_last_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as reg:
        reg['last_name'] = message.text
    await FSMADMIN.next()

    # async with state.proxy() as data:
    #     await message.reply(str(data))
    await message.reply("You have successfully registered")
    await bot_db.sql_insert_telegram_account_id(state)
    await state.finish()


def register_handler_for_users(dp: Dispatcher):
    dp.register_message_handler(user_command, commands=['user'])
    dp.register_message_handler(cancel_command, state='*', commands=['cancel'])
    dp.message_handler(cancel_command, Text(equals='cancel', ignore_case=False), state='*')
    dp.register_message_handler(fsm_start, commands=['register'], state=None)
    dp.register_message_handler(load_id, state=FSMADMIN.id)
    dp.register_message_handler(load_user_name, state=FSMADMIN.user_name)
    dp.register_message_handler(load_first_name, state=FSMADMIN.first_name)
    dp.register_message_handler(load_last_name, state=FSMADMIN.last_name)
