from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(
        message, f"🤔 Не понимаю сообщение '{message.text}'... Попробуй /help 📚"
    )
