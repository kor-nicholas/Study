"""
SHOW DATABASES - просмотр всех баз данных на сервере
CREATE DATABASE - создание базы данных
USE <name_database> - использовать, для дальнейшей работы с базой данных
SOURCE <file.sql> - выполнение несколько SQL-команд из файла
DROP DATABASE - удаление базы данных
SHOW TABLES - просмот всех таблиц

CREATE TABLE <table_name> (
name1 type,
name2 type,
PRIMARY KEY (name1) - первичный ключ (уникальное поле)
FOREIGN KEY (name1) REFERENCES table_name (name2) - внешний ключ
);

type :
INT - число
VARCHAR() - строка (максимум 255 символов), в скобках количество символов
TEXT - большой текст
DATE - формат для работы с датой
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY - для поля id
либо же в самом конце : PRIMARY KEY(id)

ALTER TABLE <table_name> ADD <name> <type> - добавить поле <name> в таблицу <table_name>
ALTER TABLE <table_name> CHANGE <name> <type> - изменить поле <name> в таблице <table_name>

DESCRIBE <table_name> - просмотр информации о столбцах таблицы (тип и так далее...)

INSERT INTO <table_name> - добавление данных в таблицу
INSERT INTO <table_name> (name1, name2, name3) VALUES (value1, value2, value3)
INSERT INTO <table_name> VALUES (value1, valu2, value3)

UPDATE <table_name> SET <name1> = <value1>, <name2> = <value2>, ... - обновить данные в таблице
DELETE FROM <table_name> WHERE <условие>- удаление данных из таблицы (DROP TABLE <table_name> - удаление целой таблицы)
TRUNCATE <table_name> - удаление всех полей в таблице

SELECT <name1> FROM <table_name> - получить данные из таблицы
SELECT * FROM <table_name> - взять все данные из таблицы
SELECT DISTINCT <name1> FROM <table_name> - получение неповторяющихся данных

WHERE - условие (так-же можно совмещать с AND, OR, NOT)
SELECT <name1> FROM <table_name> WHERE <условие>
SELECT * FROM users WHERE id>0

GROUP BY - сортировка данных
SELECT <name1>, <name2> FROM <table_name> DROUP BY <name2> - групировка по name2

HAVING - так же как WHERE, но более интересно
SELECT <name1>, <name2> FROM <table_name> GROUP BY <name2> HAVING COUNT либо MAX , ... <name1> > 1

ORDERED BY - сортировка по возрастанию / убыванию
SELECT <name1>, <name2> FROM <table_name> ORDERED BY <name1>, <name2> - по возрастанию
SELECT <name1>, <name2> FROM <table_name> ORDERED BY <name1>, <name2> DESC - по убыванию

BETWEEN - для выбора из промежутка
SELECT <name1>, <name2> FROM <table_name> WHERE <nameX> BETWEEN <value1> AND <value2>
Пример
Выведем список инструкторов, чья зарплата больше 50 000, но меньше 100 000:

SELECT * FROM instructor
  WHERE salary BETWEEN 50000 AND 100000;

------------------------------------ ПРАВИЛЬНАЯ ПОДСТАНОВКА АРГУМЕНТОВ В SQL-ЗАПРОС ------------------------------------

# C подставновкой по порядку на места знаков вопросов:
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", ('2'))

# И с использованием именнованных замен:
cursor.execute("SELECT Name from Artist ORDER BY Name LIMIT :limit", {"limit": 3})

Пример SQLite3 :
def select_user_data(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM user_data Where user_id= :0", {'0': user_id}).fetchone()

------------------------------------- ПРИМЕР РАБОТЫ В ПИТОН БОТЕ (MySQL)-------------------------------------------------------

import mysql.connector
from mysql.connector import Error

def create_connect_mysql():
    try:
        connection_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1Kolya45"
        )
        print("Подключение к базе произошло успешно")
    except Error as db_connect_error:
        print(f"Произошла ошибка подключения : {db_connect_error}")
    return connection_db

conn = create_connect_mysql()
cursor = conn.cursor()

cursor.execute("USE bot;")
cursor.execute("INSERT INTO users (chat_id, name, username) VALUES (7853985, 'Kostya', '@kostyabog145');")
cursor.execute("INSERT INTO photo (photo_id) VALUES (8743894);")
data_user = cursor.execute("SELECT * FROM users;")
data_photo = cursor.execute("SELECT * FROM photo;")
conn.commit()

cursor.close()
conn.close()

print(f"Работа программы завершена, \nДанные юзера : {data_user}\nДанные фото : {data_photo}")

------------------------------------------------- SQLite3 --------------------------------------------------------------

sqlite3 example.db - зайти в базу

Настройки для красивого вывода :
.headers ON
.mode column

.tables - все таблицы в базе
.cshema <table_name> - просмотр структуры таблицы

sqlite3.connect('database_name.db')

conn.commit() - подтверждение
conn.rallback() - откаменяет последнее conn.commit()
conn.execute("SQL-запрос")
conn.backup - создает резервную копию базы данных
conn.close() - закрывает соедение с базой

cursor.execute("SQL-запрос")
cursor.fetchone() - берет данные (только 1) из запроса (например : "SELECT")
cursor.fetchmany() - берет данные (столько, сколько указано данных) из запроса (например : "SELECT")
cursor.fetchall() - берет данные (все, возвращает список всех данных) из запроса (например : "SELECT")
cursor.close() - закрывает cursor
------------------------------------------------------------------------------------------------------------------------
"""