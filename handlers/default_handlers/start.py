from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")


# Общение с пользователем
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if (message.text.lower() == "Hello!"
            or message.text.lower() == "Hello"
            or message.text.lower() == "Привет!"
            or message.text.lower() == "Привет"
    ):

        bot.send_message(message.chat.id, "И тебе привет!")