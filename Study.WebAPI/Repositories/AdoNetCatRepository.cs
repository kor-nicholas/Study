using Cats.DAL.Interfaces;
using Cats.DAL.Models;
using System.Data.SqlClient;

namespace Cats.DAL.Repositories
{
    public class AdoNetCatRepository : ICatReporistory
    {
        private static string ConnectionString { get; } = "Server=localhost;Database=CatsDb;Trusted_Connection=True;";
        private SqlConnection connection { get; } = new SqlConnection(ConnectionString);

        public AdoNetCatRepository()
        {
            connection.Open();
        }

        private void _closeConnection()
        {
            connection.Close();
        }

        public List<Cat> GetAll()
        {
            List<Cat> localList = new List<Cat>();

            SqlCommand command = new SqlCommand("SELECT * FROM cats;", connection);

            using (var reader = command.ExecuteReader())
            {
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        localList.Add(new Cat(reader.GetInt32(0), reader.GetString(1), reader.GetDateTime(2), reader.GetString(3)));
                    }
                }
            }



            return localList;
        }

        public Cat GetById(int id)
        {
            Cat localCat;

            SqlCommand command = new SqlCommand("SELECT id, name, birthday, color FROM cats WHERE id = @id", connection);

            command.Parameters.AddWithValue("@id", id);

            using (var reader = command.ExecuteReader())
            {
                if (reader.HasRows)
                {
                    reader.Read();

                    localCat = new Cat(reader.GetInt32(0), reader.GetString(1), reader.GetDateTime(2), reader.GetString(3));

                    _closeConnection();

                    return localCat;
                }
                else
                {
                    throw new Exception("Id isn't correct or dataBase hasn't the id");
                }
            }
        }

        public int Post(Cat cat)
        {
            SqlCommand command = new SqlCommand("SELECT MAX(id) FROM cats", connection);

            var reader = command.ExecuteReader();

            reader.Read();

            int newId = reader.GetInt32(0) + 1;

            reader.Close();

            command = new SqlCommand("INSERT INTO cats VALUES (@id, @name, @DateBirthday, @color)", connection);

            command.Parameters.AddWithValue("@id", newId);
            command.Parameters.AddWithValue("@name", cat.Name);
            command.Parameters.AddWithValue("@birthday", cat.DateBirthday);
            command.Parameters.AddWithValue("@color", cat.Color);

            command.ExecuteNonQuery();

            _closeConnection();

            return newId;
        }
        public void Delete(int id)
        {
            SqlCommand command = new SqlCommand("DELETE FROM cats WHERE id = @id", connection);

            command.Parameters.AddWithValue("@id", id);

            command.ExecuteNonQuery();

            _closeConnection();
        }

        public void Put(Cat cat)
        {
            SqlCommand command = new SqlCommand("UPDATE cats SET name = @name, DateBirthday = @birthday, color = @color WHERE id = @id", connection);

            command.Parameters.AddWithValue("@id", cat.Id);
            command.Parameters.AddWithValue("@name", cat.Name);
            command.Parameters.AddWithValue("@birthday", cat.DateBirthday);
            command.Parameters.AddWithValue("@color", cat.Color);

            command.ExecuteNonQuery();

            _closeConnection();
        }
    }
}
