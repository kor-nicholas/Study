using HtmlAgilityPack;
using LINQtoCSV; // Nuget (LinqToCsv) 

namespace Study.Parser
{
    public class Csv
    {

        public void Read()
        {
            var csvFileDescription = new csvFileDescription
            {
                FirstLineHasColumnNames = true, // игнорировать первый ряд
                IgnoreUnknowColumns = true,
                SeparatorChar = ',',
                UseFieldIndexForReadingData = true, // если установлены индексы в атрибуте моделей
            };

            var csvContext = new csvContext();
            var models = csvContext.Read<Model>("models.csv", csvFileDescription);

            foreach(var model in models)
            {
                Console.WriteLine($"Id: {model.Id}\nName: {model.Name}\nAge: {model.Age}\nDescription: {model.Description}\nDate: {model.Date}\n");
            }
        }

        public void Write()
        {
            var modelsList = new List<Model>
            {
                new Model{ Id = 1, Name = "testName1", Age = 35, Description = "testDesc1", Date = new DateTime().Now}
                new Model{ Id = 2, Name = "testName2", Age = 65, Description = "testDesc2", Date = new DateTime("12.12.2002")}
                new Model{ Id = 3, Name = "testName3", Age = 16, Description = "testDesc3", Date = new DateTime("2.1.1999")}
            };

            var csvFileDescription = new csvFileDescription
            {
                FirstLineHasColumnNames = true, // игнорировать первый ряд
                SeparatorChar = ','
            };

            var csvContext = new csvContext();
            csvContext.Write(modelsList, "models.csv", csvFileDescription);

            Console.WriteLine("CSV file Created");
        }

    }

    [Serializable]
    public class Model
        {
            [CsvColumn(Id = "id")] // 2 аргумент - FiendIndex(не выкупил зачем)
            public int Id { get; set; }

            [CsvColumn(Name = "name")]
            public string Name { get; set; }

            [CsvColumn(Age = "age")]
            public int Age { get; set; }

            [CsvColumn(Description = "description")]
            public string Description { get; set; }

            [CsvColumn(Date = "data", OutputFormat = "dd-MM-yyyy")] // dd-MM-yyyy HH:mm
            public DateTime Date { get; set; }
        }
}



