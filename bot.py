from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
import asyncio

# Ваш токен от BotFather
API_TOKEN = "8099888433:AAFyxLGCkshHAT1rRaIvnySvM2c_elNBB1c"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="стили"), KeyboardButton(text="материалы")],
        [KeyboardButton(text="инструменты"), KeyboardButton(text="временные периоды")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer(
        "Привет! Я помогу вам найти нужный термин из сферы искусства и дать ему толкование. Выберите что вас интересует:",
        reply_markup=keyboard
    )

# Обработчик нажатий на кнопки
@dp.message(F.text.in_({"стили", "материалы", "инструменты", "временные периоды"}))
async def recommend_books(message: Message):
    level = message.text
    if level == "стили":
        books = "1. Easy Stories in English\n2. English Short Stories for Beginners"
    elif level == "материалы":
        books = "1. Harry Potter and the Philosopher's Stone\n2. Animal Farm by George Orwell"
    elif level == "инструменты":
        books = "1. Harry Potter and the Philosopher's Stone\n2. Animal Farm by George Orwell"
    else:  # временные периоды
        books = "1. 1984 by George Orwell\n2. Brave New World by Aldous Huxley"

    await message.answer(f"Рекомендуемые книги для уровня {level}:\n{books}")

# Главная функция для запуска бота
async def main():
    # Регистрация обработчиков
    dp.message.register(send_welcome, F.text == "/start")
    dp.message.register(recommend_books, F.text.in_({"материалы", "инструменты", "временные периоды"}))

    # Удаление старого webhook и запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
