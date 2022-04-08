namespace HelloWorldWebAPI_Cat_.Study
{
    public class Sql
    {
        /*
         * CREATE TABLE <table_name> (
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
         */
    }
}
