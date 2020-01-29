import sqlite3 as sql
base = sql.connect('database_test.db')
q = base.cursor()
#q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, passd varchar)''')
#base.commit()
un = str()
up = str()
while un != '-' or up != '-':
    un = input("Введите имя пользователя: ")
    up = input("Введите пароль пользователя: ")
    q.execute("INSERT INTO user (name, passd) VALUES ('%s', '%s')"%(un, up))
    base.commit()

print("Список пользователей:\n")
q.execute("SELECT * FROM user")
row = q.fetchone()

while row is not None:
    print("Name: ", row[1], "||| Password: ", row[2])
    row = q.fetchone()
q.close()
base.close()