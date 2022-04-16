from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher
from aiogram import types

from config import bot



# @dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def vopros_2(call: types.CallbackQuery):
    knopka2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1",
    )
    knopka2.add(button_call_2)

    photo = open("media/photo_2022.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    question_2 = "Что напечатает такой код? "
    answers = ['1', '2', 'True', 'False', 'Error']
    await bot.send_poll(call.message.chat.id,
                        question=question_2,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=knopka2
                        )

# @dp.callback_query_handler(lambda func: func.data == "button_call_3")
async def vopros_3(call_message: types.CallbackQuery):
    knopka3 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_3",
    )
    knopka3.add(button_call_3)
    photo = open("media/vopros_3.jpg", "rb")
    await bot.send_photo(call_message.message.chat.id, photo=photo)
    question_3 = "Что выведет данная строка кода? "
    answers = "True False Error".split()
    await bot.send_poll(call_message.message.chat.id,
                        question=question_3,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=5,
                        reply_markup=knopka3
                        )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        vopros_2,
        lambda func: func.data == "button_call_1")
    dp.register_callback_query_handler(
        vopros_3,
        lambda func: func.data == "button_call_3")