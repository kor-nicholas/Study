using ParserBot.Abstractions;
using ParserBot.Models;

namespace ParserBot.Services
{
    public class DataService : IDataService
    {
        private readonly ILogger _logger;
        private int i;
        private int j;

        public DataService(ILogger<DataService> logger)
        {
            i = int.Parse(File.ReadAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsCars.txt"));
            j = int.Parse(File.ReadAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsVacancy.txt"));

            _logger = logger;
        }

        /// <summary>
        /// Достать объявления машин из json
        /// </summary>
        /// <returns>Коллекция машин</returns>
        public List<Car> GetCarsFromJson()
        {
            string path = "D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\json";
            return File.Exists($"{path}\\car{i}.json") ? Newtonsoft.Json.JsonConvert.DeserializeObject<List<Car>>(File.ReadAllText($"{path}\\car{i}.json")) : throw new FileNotFoundException("[GetAddsWithJson] Json file for car not found");
        }

        /// <summary>
        /// Получить объявления вакансий из json
        /// </summary>
        /// <returns>Коллекция вакансий</returns>
        public List<Vacancy> GetVacanciesFromJson()
        {
            string path = "D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\json";
            return File.Exists($"{path}\\vacancy{j}.json") ? Newtonsoft.Json.JsonConvert.DeserializeObject<List<Vacancy>>(File.ReadAllText($"{path}\\vacancy{j}.json")) : throw new FileNotFoundException("[GetAddsWithJson] Json file for vacancy not found");

        }
    }
}
