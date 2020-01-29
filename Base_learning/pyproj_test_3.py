import sqlite3 as sql
import random as r
import matplotlib.pyplot as plt

def create_table (db_name,table_name):
    con = sql.connect(db_name)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS %s (id int auto_increment primary key, rnd FLOAT)'''%(table_name))
    con.commit()
    return con, cur

def change_bd_ex(con, cur, table_name, a):
    cur.execute("INSERT INTO %s (rnd) VALUES ('%f')"%(table_name, a))
    con.commit()
    pass

def med_filt(data, w = 2):
    s = 0
    w = int(w)
    i_count = int(w / 2) - 1
    data_new = data
    while i_count < len(data) - w / 2 - 1:
        left = int(i_count - w / 2 + 1)
        right = int(i_count + w / 2)
        for j in range(left, right + 1, 1):
            s += data[j]
        data_new[i_count] = s / w
        s = 0
        i_count += 1
    return data_new

c_of_ex = 10
i = 0
w = 20
bd_name = "test_database_random.db"
table_1 = "rand_table"
table_2 = "rand_table_filt"
con_cur = create_table(bd_name, table_1)
while i < c_of_ex:
    i += 1
    d = float(r.randint(0, 100))
    change_bd_ex(con_cur[0], con_cur[1],table_1, d)

con = con_cur[0]
cur = con_cur[1]
cur.execute('SELECT * FROM %s'%(table_1))
row = cur.fetchall()
rand_data = []
i_x = []
i = 0
while i < len(row):
    rand_data.append(row[i][1])
    i_x.append(i)
    i += 1
f = plt.figure(1)
plt.plot(i_x, rand_data)
f_med = plt.figure(2)
rand_data_filt = med_filt(rand_data, w)
plt.plot(i_x, rand_data_filt)
plt.show()

i = 0
create_table(bd_name, table_2)
while i < len(rand_data_filt):
    change_bd_ex(con, cur, table_2, rand_data_filt[i])
    i += 1


