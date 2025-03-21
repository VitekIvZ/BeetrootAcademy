import logging
import aiohttp
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties

from config import TOKEN, JSON_URL, CHANNEL_ID
from keyboards import main_menu

# Налаштування
API_TOKEN = TOKEN  
JSON_URL = JSON_URL
CHANNEL_ID = CHANNEL_ID
menu_keyboard = main_menu

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Глобальна змінна для управління завданнями
scheduled_task = None

# Функція для отримання коментарів з API
async def fetch_comments():
    async with aiohttp.ClientSession() as session:
        async with session.get(JSON_URL) as response:
            if response.status == 200:
                return await response.json()
            else:
                logging.error(f"Помилка при отриманні коментарів: {response.status}")
                return None

# Функція для надсилання випадкового коментаря
async def send_random_comment():
    comments = await fetch_comments()
    if comments:
        comment = random.choice(comments)
        await bot.send_message(
            CHANNEL_ID,
            f"<b>ID:</b> {comment['id']}\n"
            f"<b>Name:</b> {comment['name']}\n"
            f"<b>Email:</b> {comment['email']}\n"
            f"<b>Body:</b> {comment['body']}\n",
        )
        logging.info(f"Надіслано коментар з ID {comment['id']}")
    else:
        logging.error("Не вдалося отримати коментарі.")

# Функція для запуску відкладених сповіщень
async def start_scheduled_notifications(interval: int):
    while True:
        try:
            await send_random_comment()
            await asyncio.sleep(interval)
        except Exception as e:
            logging.error(f"Помилка у відкладених сповіщеннях: {e}")
            await asyncio.sleep(10)

# Обробник команди /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Вітаю! Оберіть опцію з меню:", reply_markup=menu_keyboard)

# Обробник кнопки "Отримати всі коментарі"
@dp.message(lambda message: message.text == "Отримати всі коментарі")
async def get_all_comments(message: types.Message):
    comments = await fetch_comments()
    if comments:
        random_comments = random.sample(comments, min(10, len(comments)))
        for comment in random_comments:
            await message.answer(
                f"<b>ID:</b> {comment['id']}\n"
                f"<b>Name:</b> {comment['name']}\n"
                f"<b>Email:</b> {comment['email']}\n"
                f"<b>Body:</b> {comment['body']}\n",
            )
            await asyncio.sleep(1)
    else:
        await message.answer("Не вдалося отримати коментарі.")

# Обробник кнопки "Отримати коментарі за постом"
@dp.message(lambda message: message.text == "Отримати коментарі за постом")
async def ask_post_id(message: types.Message):
    await message.answer("Введіть ID поста (від 1 до 100):")

# Обробник для отримання коментарів за ID поста
@dp.message(lambda message: message.text.isdigit() and 1 <= int(message.text) <= 100)
async def get_comments_by_post(message: types.Message):
    post_id = int(message.text)
    comments = await fetch_comments()
    if comments:
        filtered_comments = [c for c in comments if c['postId'] == post_id]
        if filtered_comments:
            for comment in filtered_comments[:10]:
                await message.answer(
                    f"<b>ID:</b> {comment['id']}\n"
                    f"<b>Name:</b> {comment['name']}\n"
                    f"<b>Email:</b> {comment['email']}\n"
                    f"<b>Body:</b> {comment['body']}\n",
                )
                await asyncio.sleep(1)
        else:
            await message.answer(f"Коментарі для поста з ID {post_id} не знайдено.")
    else:
        await message.answer("Не вдалося отримати коментарі.")
    await message.answer("Повертаємося до головного меню:", reply_markup=menu_keyboard)

# Обробник кнопки "Отримати випадковий коментар"
@dp.message(lambda message: message.text == "Отримати випадковий коментар")
async def get_random_comment(message: types.Message):
    comments = await fetch_comments()
    if comments:
        comment = random.choice(comments)
        await message.answer(
            f"<b>ID:</b> {comment['id']}\n"
            f"<b>Name:</b> {comment['name']}\n"
            f"<b>Email:</b> {comment['email']}\n"
            f"<b>Body:</b> {comment['body']}\n",
        )
    else:
        await message.answer("Не вдалося отримати коментарі.")

# Обробник кнопки "Розпочати відкладені сповіщення"
@dp.message(lambda message: message.text == "Розпочати відкладені сповіщення")
async def start_notifications(message: types.Message):
    global scheduled_task
    if scheduled_task is None:
        scheduled_task = asyncio.create_task(start_scheduled_notifications(600))
        await message.answer("Відкладені сповіщення розпочато. Коментарі будуть надсилатися кожні 10 хвилин.")
    else:
        await message.answer("Відкладені сповіщення вже запущено.")
        
# Обробник кнопки "Зупинити відкладені сповіщення"
@dp.message(lambda message: message.text == "Зупинити відкладені сповіщення")
async def stop_notifications(message: types.Message):
    global scheduled_task
    if scheduled_task is not None:
        scheduled_task.cancel()
        scheduled_task = None
        await message.answer("Відкладені сповіщення зупинено.")
    else:
        await message.answer("Відкладені сповіщення вже зупинено.")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())