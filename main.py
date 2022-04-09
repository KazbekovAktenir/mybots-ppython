from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging

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
                        open_period=5
                        )

@dp.message_handler(commands = ['mem'])
async def photo(message: types.Message):
    photo = open("media/images (3).jpg", "rb")
    await bot.send_photo(message.chat.id,
        photo=photo
                         )

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        chislo = int(message.text)
        await message.answer(chislo ** 2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)

# ds