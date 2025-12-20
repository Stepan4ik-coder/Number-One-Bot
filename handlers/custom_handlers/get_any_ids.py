from loader import bot

@bot.message_handler(commands=['getid'])
def get_group_id(message):
    """Получаем ID чата/группы"""
    chat_id = message.chat.id
    chat_type = message.chat.type  # 'group', 'supergroup', 'private'

    bot.reply_to(
        message,
        f"📊 ID этого чата: `{chat_id}`\n"
        f"📝 Тип чата: {chat_type}",
        parse_mode='Markdown'
    )

    # Также выводим в консоль
    print(f"🆔 ID чата: {chat_id}")
    print(f"📁 Тип: {chat_type}")
    print(f"👥 Название: {message.chat.title}")