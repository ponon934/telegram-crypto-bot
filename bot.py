import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

# Токен, который ты получил от @BotFather (вставь его внутрь кавычек)
TOKEN = "8802376513:AAFma6UEZF7lMNeO_wQNiL7JsWSbpQ-VhPQ"

# Инициализируем бота и диспетчер (обработчик событий)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Словарь с курсами криптовалют (наша новая тема!)
# В реальной жизни эти данные берутся из интернета, но пока пропишем их вручную
crypto_rates = {
    "BTC": "102,400 USD (Примерно 4,250,000 грн)",
    "ETH": "2,650 USD (Примерно 110,000 грн)",
    "TON": "5.20 USD (Примерно 215 грн)",
    "USD":  "41.50 грн"
}

# Обработка команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я твой первый личный бот. Напиши команду /crypto, чтобы узнать актуальный курс, "
        "или /laptop, чтобы вспомнить параметры твоей цели!"
    )

# Обработка команды /crypto (используем наш словарь)
@dp.message(Command("crypto"))
async def cmd_crypto(message: types.Message):
    # Достаем данные из словаря crypto_rates
    text = (
        "📊 Актуальный курс криптовалют:\n\n"
        f"🪙 Bitcoin (BTC): {crypto_rates['BTC']}\n"
        f"🔷 Ethereum (ETH): {crypto_rates['ETH']}\n"
        f"💎 Toncoin (TON): {crypto_rates['TON']}\n"
        f"💵 Доллар (USD): {crypto_rates['USD']}"
    )
    await message.answer(text, parse_mode="Markdown")

# Обработка команды /laptop
@dp.message(Command("laptop"))
async def cmd_laptop(message: types.Message):
    await message.answer(
        "💻 Твоя цель: Gigabyte G6X\n"
        "🔧 Характеристики: Intel Core i7 / RTX 4060 8GB / 16GB RAM / 1TB SSD\n"
        "💰 Цена: ~37,000 грн\n\n"
        "Код — это сила, продолжай учиться и ноут будет твоим! 🚀"
    )

# Главная функция запуска бота
async def main():
    print("Бот успешно запущен и слушает команды...")
    await dp.start_polling(bot)

await main()