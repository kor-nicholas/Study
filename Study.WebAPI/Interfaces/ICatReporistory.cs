using Cats.DAL.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Cats.DAL.Interfaces
{
    public interface ICatReporistory
    {
        public List<Cat> GetAll();
        public Cat GetById(int id);
        public int Post(Cat cat);
        public void Delete(int id);
        public void Put(Cat cat);
    }
}
