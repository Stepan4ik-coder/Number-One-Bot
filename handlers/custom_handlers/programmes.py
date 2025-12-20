from telebot.types import Message
from loader import bot
from keyboards.reply import buttons
from .button_text import MAIN_PROGRAMME, STATES_EXAM, ADDITIONAL_PROGRAMME


@bot.message_handler(commands=['programmes'])
def show_buttons(message: Message):
    bot.send_message(
        message.chat.id,
        '🎓 **Про какую программу обучения хотите получить информацию?**',
        reply_markup=buttons(),
        parse_mode='Markdown'
    )


@bot.message_handler(func=lambda m: m.text in ('📘 Основная программа', '📚 Подготовка к ОГЭ и ЕГЭ', '🌟 Дополнительная программа'))
def each_buttons(message):
    if message.text == '📘 Основная программа':
        bot.send_message(message.chat.id, f'📘 **Основная программа**\n\n{MAIN_PROGRAMME}', parse_mode='Markdown')
    elif message.text == '📚 Подготовка к ОГЭ и ЕГЭ':
        bot.send_message(message.chat.id, f'📚 **Подготовка к ОГЭ и ЕГЭ**\n\n{STATES_EXAM}', parse_mode='Markdown')
    elif message.text == '🌟 Дополнительная программа':
        bot.send_message(message.chat.id, f'🌟 **Дополнительная программа**\n\n{ADDITIONAL_PROGRAMME}', parse_mode='Markdown')







