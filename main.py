from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notification, fsmAdminMenu

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_hendler_fsmAdminMenu(dp)

notification.register_hendlers_notification(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
