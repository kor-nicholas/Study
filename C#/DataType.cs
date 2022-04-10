using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Study_CSharp_Design
{
    internal class DataType
    {
        private void Method()
        {
            // ЧИСЛОВЫЕ ТИПЫ ДАННЫХ


            int integerNumber;
            // так объявляется переменная: тип (int), затем имя (integerNumber)

            // так осуществляется присваивание
            integerNumber = 10;

            // double - основной тип чисел с плавающей точкой.
            // Можно совмещать объявление и присваивание.
            double doubleNumber = 12.34;


            // float - тип меньшей точности.
            // Суффикс f говорит, что 1.234 - константа типа float, а не double.
            // Используются в библиотеках работы с графикой в Windows.
            float floatNumber = 1.234f;

            //long (большие целые числа). Часто используется для подсчета миллисекунд. 
            // L - суффикс констант такого типа, чтобы не перепутать их с int.
            long longIntegerNumber = 3000000000000L;

            // Есть и другие типы данных: short, decimal, и т.д.
            // В основном, для чисел вы будете пользоваться int и double, иногда - long и float

            //Почти всегда переменные можно объявлять без явного указания типа,
            //с ключевым словом var.
            //var - это не "отсутствие типа". Это означает, что тип будет подобран компилятором.
            var number = 13 + 45.5;
            Console.WriteLine(number);


            // КОНВЕРСИЯ ТИПОВ 

            doubleNumber = integerNumber;
            // Это неявная конверсия типов: присвоение переменной одного типа 
            // значения переменной другого типа без дополнительных усилий. 
            // Она возможна, когда не происходит потери информации

            integerNumber = (int)doubleNumber;
            // Это явная конверсия типов. В случае, когда конверсия ведет к потере информации
            // (в данном случае - дробной части), необходимо явно обозначать свои намерения
            // по конверсии.


            integerNumber = (int)Math.Round(34.67);
            // Округление лучше всего делать не конверсией, а функцией Round. 
            // Кстати, Math - "математическая библиотека" C# - имеет множество других
            // полезных методов. 


            long longInteger = 4000000000;
            integerNumber = (int)longInteger;
            // При такой конверсии происходит ошибка переполнения, которая, однако, остается
            // незамеченной для компилятора и среды разработки


            // Таким образом можно отловить эти ошибки явно
            checked
            {
                integerNumber = (int)longInteger;
            }

            //СТРОКИ

            //Строки - это последовательности символов
            string myString = "Hello, world!";

            // + — это операция "приписывания" одной строки к другой:
            string s = "Hello" + " " + "world";

            // Можно обращаться к отдельным символам
            char c = myString[1]; //'e' — нумерация символов с нуля.
            char myChar = 'e'; // одинарные кавычки используются для символов. Двойные — для строк.

            //У строк есть собственные методы и свойства,
            //которые позволяют узнать информацию о строке 
            Console.WriteLine(myString.Length);

            myString = myString.Substring(0, 5);
            Console.WriteLine(myString);

            //строка может содержать символы Unicode
            string strangeSymbols = "© 2014 Σγμβόλσ";

            //Есть спецсимволы, которые нужно экранировать
            strangeSymbols = "\\\"\'"; //строка \"'
            strangeSymbols = @"\""'"; // та же строка \"'

            //Тип string может иметь особое значение - null.
            //Это не пустая строка, а отсутствие всякой строки.
            myString = null;

            //Интересно, что тип int такого значения иметь не может.
            //int a=null;

            number = int.Parse("42"); //Из строки в число
            string numString = 42.ToString(); // Из числа в строку
            double number2 = double.Parse("34.42"); // Зависит от настроек операционной системы

            //Следующий вызов не зависит от настроек и всегда ожидает точку в качестве разделителя:
            number2 = double.Parse("34.42", CultureInfo.InvariantCulture);
            
            // DateTime
            
            DateTime date1 = new DateTime(2015, 7, 20, 18, 30, 25); // год - месяц - день - час - минута - секунда
            Console.WriteLine(date1); // 20.07.2015 18:30:25
            Console.WriteLine(DateTime.Now); // текущая дата + время
            
        }
    }
}
