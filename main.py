import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Піца"),
            KeyboardButton(text="🍔 Бургер"),
        ],
        [
            KeyboardButton(text="🥗 Салат"),
            KeyboardButton(text="🥤 Напій"),
        ],
    ],
    resize_keyboard=True
)

items = {
    "🍕 Піца": {
        "price": "180 грн",
        "description": "Тісто, сир моцарела, томатний соус, салямі"
    },
    "🍔 Бургер": {
        "price": "150 грн",
        "description": "Булочка, яловича котлета, сир, салат, соус"
    },
    "🥗 Салат": {
        "price": "120 грн",
        "description": "Овочі, курка, зелень, соус"
    },
    "🥤 Напій": {
        "price": "50 грн",
        "description": "Газований або холодний напій"
    }
}


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Привіт! Обери один пункт з меню:",
        reply_markup=menu_keyboard
    )


@dp.message(F.text.in_(items.keys()))
async def item_handler(message: Message):
    item = items[message.text]

    await message.answer(
        f"{message.text}\n\n"
        f"Ціна: {item['price']}\n"
        f"Опис: {item['description']}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "main":
    asyncio.run(main())