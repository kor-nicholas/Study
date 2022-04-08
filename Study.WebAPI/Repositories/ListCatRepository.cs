using Cats.DAL.Interfaces;
using Cats.DAL.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Cats.DAL.Repositories
{
    public class ListCatRepository : ICatReporistory
    {
        private List<Cat> _cats;

        private void InitializeList()
        {
            _cats = new List<Cat>();

            _cats.Add(new Cat(1, "Vasya", new DateTime(1991, 01, 01), "green"));
            _cats.Add(new Cat(2, "Kostya", new DateTime(1992, 02, 02), "blue"));
        }

        public ListCatRepository()
        {
            InitializeList();
        }

        public List<Cat> GetAll()
        {
            return _cats;
        }

        public Cat GetById(int id)
        {
            return _cats.Single(cat => cat.Id == id);
        }

        public int Post(Cat cat)
        {
            int newId = _cats[_cats.Count - 1].Id + 1;

            _cats.Add(new Cat(newId, cat.Name, cat.DateBirthday, cat.Color));

            return newId;
        }

        public void Delete(int id)
        {
            Cat cat = _cats.Single(catInLinq => catInLinq.Id == id);

            _cats.Remove(cat);
        }

        public void Put(Cat cat)
        {
            Cat localCat = _cats.Single(localCat => localCat.Id == cat.Id);

            localCat.Name = cat.Name;
            localCat.DateBirthday = cat.DateBirthday;
            localCat.Color = cat.Color;
        }
    }
}
