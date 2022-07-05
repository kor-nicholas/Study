using Cats.DAL.Interfaces;
using Cats.DAL.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;

namespace Cats.DAL.Repositories.EfCore
{
    public class EfCoreCatRepository : ICatReporistory
    {
        //private static string _connectionString { get; } = "Server=localhost;Database=CatsDb;Trusted_Connection=True;";
        private IConfiguration _configuration;

        public EfCoreCatRepository(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public EfCoreCatRepository()
        {

        }

        /*
         * System.IO.InvalidDataException: 'Failed to load configuration from file 'D:\Programming\C#\HelloWorldWebAPI(Cat)\HelloWorldWebApi(Cat)\appsettings.json'.'
         * JsonReaderException: '{' is invalid after a value.Expected either ',', '}', or ']'. LineNumber: 8 | BytePositionInLine: 2.
         */

        private DbContextOptionsBuilder<CatsContext> CreateBuilder()
        {
            var builder = new DbContextOptionsBuilder<CatsContext>();
            builder.UseSqlServer(_configuration["MyConn"]);

            return builder;
        }

        public List<Cat> GetAll()
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                return context.Cats.ToList();
            }
        }

        public Cat GetById(int id)
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                return context.Cats.Single(cat => cat.Id == id);
            }
        }

        public int Post(Cat cat)
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                cat.Id = context.Cats.Count() + 1;
                context.Cats.Add(cat);
                context.SaveChanges();

                return context.Cats.Count();
            }
        }

        public void Delete(int id)
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                var cat = context.Cats.Single(cat => cat.Id == id);
                context.Cats.Remove(cat);
                context.SaveChanges();
            }
        }
        
        public void DeleteAll()
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                foreach (var item in context.Cats)
                {
                    context.Cats.Remove(item);
                }
                context.SaveChanges();
            }
        }

        public void Put(Cat cat)
        {
            using (var context = new CatsContext(CreateBuilder().Options))
            {
                var catFromBase = context.Cats.Single(localCat => localCat.Id == cat.Id); // linq - original link to object
                catFromBase.Name = cat.Name;
                catFromBase.DateBirthday = cat.DateBirthday;
                catFromBase.Color = cat.Color;

                context.SaveChanges();
            }
        }
    }

}
