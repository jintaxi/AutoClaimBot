from datetime import datetime, timedelta
from telethon import TelegramClient
from dotenv import load_dotenv
from os import getenv
from asyncio import sleep
from loguru import logger


# Загружаем переменные окружения из файла .env
load_dotenv()

# Необходимо создать файл .env, куда записать данные ваших переменных
api_id = int(getenv('API_ID'))  # Ваш API ID
api_hash = getenv('API_HASH')  # Ваш API Hash
phone_number = getenv('PHONE_NUMBER')  # Ваш номер телефона

# Ваши ссылки на бота, номер сообщения и callback
chat_link = 'https://t.me/nastyanovelbot'
ids = 466_073
callback = 'get_coins'
session_name = "jintaxi" # Change on your and in docker compose file

# Создаем клиент Telethon
client = TelegramClient(f'{session_name}', api_id, api_hash)

async def main():
    iteration = 1
    while True:
        # Информация о номере запуска
        logger.info(f"Ожидание завершено. Начало итерации №{iteration}")
        iteration += 1

        # Получаем текущее время
        now = datetime.now()

        # Рассчитываем время следующего запуска
        next_run = (now + timedelta(hours=1, seconds=2))

        # Вычисляем время ожидания до следующего запуска
        wait_time = (next_run - now).total_seconds()
        
        # Активируем клиента
        await client.start(phone_number)
        logger.info("Сессия телеграм начата")

        # Получаем диалог с ботом
        dialog = await client.get_entity(chat_link)
        logger.info("Диалог найден")

        # Получаем сообщение по ID
        message = await client.get_messages(dialog, ids=ids)
        logger.info("Сообщение получено")

        # Вызываем CallBack get_coins
        await message.click(data=callback)
        logger.info("CallBack активирован")

        # Ожидание до следующего запуска
        logger.info(f"Начинаю ожидание")
        await sleep(wait_time)


with client:
    client.loop.run_until_complete(main())

