using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Study_CSharp_Design
{
    internal class ArrayForeachListDictionary
    {
        private void Method()
        {
            //Объявление и инициализация массива
            int[] array = new int[3];

            //Доступ к элементам массива
            array[0] = 0;
            array[1] = 1;
            array[2] = 2;

            //Сокращенная инициализация
            array = new[] { 0, 1, 2 };

            //foreach
            foreach (var e in array)
                Console.WriteLine(e); // e - это int

            //Двумерные массивы имеют тип int[,] (соответственно, double[,], string[,] и т.д.)
            int[,] twoDimensionalArray = new int[2, 3];
            twoDimensionalArray[1, 2] = 1;
            twoDimensionalArray = new[,] { { 0, 1 }, { 2, 3 } };
            foreach (var e in twoDimensionalArray)
                Console.WriteLine(e); // e - это int

            //Массив массивов
            int[][] jaggedArray = new int[2][];
            jaggedArray[0] = new int[2];
            jaggedArray[0][0] = 1;
            jaggedArray = new[] { new[] { 0, 1 }, new[] { 0, 1, 2 } };
            foreach (var e in jaggedArray)
                Console.WriteLine(e.Length); // e - это int[]

            //List - может увеличивать количество хранимых элементов
            List<int> list = new List<int>();
            list.Add(1);
            Console.WriteLine(list[0]);
            list = new List<int> { 1, 2, 3 };
            foreach (var e in list)
                Console.WriteLine(e); // e - это int


            //Dictionary - соответствие между произвольными типами данных
            Dictionary<string, int> dictionary = new Dictionary<string, int>();
            dictionary["ab"] = 2;
            dictionary = new Dictionary<string, int>
            {
                { "ab", 2 },
                { "a", 1}
            };
            foreach (var e in dictionary)
                Console.WriteLine("{0} {1}", e.Key, e.Value); // e - это KeyValuePair<string,int>

        }
    }
}

