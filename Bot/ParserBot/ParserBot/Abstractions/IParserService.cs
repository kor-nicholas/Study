using HtmlAgilityPack;
using ParserBot.Models;

namespace ParserBot.Abstractions
{
    public interface IParserService
    {
        /// <summary>
        /// Спарсит все объявления машин со страницы
        /// </summary>
        /// <param name="link"></param>
        /// <returns>Коллекция объявлений</returns>
        Task<bool> ParseCarAdds(string link);

        /// <summary>
        /// Спарсит все объявления вакансий со страницы
        /// </summary>
        /// <param name="link"></param>
        /// <returns>Коллекция объявлений</returns>
        Task<bool> ParseVacancyAddsAsync(string link);
    }
}
