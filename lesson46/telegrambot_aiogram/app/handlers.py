from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .keyboards import main_menu, settings
# import app.keyboards as kb

# from run import dp
router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    user = message.from_user
    await message.answer(f"Hello, {user.first_name}!", reply_markup=main_menu)
    # await message.reply(f"Got from user with id: {user.id}")


@router.message(Command('help'))
async def help(message: Message) -> None:
    await message.answer(f"NO help!", reply_markup=settings)


@router.message(F.text.lower().startswith('how are you')) 
async def greete(message: Message) -> None:
    await message.answer(f"Ok!")


@router.message(F.text == 'Students') 
async def students(message: Message) -> None:
    await message.answer(f"Students list... ")


@router.callback_query(F.data == 'lesson')
async def lecture(callback):
    await callback.answer("Lesson state")
    await callback.message.answer('Lesson finifhed')


@router.message() 
async def greete(message: Message) -> None:
    await message.answer("No handler for this input")


