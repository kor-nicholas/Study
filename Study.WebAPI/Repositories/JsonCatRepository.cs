using Cats.DAL.Interfaces;
using Cats.DAL.Models;
using System.Text;

namespace Cats.DAL.Repositories
{
    public class JsonCatRepository : ICatReporistory
    {
        private string Path { get; } = "cats.json";
        private List<Cat> _cats;

        public JsonCatRepository()
        {
            InitializeList();
        }

        private void InitializeList()
        {
            string textJson = File.ReadAllText(Path, Encoding.Default);

            _cats = Newtonsoft.Json.JsonConvert.DeserializeObject<List<Cat>>(textJson);
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

            string textJson = Newtonsoft.Json.JsonConvert.SerializeObject(_cats);

            File.WriteAllText(Path, textJson, Encoding.Default);

            return newId;
        }

        public void Delete(int id)
        {
            Cat cat = _cats.Single(catInLinq => catInLinq.Id == id);

            _cats.Remove(cat);

            string textJson = Newtonsoft.Json.JsonConvert.SerializeObject(_cats);
            File.WriteAllText(Path, textJson, Encoding.Default);
        }

        public void Put(Cat cat)
        {
            Cat localCat = _cats.Single(localCat => localCat.Id == cat.Id);

            localCat.Name = cat.Name;
            localCat.DateBirthday = cat.DateBirthday;
            localCat.Color = cat.Color;

            string textJson = Newtonsoft.Json.JsonConvert.SerializeObject(_cats);
            File.WriteAllText(Path, textJson, Encoding.Default);
        }
    }
}
