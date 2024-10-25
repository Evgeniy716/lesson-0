import sqlite3



connection =sqlite3.connect('not_telegramm.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    
''')
cursor.execute('''DELETE FROM Users''')

for num  in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)",
                   (f"User{num}",f"example{num}@gmail.com",num * 10, 1000))
for num in range(1,11,2):
    cursor.execute("UPDATE Users SET balance =? WHERE age =?",(500, 10 * num))

for user_id in range(1,11,3):
    cursor.execute("DELETE FROM Users WHERE id =?",(user_id,))

connection.commit()
cursor.execute("SELECT * FROM Users WHERE age !=60")

for i in cursor.fetchall():
    print(f"Имя:{i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс{i[4]}")
    connection.close()


