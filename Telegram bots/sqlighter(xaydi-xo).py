import sqlite3

class SQLighter:
    # Конструктор
    def __init__(self, database_file):
        # Подключение к базе данных и создание курсора
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscroptions(self, status = True):
        # Возвращяет всех активных подписчиков
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'table_name' WHERE 'status' = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        # Проверяет есть ли уже юзер в базе
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'table_name' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        # Добавляем нового подписчика в базу
        with self.connection:
            return self.cursor.execute("INSERT INTO 'table_name' (user_id, status) VALUES (?,?)", (user_id,status))

    def update_subscription(self, user_id, status):
        # Обновление статуса подписки
        return self.cursor.execute("UPDATE 'table_name' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def close(self):
        # Закрыть соеденение
        self.cursor.close()
        self.connection.close()