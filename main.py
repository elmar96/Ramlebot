from aiogram.utils import executor

from decouple import config
from config import dp, bot, URL
from handlers import client, callback, extra, fsmadmin, \
    survey_one, survey_two, fsmadmin_register, notification, prayer_note
from database import bot_db
import asyncio


async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    asyncio.create_task(notification.scheduler())
    asyncio.create_task(prayer_note.scheduler())
    print("Bot is online")

async def on_shutdown(dp):
    await bot.delete_webhook()

fsmadmin_register.register_handler_for_users(dp)
survey_two.register_handlers_client(dp)
survey_one.register_handlers_client(dp)
fsmadmin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
prayer_note.register_handler_prayer(dp)
notification.register_handler_notification(dp)
extra.register_handlers_other(dp)

if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
   executor.start_webhook(
        dispatcher = dp,
        webhook_patch = '',
        on_startup = on_startup,
        on_shutdown= on_shutdown,
        skip_updates=True,
        host = '0.0.0.0',
        port=int(config("PORT",default=5000)))



