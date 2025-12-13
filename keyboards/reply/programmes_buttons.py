from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def buttons():
    # Создаем кнопку
    button_1 = KeyboardButton(text='Основная программа')
    button_2 = KeyboardButton(text='Подготовка к ОГЭ и ЕГЭ')
    button_3 = KeyboardButton(text='Дополнительная программа')

    # Объект клавиатуры
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3)

    return keyboard


