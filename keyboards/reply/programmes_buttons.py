from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def buttons():
    # Создаем кнопки с эмодзи
    button_1 = KeyboardButton(text='📘 Основная программа')
    button_2 = KeyboardButton(text='📚 Подготовка к ОГЭ и ЕГЭ')
    button_3 = KeyboardButton(text='🌟 Дополнительная программа')

    # Объект клавиатуры с настройками
    keyboard = ReplyKeyboardMarkup(
        row_width=2,  # Максимум 2 кнопки в строке
        resize_keyboard=True,  # Автоматически подстраивает размер под экран
        one_time_keyboard=True  # Скрывает клавиатуру после нажатия (опционально)
    )

    # Добавляем кнопки в две строки
    keyboard.add(button_1, button_2)
    keyboard.add(button_3)

    return keyboard


