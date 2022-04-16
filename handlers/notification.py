from aiogram import types, Dispatcher
from config import bot, dp

# @dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)




def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)