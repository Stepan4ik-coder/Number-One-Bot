from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from database.models import db, User, Programme
db.connect()
db.create_tables([User, Programme], safe=True)

if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()
