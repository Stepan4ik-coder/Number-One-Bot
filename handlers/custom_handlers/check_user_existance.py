from loader import bot
from database import models
from keyboards.inline import gen_yes_and_no_answer_button
from .get_user_information import get_first_name

def check_exists(value_id, message):
    if models.User.select().where(models.User.user_id == value_id).exists():
        found_user = models.User.get_or_none(models.User.user_id == value_id)
        name_of_programme = models.Programme.select().where(models.Programme.user == found_user).first()
        if name_of_programme:
            name_of_programme = name_of_programme.programme_name
        else:
            name_of_programme = '❌ Не выбрано'
        keyboard = gen_yes_and_no_answer_button(user_id=value_id)

        bot.send_message(message.chat.id, f'⚠️ **Найден существующий пользователь!**\n\n'
                                          f'📅 **Дата создания:** {found_user.created_at}\n'
                                          f'🆔 **ID:** {found_user.user_id}\n'
                                          f'👤 **Имя:** {found_user.first_name if found_user.first_name else "❌ Не указано"}\n'
                                          f'📋 **Фамилия:** {found_user.surname if found_user.surname else "❌ Не указано"}\n'
                                          f'🎂 **Возраст:** {found_user.age if found_user.age else "❌ Не указано"}\n'
                                          f'📞 **Номер телефона:** {found_user.phone_number if found_user.phone_number and found_user.phone_number != "pending" else "❌ Не указано"}\n'
                                          f'🎓 **Выбранная программа обучения:** {name_of_programme}\n\n'
                                          f'❓ **Желаете перезаписать данные?**',
                                          reply_markup=keyboard,
                                          parse_mode='Markdown')
        return True
    return False


@bot.callback_query_handler(func=lambda callback_query:(callback_query.data.startswith('overwrite_yes')))
def overwriting_yes(callback_query):
    massive = callback_query.data.split(':')
    user_id_str = massive[1].strip()
    user_id = int(user_id_str)  # получаем ID
    username = callback_query.from_user.username  # получаем username
    phone_number = 'pending'  # получаем номер телефона

    found_user = models.User.get_or_none(models.User.user_id == user_id)
    chat_id = callback_query.message.chat.id

    models.Programme.delete().where(models.Programme.user == found_user).execute()
    models.User.delete().where(models.User.user_id == user_id).execute()
    models.User.create(user_id=user_id, username=username, phone_number=phone_number)

    bot.send_message(chat_id, '🎉 **Мы рады, что вы готовы присоединиться к Number One!**', parse_mode='Markdown')
    first_name = bot.send_message(chat_id, '👤 **Ваше имя (имя ребёнка):**', parse_mode='Markdown')
    bot.register_next_step_handler(first_name, get_first_name)  # ➡️ Переход к следующему шагу


@bot.callback_query_handler(func=lambda callback_query:(callback_query.data.startswith('overwrite_no')))
def overwriting_no(callback_query):
    massive = callback_query.data.split(':')
    user_id_str = massive[1].strip()
    user_id = int(user_id_str)  # получаем ID
    chat_id = callback_query.message.chat.id

    bot.send_message(chat_id, f'✅ **Данные пользователя с ID {user_id} сохранены без изменений!** 🎉', parse_mode='Markdown')

