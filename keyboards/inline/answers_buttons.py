from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def gen_yes_and_no_answer_button(user_id):
    yes_button = InlineKeyboardButton(text='Да', callback_data=f'overwrite_yes: {user_id}')
    no_button = InlineKeyboardButton(text='Нет', callback_data=f'overwrite_no: {user_id}')

    keyboard = InlineKeyboardMarkup()
    keyboard.add(yes_button, no_button)

    return keyboard