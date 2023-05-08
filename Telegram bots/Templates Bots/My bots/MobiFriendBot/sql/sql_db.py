import sqlite3

class SQL_work:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def sql_add_product(self, name, category, description, prise, photo_id, code):
        with self.connection:
            self.cursor.execute("INSERT INTO product VALUES (?,?,?,?,?,?)",(name, category, description, prise,photo_id, code, ))
            self.connection.commit()
            return True

    def sql_delete_product(self, name, prise):
        with self.connection:
            self.cursor.execute("DELETE FROM product WHERE name = ? AND prise = ?", (name, prise, ))
            self.connection.commit()
            return True

    def sql_select_for_category(self, category):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product WHERE category = ?", (category,)).fetchall()

    def sql_select_for_code(self, code):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product WHERE code = ?", (code, ))

    def sql_select_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM product").fetchall()

    def sql_close(self):
        self.cursor.close()
        self.connection.close()