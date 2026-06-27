import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

CAFE_MENU = {
    "pizza": "🍕 Піца «Маргарита»",
    "burger": "🍔 Бургер «Шеф»",
    "salad": "🥗 Салат «Цезар»",
    "drink": "🥤 Лимонад Класичний"
}

def get_inline_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🍕 Піца", callback_data="pizza")
    builder.button(text="🍔 Бургер", callback_data="burger")
    builder.button(text="🥗 Салат", callback_data="salad")
    builder.button(text="🥤 Напій", callback_data="drink")
    builder.adjust(2)
    return builder.as_markup()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Оберіть категорію з меню нижче:", reply_markup=get_inline_menu())

@dp.callback_query()
async def process_menu_click(callback: CallbackQuery):
    if callback.data in CAFE_MENU:
        await callback.message.answer(CAFE_MENU[callback.data])
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())