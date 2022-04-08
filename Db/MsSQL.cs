using System;
using System.Data;
using System.Data.SqlClient;
using System.Text;

namespace HelloWorldWebAPI_Cat_.Study
{
    public class MsSQL
    {
        private static string ConnectionString { get; } = "Server=localhost;Database=cats;Trusted_Connection=True;";

        // Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword; - STANDART
        // Server=localhost;Database=cats;Trusted_Connection=True;

        private static void SqlClose()
        {
            /*// Вариант 1 

            SqlConnection connection = new SqlConnection(ConnectionString);

            SqlCommand command = new SqlCommand("SELECT * FROM cats", connection);

            var reader = command.ExecuteReader();

            connection.Open();

            reader.Close();
            command.Clone();
            connection.Close();

            // ----------------------------------------------------------------------------------------------------------------------------------

            // Вариант 2

            using (SqlConnection connection2 = new SqlConnection(ConnectionString))
            {
                using (SqlCommand command2 = new SqlCommand("SELECT * FROM cats", connection2))
                {
                    using (var reader2 = command2.ExecuteReader())
                    {

                    }
                }
            }*/
        }

        private void SqlExecute(SqlConnection connection)
        {
            SqlCommand command = new SqlCommand("SELECT TOP 100 * FROM cats", connection);

            var reader = command.ExecuteReader(); // для select чтобы получить результат

            if (reader.HasRows) // проверка что пришли строки
            {
                while (reader.Read()) // построчное чтение таблицы, пока есть строки - цикл работает 
                {
                    int someindex = 0;
                    Console.WriteLine(reader[someindex]); // возможность работать как с массивом

                    reader.GetBoolean(0); // взять bool значение из колонки 1
                    reader.GetChar(1); // взять строку (либо 1 char, тут не знаю ??? ) из колонки 2  
                    reader.GetDateTime(2); // взять дату из колонки 3  
                    reader.GetValue(3); // достать какое-то значение из колонки 4

                    int id = reader.GetInt32(0);
                    string name = reader.GetString(1);
                    //DateTime datebirthday = new DateTime(reader.GetString(2));
                    string dateBirthday = reader.GetString(2);
                    string color = reader.GetString(3);

                    Console.WriteLine($"id: {id} ; name: {name} ; datebirthday: {dateBirthday} ; color: {color}");
                }
            }
        }

        private static void SqlParameters(SqlConnection connection, string exampleStringParameter, int exampleIntParameter, DateTime examplaDateTimeParameter)
        {
            SqlCommand command = new SqlCommand("SELECT * FROM cats WHERE id < @limit", connection);

            command.Parameters.AddWithValue("@limit", 10);// DECLARE @limit INT 10 ; потом его в sql-запросе можно просто юзать как переменную @limit
            // Безопасная передача параметров от Sql-Injection (либо DECLARE либо через Parameters.Add / Parameters.AddWithValue)

            char[] year = { '1', '9', '9', '1' };
            command.Parameters.Add("@year", SqlDbType.Char, 4).Value = year;

            command.Parameters.Add("@date", SqlDbType.DateTime).Value = examplaDateTimeParameter;

            command.Parameters.Add("@limit", SqlDbType.Int).Value = exampleIntParameter;

            command.Parameters.Add("@stringParameter", SqlDbType.Text).Value = exampleStringParameter;

            var parameter = new SqlParameter("@limit", exampleIntParameter);
            command.Parameters.Add(parameter);

            parameter = new SqlParameter
            {
                ParameterName = "@limit",
                Value = exampleIntParameter,
                SqlDbType = SqlDbType.Int
            };
            command.Parameters.Add(parameter);


        }

        private static void SqlInsertUpdateDelete(SqlConnection connection)
        {
            SqlCommand command = new SqlCommand("INSERT INTO cats (id, name, dateBirthday, color) VALUES (1, 'Vasya', '01.01.1991', 'green')", connection);

            command.ExecuteNonQuery(); // просто выполнить команду (для таких sql-запросов как INSERT, UPDATE, DELETE)
        }
    }
}

