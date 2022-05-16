using ParserBot.Models;

namespace ParserBot.Abstractions
{
    public interface IDataService
    {
        public List<Car> GetCarsFromJson();
        public List<Vacancy> GetVacanciesFromJson();
    }
}
