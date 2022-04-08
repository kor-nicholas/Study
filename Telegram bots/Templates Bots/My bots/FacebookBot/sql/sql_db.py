import sqlite3

class SQL_people:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def add_id_in_base(self, id):
        with self.connection:
            if self.cursor.execute("SELECT telegram_id FROM people WHERE telegram_id == (?)", (id,)).fetchone() is None:
                self.cursor.execute("INSERT INTO people (telegram_id) VALUES (?)", (id,))
                self.connection.commit()
            else:
                print("Человек уже есть в базе")

    def change_file_id_to_pluss_for_telegram_id(self, telegram_id):
        with self.connection:
            self.cursor.execute("UPDATE people SET file_id = '+' WHERE telegram_id = ?", (telegram_id, ))
            self.connection.commit()

    def change_file_id_to_minuss_for_telegram_id(self, telegram_id):
        with self.connection:
            self.cursor.execute("UPDATE people SET file_id = '-' WHERE telegram_id = ?", (telegram_id, ))
            self.connection.commit()

    def select_telegram_id_for_file_id(self, file_id):
        with self.connection:
            return self.cursor.execute("SELECT telegram_id FROM people WHERE file_id = ?", (file_id, )).fetchall()

    def mailing(self):
        with self.connection:
            return self.cursor.execute("SELECT telegram_id FROM people WHERE id!=0").fetchall()

    def sql_close(self):
        self.cursor.close()
        self.connection.close()

class SQL_product:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def sql_add_product(self, name, description, prise, photo_id, count):
        with self.connection:
            self.cursor.execute("INSERT INTO product (name, description, prise, photo_id, count) VALUES (?,?,?,?,?)",(name, description, prise,photo_id, count, ))
            self.connection.commit()

    def sql_delete_product(self, name, prise):
        with self.connection:
            self.cursor.execute("DELETE FROM product WHERE name = ? AND prise = ?", (name, prise, ))
            self.connection.commit()

    def sql_select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product").fetchall()

    def sql_select_for_id(self, id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product WHERE id = ?", (id, )).fetchone()

    def sql_select_count_for_id(self, id):
        with self.connection:
            return self.cursor.execute("SELECT count FROM product WHERE id = ?", (id, )).fetchone()

    def sql_change_name_for_id(self, id, name):
        with self.connection:
            self.cursor.execute("UPDATE product SET name = ? WHERE id = ?", (name, id, ))
            self.connection.commit()

    def sql_change_description_for_id(self, id, description):
        with self.connection:
            self.cursor.execute("UPDATE product SET description = ? WHERE id = ?", (description, id, ))
            self.connection.commit()

    def sql_change_prise_for_id(self, id, prise):
        with self.connection:
            self.cursor.execute("UPDATE product SET prise = ? WHERE id = ?", (prise, id, ))
            self.connection.commit()

    def sql_change_photo_id_for_id(self, id, photo_id):
        with self.connection:
            self.cursor.execute("UPDATE product SET photo_id = ? WHERE id = ?", (photo_id, id, ))
            self.connection.commit()

    def sql_change_count_for_id(self, id, count):
        with self.connection:
            self.cursor.execute("UPDATE product SET count = ? WHERE id = ?", (count, id, ))
            self.connection.commit()

    def sql_close(self):
        self.cursor.close()
        self.connection.close()

class SQL_shop:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def sql_add(self, telegram_id, name, prise, count, total):
        with self.connection:
            self.cursor.execute("INSERT INTO shop (telegram_id, name, prise, count, total) VALUES (?,?,?,?,?)",(telegram_id, name, prise, count, total, ))
            self.connection.commit()

    def sql_select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM shop")

    def sql_select_all_for_telegram_id(self, telegram_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM shop WHERE telegram_id = ?", (telegram_id, ))

    def sql_delete_all(self, telegram_id):
        with self.connection:
            self.cursor.execute("DELETE FROM shop WHERE telegram_id = ?", (telegram_id, ))

    def sql_delete_for_id(self, id, telegram_id):
        with self.connection:
            self.cursor.execute("DELETE FROM shop WHERE id = ? AND telegram_id = ?", (id, telegram_id, ))

    def sql_close(self):
        self.cursor.close()
        self.connection.close()