import sqlite3

class SQL_people:

    # Конструктор который создает подключение к базе (SqlLite)
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавление человека в базу
    def add_id_in_base(self, telegram_id):
        with self.connection:
            if self.cursor.execute("SELECT telegram_id FROM people WHERE telegram_id == (?)", (telegram_id,)).fetchone() is None:
                self.cursor.execute("INSERT INTO people (telegram_id, vacancy_id) VALUES (?,?)", (telegram_id,-1, ))
                self.connection.commit()
            else:
                print("Человек уже есть в базе")

    # Рассылка
    def mailing(self):
        with self.connection:
            return self.cursor.execute("SELECT telegram_id FROM people WHERE id!=0").fetchall()

    def add_vacancy_id(self, telegram_id, vacancy_id):
        with self.connection:
            self.cursor.execute("UPDATE people SET vacancy_id = (?) WHERE telegram_id = (?)", (vacancy_id, telegram_id, ))
            self.connection.commit()

    def select_vacancy_id_for_telegram_id(self, telegram_id):
        with self.connection:
            return self.cursor.execute("SELECT vacancy_id FROM people WHERE telegram_id = (?)", (telegram_id, )).fetchone()

    # Закрываем соедение с базой
    def sql_close(self):
        self.cursor.close()
        self.connection.close()

class SQL_vacancy:

    # Конструктор который создает подключение к базе (SqlLite)
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавление вакансии в базу
    def add_vacancy(self, category, name, description, salary):
        with self.connection:
            self.cursor.execute("INSERT INTO vacancy (category, name, description, salary) VALUES (?,?,?,?)", (category, name, description, salary))
            self.connection.commit()

    # Удаление вакансии из базы
    def delete_vacancy(self, category, name):
        with self.connection:
            self.cursor.execute("DELETE FROM vacancy WHERE category = (?) AND name = (?)",(category, name, ))
            self.connection.commit()

    # Достаем всю информацию о вакансиях по категории
    def select_vacancy_for_category(self, category):
        with self.connection:
            return self.cursor.execute("SELECT * FROM vacancy WHERE category = (?)", (category, )).fetchall()

    def select_vacancy_for_vacancy_id(self, vacancy_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM vacancy WHERE id = (?)", (vacancy_id, )).fetchone()

    # Закрываем соедение с базой
    def sql_close(self):
        self.cursor.close()
        self.connection.close()

class SQL_category:

    # Конструктор который создает подключение к базе (SqlLite)
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавление категории в базу
    def add_category(self, name):
        with self.connection:
            self.cursor.execute("INSERT INTO category (name) VALUES (?)",(name, ))
            self.connection.commit()

    # Удаление категории из базы
    def delete_category(self, name):
        with self.connection:
            self.cursor.execute("DELETE FROM category WHERE name = (?)", (name,))
            self.connection.commit()

    # Достаем все категории
    def select_all_category(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM category").fetchall()

    # Закрываем соедение с базой
    def sql_close(self):
        self.cursor.close()
        self.connection.close()






















class SQL_product:

    # Конструктор который создает подключение к базе (SqlLite)
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавляем товар в базу (/add)
    def sql_add_product(self, name, description, prise, photo_id, count):
        with self.connection:
            self.cursor.execute("INSERT INTO product (name, description, prise, photo_id, count) VALUES (?,?,?,?,?)",(name, description, prise,photo_id, count, ))
            self.connection.commit()

    # Удаляем товар из базы (/delete)
    def sql_delete_product(self, name, prise):
        with self.connection:
            self.cursor.execute("DELETE FROM product WHERE name = ? AND prise = ?", (name, prise, ))
            self.connection.commit()

    # Достаем все товары из базы (для вывода Списка товаров)
    def sql_select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product").fetchall()

    # Достаем товар по его id
    def sql_select_for_id(self, id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product WHERE id = ?", (id, )).fetchone()

    # Достаем количество товара по его id
    def sql_select_count_for_id(self, id):
        with self.connection:
            return self.cursor.execute("SELECT count FROM product WHERE id = ?", (id, )).fetchone()

    # Меняем название товара по его id
    def sql_change_name_for_id(self, id, name):
        with self.connection:
            self.cursor.execute("UPDATE product SET name = ? WHERE id = ?", (name, id, ))
            self.connection.commit()

    # Меняем описание товара по его id
    def sql_change_description_for_id(self, id, description):
        with self.connection:
            self.cursor.execute("UPDATE product SET description = ? WHERE id = ?", (description, id, ))
            self.connection.commit()

    # Меняем цену товара по его id
    def sql_change_prise_for_id(self, id, prise):
        with self.connection:
            self.cursor.execute("UPDATE product SET prise = ? WHERE id = ?", (prise, id, ))
            self.connection.commit()

    # Меняем photo_id товара по его id
    def sql_change_photo_id_for_id(self, id, photo_id):
        with self.connection:
            self.cursor.execute("UPDATE product SET photo_id = ? WHERE id = ?", (photo_id, id, ))
            self.connection.commit()

    # Меняем количество товара по его id
    def sql_change_count_for_id(self, id, count):
        with self.connection:
            self.cursor.execute("UPDATE product SET count = ? WHERE id = ?", (count, id, ))
            self.connection.commit()

    # Закрываем соедение с базой
    def sql_close(self):
        self.cursor.close()
        self.connection.close()

class SQL_shop:

    # Конструктор который создает подключение к базе (SqlLite)
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Добавляем товар в Корзину
    def sql_add(self, telegram_id, name, prise, count, total):
        with self.connection:
            self.cursor.execute("INSERT INTO shop (telegram_id, name, prise, count, total) VALUES (?,?,?,?,?)",(telegram_id, name, prise, count, total, ))
            self.connection.commit()

    # Достаем всю Корзину ( ??? Нужно ли ??? )
    def sql_select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM shop")

    # Достаем все товары по telegram_id человка
    def sql_select_all_for_telegram_id(self, telegram_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM shop WHERE telegram_id = ?", (telegram_id, )).fetchall()

    # Удаляем все товары по telegram_id человека (кнопка Очистка корзины)
    def sql_delete_all_for_telegram_id(self, telegram_id):
        with self.connection:
            self.cursor.execute("DELETE FROM shop WHERE telegram_id = (?)", (telegram_id, ))

    # Удаляем товар по его id
    def sql_delete_for_id(self, id):
        with self.connection:
            self.cursor.execute("DELETE FROM shop WHERE id = ?", (id, ))

    # Закрываем соедение с базой
    def sql_close(self):
        self.cursor.close()
        self.connection.close()