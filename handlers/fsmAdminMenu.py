from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from .keyboards import cancel_markup

from config import bot


class FSMAdmin(StatesGroup):
    photo = State()
    dish = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await bot.send_message(message.chat.id,
                           f"Привет {message.from_user.full_name}, скинь фотку...",
                           reply_markup=cancel_markup)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['nickname'] = f"{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Название блюда?")

async def load_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dish'] = message.photo[0].file_id
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Название блюда?")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Описание блюда?")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Цена блюда?")
    await state.finish()
    await bot.send_message(message.chat.id, "Ням ням!")


async def cancal_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("ОК")



def register_handler_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(cancal_reg, state="*", commands="cancel")
    dp.register_message_handler(cancal_reg, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=["register"])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
