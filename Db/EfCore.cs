using Cats.DAL.Models;
using Microsoft.EntityFrameworkCore;

namespace HelloWorldWebApi_Cat_.Study
{
    public class EfCore
    {
        /*
         * ORM - связывает базу и код (framework-и) 
         * 
         * Подходы создания базы / проекта в Ef Core: 
         * 1. Code-First - сначала создаем модели, потом создается база (таблицы)
         * 2. Module-First - рисуешь модели, нарисовал связи, потом генерируется база и код
         * 3. Database-First - есть база, к ней делается приложение (Ef Core генерируеи модели на основе базы)
         * 
         * 
         */
    }

    public class TestClass
    {
        private static string _connectionString { get; } = "Server=localhost;Database=CatsDb;Trusted_Connection=True;";

        static async void Main(string[] args)
        {
            var builder = new DbContextOptionsBuilder<CatContext>();
            builder.UseSqlServer(_connectionString); // тут выбираем сервер (для каждой базы разный : PostgresSql, MySql, SqlLite)
                                                     // После установки пакетов / библиотек сервера, builder их подгружает и можно выбрать интересующий сервер

            using (var context = new CatContext(builder.Options))
            {
                Cat cat = new Cat
                {
                    Id = 4,
                    Name = "Petya",
                    DateBirthday = DateTime.Now,
                    Color = "purpy",
                };

                context.Cats.Add(cat); // добавляем в локальную базу нового Cat (кота)
                context.SaveChanges(); // сохраняем в реальную базу из кешированной (нужно чтобы не нагружать основную базу)
                                       // то есть можно сделать сколько угодно изменений в локальной базе, потом командой Save все сохранить в реальную базу

                context.Attach(cat).State = EntityState.Added; // тоже самое добавление, но лучше юзать верхний способ

                var cats = new List<Cat>()
            {
                new Cat { Id = 5, Name = "test", DateBirthday = DateTime.Now, Color = "test"},
                new Cat { Id = 6, Name = "test2", DateBirthday = DateTime.Now, Color = "test2"},
            };

                context.Cats.AddRange(cats); // добавление коллекции
                context.SaveChanges();

                var localCat = context.Cats.Single(cat => cat.Id == 1); // достать Cat (кота) с Id == 1, с помощью LINQ
                localCat.Name = "other name"; // так как это ссылка на объект (так как юзается LINQ), то имя изменится в локальной базе
                context.SaveChanges(); // по-этому тут нужно сохранить изменения в реальной

                //Console.WriteLine(cat.GroupCats?.Name); // знак вопроса, чтобы если cat.GroupCats == null не вылетел Exception,
                                                        // а все выражение cat.GroupCats.Name == null (стало null)

                var cats2 = context.Cats.ToList(); // чтобы прочитать базу (достать всех Cat / котов)
                var cats3 = await context.Cats.ToListAsync(); // прочитать асинхронно

                var newCat = new Cat()
                {
                    Id = 5,
                    Name = "new Name"
                };

                context.Cats.Update(newCat); // обновляет в базе !!! по Id !!!, иначе создает новый объект в базе
                context.SaveChanges();
            }
        }
    }

    /* 
     * Работа с миграциями (если появились какие-то изменение, чтобы синхронизировать локальную и настоящую базы данных)
     * 
     * 1. View -> Other Windows -> Package Manager Console
     * 2. enable-migrations (после этого создается папка Migrations и файл миграций)
     * 3. add-migration AddGroupType (как коммит в git,пишется после всех изменений в базе, AddGroupType - имя "коммита")
     * 4. update-database (базы синхронизировались)
     * 
     * dotnet ef migrations add [migration name]
     */

    // Кешировання база данных, через которую Ef Core работает с реальной базой 
    public class CatContext : DbContext
    {
        //public CatContext() : base("ConnectionString") { } // еще один вариант подключения к базе (почему-то не работал)
        public CatContext(DbContextOptions<CatContext> options) : base(options) { } // стандартная схема создания Context
        public DbSet<Cat> Cats { get; set; } // Таблицы в базе данных (название таблицы как имя класс - Cats, 1 способ)

        //protected override void OnModelCreating(ModelBuilder modelBuilder)
        //{
        //    modelBuilder.ApplyConfiguration(new CatConfiguration()); // чтобы поменялось название таблицы

        //    base.OnModelCreating(modelBuilder);
        //}
    }

    //public class CatConfiguration : IEntityTypeConfiguration<Cat>
    //{
    //    public void Configure(EntityTypeBuilder<Cat> builder)
    //    {
    //        builder.ToTable("products"); // тоже свое название таблицы, 3 способ

    //        builder.HasKey(c => c.Id);

    //        builder.Property(c => c.Name)
    //            .HasMaxLength(20)
    //            .IsRequired(); // обязательное поле
    //    }
    //}

    //[Table("products")] // другое название таблицы, 2 способ
    //public class Cat
    //{
    //    public int Id { get; set; }
    //    public string Name { get; set; }
    //    public DateTime DateBirthday { get; set; }
    //    public string Color { get; set; }

    //    public Cat(int id, string name, DateTime birthday, string color)
    //    {
    //        Id = id;
    //        Name = name;
    //        DateBirthday = birthday;
    //        Color = color;
    //    }

    //    public Cat()
    //    {

    //    }
    //}
}
