using ParserBot.Abstractions;

namespace ParserBot.Models
{
    /// <summary>
    /// Titile, JobSegment, JobTime, Expirience, Salary, City, Publicationdate, Photo, Link
    /// </summary>
    public class Vacancy
    {
        public int Id { get; set; }
        public string Title { get; set; }
        /// <summary>
        /// Сфера деятельности
        /// </summary>
        public string JobSegment { get; set; }
        /// <summary>
        /// Занятость
        /// </summary>
        public string JobTime { get; set; }
        public string Expirience { get; set; }
        public string Salary { get; set; }
        public string City { get; set; }
        public string PublicationDate { get; set; }
        public string Photo { get; set; }
        public string Link { get; set; }

    }
}
