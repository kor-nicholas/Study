using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Cats.DAL.Models
{
    public class Cat
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public DateTime DateBirthday { get; set; }
        public string Color { get; set; }
        //public int? GroupId { get; set; } // поле для связи с моделью / таблицей GroupCats
        // !!! чтобы не переписывать весь код, это поле может быть null, но в реальности так делать нельзя !!!

        //public virtual GroupCats GroupCats { get; set; } // тоже для Ef Core, чтобы по Id Cat, он мог достать группу его (для связи)

        // Чтобы указать не обязательное поле, нужно поставить после типа ? (указывает что поле может принимать null)
        // public int? Year { get; set; }

        public Cat(int id, string name, DateTime birthday, string color)
        {
            Id = id;
            Name = name;
            DateBirthday = birthday;
            Color = color;
        }

        public Cat()
        {

        }
    }
}


