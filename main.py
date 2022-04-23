from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notification, fsmAdminMenu

async def on_start_up(_):
    users_db.sql_create()

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handler_fsmAdminMenu(dp)

notification.register_handlers_notification(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)

