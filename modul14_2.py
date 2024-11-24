import sqlite3
                   # Создаем и подключаемся к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

                    # Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
                # Заполняем таблицу Users 10 записями
# for i in range(1, 11):
#     cursor.execute("""
# INSERT INTO Users(username, email, age, balance)
# VALUES(?, ?, ?, ?)
# """,
#  (f"User{i}", f'example{i}@gmail.com', i * 10, 1000))

            # Обновляем balance у каждой 2-й записи на 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

                # Удаляем каждую 3-ю запись
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
            # Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")
        # Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
            # Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances/total_users)

    
connection.commit()
connection.close()