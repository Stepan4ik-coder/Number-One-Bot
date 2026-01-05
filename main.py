from loader import bot
from utils.set_bot_commands import set_default_commands
from database.models import db, User, Programme
import handlers  # noqa
from flask import Flask
import threading


# Flask приложение
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Telegram bot is running!"

# Запускаем Flask в отдельном потоке
def run_web_server():
    app.run(host='0.0.0.0', port=10000, debug=False)

web_thread = threading.Thread(target=run_web_server, daemon=True)
web_thread.start()

db.connect()
db.create_tables([User, Programme], safe=True)

if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()
