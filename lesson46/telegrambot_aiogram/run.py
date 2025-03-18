import asyncio, logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

from app.handlers import router


# @dp.message(CommandStart())
# async def start(message: Message) -> None:
#     user = message.from_user
#     await message.answer(f"Hello, {user.first_name}!")
#     await message.reply(f"Got from user with id: {user.id}")


# @dp.message(Command('help'))
# async def help(message: Message) -> None:
#     await message.answer(f"NO help!")


# @dp.message(F.text.lower().startswith('how are you')) 
# async def greete(message: Message) -> None:
#     await message.answer(f"Ok!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    dp.include_router(router)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit bot!")