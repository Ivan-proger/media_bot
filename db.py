import sqlite3

try:
    con = sqlite3.connect('database1.db')
    cursor = con.cursor()

    with open('sql_request/user_creat.sql', 'r') as sqlite_file:
        user_creat = sqlite_file.read()

    cursor.executescript(user_creat)
    print("вроде работает")
    cursor.close()

except sqlite3.Error as error:
    print("все в *****", error)

finally:
    if (con):
        con.close()
        print("Соединение с SQLite закрыто")