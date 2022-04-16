from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
import random

# @dp.message_handler(commands=['quiz'])
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

# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/images (3).jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)


# @dp.message_handler(commands=['vopros'])
async def vopros_1(message: types.Message):
    knopka = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1",
    )
    knopka.add(button_call_1)

    photo = open("media/pyt.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)
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


# @dp.message_handler(commands=["pin"], commands_prefix = "!/")
async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        await message.bot.delete_message(message.chat.id, message.message_id)
        await message.bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

# @dp.message_handler(commands=["text"])
async def echo_message(message: types.Message):
    if message.text.startswith("game"):
        if message.from_user.id != ADMIN:
            await bot.send_message(message.chat.id, "Permission denied!")
        else:
            emoji_list = ["🎲", "🏀", "🎰", "⚽", "🎯", "🎳"]
            emoji = random.choice(emoji_list)
            await bot.send_dice(message.chat.id, emoji=emoji)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(vopros_1, commands=['vopros'])
    dp.register_message_handler(echo_message, commands=["text"])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix = "!/")