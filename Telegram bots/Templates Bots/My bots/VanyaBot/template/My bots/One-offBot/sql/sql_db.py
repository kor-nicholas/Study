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
                self.cursor.execute("INSERT INTO people (telegram_id, read) VALUES (?,?)", (telegram_id,'-', ))
                self.connection.commit()
            else:
                print("Человек уже есть в базе")

    # Добавляем total по telegram_id
    def add_total_for_telegram_id(self, total, telegram_id):
        with self.connection:
            self.cursor.execute("UPDATE people SET total = (?) WHERE telegram_id = (?)", (total, telegram_id, ))
            self.connection.commit()

    def select_total_for_telegram_id(self, telegram_id):
        with self.connection:
            return self.cursor.execute("SELECT total FROM people WHERE telegram_id = (?)", (telegram_id, )).fetchone()

    # Рассылка
    def mailing(self):
        with self.connection:
            return self.cursor.execute("SELECT telegram_id FROM people WHERE id!=0").fetchall()

    # Меняем read (прочитал ли человек правила)
    def change_read_for_telegram_id(self, telegram_id):
        with self.connection:
            self.cursor.execute("UPDATE people SET read = '+' WHERE telegram_id = (?)", (telegram_id, ))
            self.connection.commit()

    # Достаем read по telegram_id
    def select_read_for_telegram_id(self, telegram_id):
        with self.connection:
            return self.cursor.execute("SELECT read FROM people WHERE telegram_id = (?)", (telegram_id, )).fetchone()

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