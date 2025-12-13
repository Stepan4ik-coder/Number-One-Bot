from telebot.types import Message
from loader import bot
from keyboards.reply import buttons
from .button_text import MAIN_PROGRAMME, STATES_EXAM, ADDITIONAL_PROGRAMME


@bot.message_handler(commands=['programmes'])
def show_buttons(message: Message):
    bot.send_message(
        message.chat.id,
        '🎓 Про какую программу обучения хотите получить информацию?',
        reply_markup=buttons()
    )


@bot.message_handler(func=lambda m: m.text in ('Основная программа', 'Подготовка к ОГЭ и ЕГЭ', 'Дополнительная программа'))
def each_buttons(message):
    if message.text == 'Основная программа':
        bot.send_message(message.chat.id, f'📘 {MAIN_PROGRAMME}')
    elif message.text == 'Подготовка к ОГЭ и ЕГЭ':
        bot.send_message(message.chat.id, f'📚 {STATES_EXAM}')
    elif message.text == 'Дополнительная программа':
        bot.send_message(message.chat.id, f'🌟 {ADDITIONAL_PROGRAMME}')







