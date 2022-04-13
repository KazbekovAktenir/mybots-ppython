from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging
import random

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "Сколько золотых мячей у Месси?"
    answers = ['7', '5', '4', '6']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=5
                        )

@dp.message_handler(commands=['mem'])
async def photo(message: types.Message):
    photo = open("media/images (3).jpg", "rb")
    await bot.send_photo(message.chat.id,
                         photo=photo
                         )


@dp.message_handler(commands=['vopros'])
async def vopros_1(message: types.Message):
    knopka = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1",
    )
    knopka.add(button_call_1)

    photo = open("media/pyt.jpg", "rb")
    await bot.send_photo(message.chat.id,
                         photo=photo)
    question = "Что выведет этот код при выполнении? "
    answers = ['1', '1 4', '6 10', '1 4 6', '1 4 6 10', 'Error']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=5,
                        reply_markup=knopka
                        )

@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def vopros_2(call: types.CallbackQuery):
    knopka = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1",
    )
    knopka.add(button_call_1)

    photo = open("media/photo_2022.jpg", "rb")
    await bot.send_photo(call.message.chat.id,
                         photo=photo)
    question_2 = "Что напечатает такой код? "
    answers = ['1', '2', 'True', 'False', 'Error']
    await bot.send_poll(call.message.chat.id,
                        question=question_2,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=knopka
                        )

@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def vopros_3(call_message: types.CallbackQuery):
    knopka = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2",
    )
    knopka.add(button_call_2)
    photo = open("media/vopros_3.jpg", "rb")
    await bot.send_photo(call_message.message.chat.id,
                         photo=photo)
    question_3 = "Что выведет данная строка кода? "
    answers = "True False Error".split()
    await bot.send_poll(call_message.message.chat.id,
                        question=question_3,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=5,
                        reply_markup=knopka
                        )

@dp.message_handler(content_types=["text"])
async def echo_message(message: types.Message):
    # Send dice
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji="🎯")


    #pin message
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
