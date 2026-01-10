"""
Модуль models.
Предназначен для создания моделей пользователя и выбранной программы обучения, который он(она) выберет.
Создаёт таблицу в базе данных
"""

from peewee import *
from datetime import datetime


db = SqliteDatabase('user.db')

class User(Model):
    user_id = IntegerField(unique=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    surname = CharField(null=True)
    age = IntegerField(null=True)
    phone_number = CharField(unique=True)
    created_at = DateTimeField(default=datetime.now)
    

    class Meta:
        database = db    # модель будет использовать базу данных 'user.db'


class Programme(Model):
    programme_name = CharField()
    user = ForeignKeyField(User, backref='programmes')
    request_date = DateTimeField(default=datetime.now)
    details = TextField(null=True)

    class Meta:
        database = db
