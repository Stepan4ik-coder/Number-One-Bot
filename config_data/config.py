import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print("Файл .env не найден, используем Environment Variables")


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    exit("Ошибка: BOT_TOKEN не найден! Добавь его в Environment Variables")

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота 🚀"),
    ("help", "Показать больше информации 💡"),
    ("join", "Присоединиться к Number One 👥"),
    ("staff_info", "Педагогический состав 👨‍🏫"),
    ("programmes", "Программы обучения 📚")
)
