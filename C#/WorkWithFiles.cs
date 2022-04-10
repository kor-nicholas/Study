using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.IO;
using System.Text;

namespace HelloWorldWebAPI_Cat_
{
    public class WorkWithFiles
    {
        private string _path = "test.txt";

        public void TestReadFile()
        {
            File.ReadAllText("person.json");

// ----------------------------------------------------------------------------------------------------------

            /*
            * Peek() - вовзращает следующий символ, если его нету, то -1
            * Read() - считывает данные в массив
            * ReadLine() - считывает одну строку 
            * ReadToEnd() - считывает весь текст из файла
            */

            // прочитать полностью файл
            using (StreamReader stream = new StreamReader(_path, Encoding.Default))
            {
                Console.WriteLine(stream.ReadToEnd());
            }

            // построчное чтение файла
            using (StreamReader stream1 = new StreamReader(_path, Encoding.Default))
            {
                string line;
                while ((line = stream1.ReadLine()) != null)
                {
                    Console.WriteLine(line);
                }
            }
        }

        public void TestWriteFile()
        {
            File.WriteAllText("person.json", Newtonsoft.Json.JsonConvert.SerializeObject(person));

// ----------------------------------------------------------------------------------------------------------

            /*
             * Flush() - записывает в файл данные из буфера и очищает буфер
             * Write() - записывает простые типы
             * WriteLine() - тоже самое, просто в конце добавляет \n
             */

            // обычная запись в файл (либо же перезапись всего файла)
            using (StreamWriter stream = new StreamWriter(_path, false, Encoding.Default))
            {
                stream.WriteLine("Some text");
            }

            // дозапись в конец файла (указывает на это параметр true в констрокторе)
            using (StreamWriter stream1 = new StreamWriter(_path, true, Encoding.Default))
            {
                stream1.WriteLine("Дозапись");
            }
        }
    }
}
