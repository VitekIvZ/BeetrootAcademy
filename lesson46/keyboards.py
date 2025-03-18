from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Отримати всі коментарі"),
        KeyboardButton(text="Отримати коментарі за постом"),
        KeyboardButton(text="Отримати випадковий коментар")],
        [KeyboardButton(text="Розпочати відкладені сповіщення"),
        KeyboardButton(text="Зупинити відкладені сповіщення")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select menu..."
)

# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='YouTube', url="https://www.bing.com/ck/a?!&&p=701316f0b5647224fb4f4480030125f460d9a588f317391a817bd15bf67586b1JmltdHM9MTc0MjE2OTYwMA&ptn=3&ver=2&hsh=4&fclid=17f58263-280d-689e-3c52-90df296669a7&u=a1L3ZpZGVvcy9zZWFyY2g_cT15b3V0dWJlK2Fpb2dyYW0rMyZxcHZ0PXlvdXR1YmUrYWlvZ3JhbSszJkZPUk09VkRSRQ&ntb=1")],
#     [InlineKeyboardButton(text='Lecture', callback_data='lesson')]
#     ]
# )
