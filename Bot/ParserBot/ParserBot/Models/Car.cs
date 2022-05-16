using ParserBot.Abstractions;

namespace ParserBot.Models
{
    /// <summary>
    /// Title, Desc, Price, City, PublicationDate, Photo, Link
    /// </summary>
    public class Car
    {
        public int Id { get; set; }
        public string Title { get; set; } //
        public string Description { get; set; } // regdate - год, mileage - пробег, cars_engine - тип двигателя ,cars_capacity - объем,
        // cars_gearbox - коробка, cars_type - кузов, cars_drive - привод, cars_color - цвет, 
        public string Price { get; set; } //
        public string City { get; set; } //
        public string PublicationDate { get; set; } //
        public string Photo { get; set; } 
        public string Link { get; set; } //
    }
}
