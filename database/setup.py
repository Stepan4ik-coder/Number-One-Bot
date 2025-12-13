from .models import User, Programme, db

print("Создаю базу...")
db.connect()
db.create_tables([User, Programme])
print("Готово!")
db.close()