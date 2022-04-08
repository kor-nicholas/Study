using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace HelloWorldWebAPI_Cat_
{
    /*
     * {} - обозначает объекты
     * [] - обозначает массив
     * ключ - всегда string; значение - любой тип (int, другой объект, массив, ...)
     * {
     *      "object": 
            {
                "key": [{"number": 1}, 5]
            }
     * }
     * 
     * Библиотека - Newtonsoft.Json или System.Text.Json
     */

    public class WokrWithJson
    {
        public class Person
        {
            //[Newtonsoft.Json.JsonProperty("name")] - возможность назвать свойство по своему
            public string Name { get; set; }

            //[Newtonsoft.Json.JsonProperty("surName")]
            public string SurName { get; set; }

            //[Newtonsoft.Json.JsonProperty("age")]
            public int Age { get; set; }

            public Person(string name, string surName, int age)
            {
                Name = name;
                SurName = surName;
                Age = age;
            }
        }

        private void SerializeAndDeserialize()
        {
            Person person = new Person("Vasya", "Pupkin", 45);

            string json = Newtonsoft.Json.JsonConvert.SerializeObject(person); // сериализация - преобразование объекта в json-строку

            var personCopy = Newtonsoft.Json.JsonConvert.DeserializeObject<Person>(json); // десериализация - преобразование json-строки в объект
            var personCopy2 = Newtonsoft.Json.JsonConvert.DeserializeObject(json); // десериализация - преобразование json-строки в объект
        }

        private void JsonAndFile()
        {
            //var person = File.Exists("person.json");

            //if (person)
            //    Newtonsoft.Json.JsonConvert.DeserializeObject<Person>(File.ReadAllText("person.json"));
            //else
            //    new Person("Kostya", "Rudenko", 19);

            var person = File.Exists("person.json") ? Newtonsoft.Json.JsonConvert.DeserializeObject<Person>(File.ReadAllText("person.json")) : new Person("Kostya", "Rudenko", 19);

            person.Age++;

            File.WriteAllText("person.json", Newtonsoft.Json.JsonConvert.SerializeObject(person));
        } 
    }
}
