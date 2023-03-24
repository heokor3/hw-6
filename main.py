#база данных
#sql язык структурированных данных
#субд система управления баз данных
#реляционные
#не реляционные
import sqlite3
from sqlite3 import Error
def create_conection(db_file):
    conn=False
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def create_student(conn,student):
    sql='''INSERT INTO student (name,mark,hobby,b_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor= conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)

def delete_student(conn, name):
    sql ='''DELITE FROM '''


def create_table(conn, sql):
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

data_base=r'puge.db'

def delete_student(conn):
    name = input("Введите имя студента, которого нужно удалить: ")
    sql = '''DELETE FROM student WHERE name = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        conn.commit()
        print("Студент успешно удален из базы данных")
    except Error as e:
        print(e)


def reed(conn):
    try:
        sql='''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)

def update_student(conn):
    name = input("Введите имя студента, которого нужно изменить: ")
    print("Введите новые данные студента:")
    new_name = input("Имя: ")
    new_mark = input("Оценка: ")
    new_hobby = input("Хобби: ")
    new_b_date = input("Дата рождения (гггг-мм-дд): ")
    new_is_married = input("Семейное положение (True/False): ")
    sql = '''UPDATE student SET name = ?, mark = ?, hobby = ?, b_date = ?, is_married = ? WHERE name = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_name, new_mark, new_hobby, new_b_date, new_is_married, name))
        conn.commit()
        print("Данные студента успешно изменены")
    except Error as e:
        print(e)

sql_create_table='''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (104) NOT NULL,
mark FLOAT NOT NULL DEFAULT  0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_conection(data_base)
# if connection is not None:
# create_student(connection,('бека',10.2,'пишет','2003-06-06',False))
while True:
    print("Выберите действие:")
    print("1. Показать список студентов")
    print("2. Обновить данные студента")
    print("3. Удалить студента из базы данных")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        reed(connection)
    elif choice == "2":
        update_student(connection)
    elif choice == "3":
        delete_student(connection)
    elif choice == "4":
        break
    else:
        print("Некорректный ввод, попробуйте еще раз")
