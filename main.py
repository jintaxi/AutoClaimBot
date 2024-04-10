from datetime import datetime, timedelta
from telethon import TelegramClient, events
from dotenv import load_dotenv
from os import getenv
from asyncio import sleep


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

# Создаем клиент Telethon
client = TelegramClient('session_name', api_id, api_hash)

async def main():

    # Получаем текущее время
    now = datetime.now()

    # Рассчитываем время следующего запуска
    next_run = (now + timedelta(hours=1, seconds=3))

    # Вычисляем время ожидания до следующего запуска
    wait_time = (next_run - now).total_seconds()
    
    # Активируем клиента
    await client.start(phone_number)

    # Получаем диалог с ботом
    dialog = await client.get_entity(chat_link)

    # Получаем сообщение по ID
    message = await client.get_messages(dialog, ids=ids)

    # Вызываем CallBack get_coins
    await message.click(data=callback)

    # Ожидание до следующего запуска
    await sleep(wait_time)

with client:
    client.loop.run_until_complete(main())