using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Study_CSharp_Design
{
    internal class IfWhileFor
    {
        private void Method()
        {
            //ОПЕРАТОР IF

            var a = int.Parse(Console.ReadLine());

            if (a == 0) Console.WriteLine("A equals zero");
            // если действие if состоит из одного оператора, его можно писать без фигурных скобок

            if (a == 1)
            {
                //В противном случае нужно обнести нужные операторы скобками
                Console.Write("Let me think... ");
                Console.WriteLine("A equals one!");
            }

            if (a % 2 == 0) Console.WriteLine("A is odd");
            else Console.WriteLine("A is even");

            if (a < 0) Console.WriteLine("A is negative");
            else if (a < 10) Console.WriteLine("A contains one digit");
            else
            {
                var num = a.ToString().Length;
                Console.WriteLine("The number of digits in A is {0}", num);
                if (a > 1000)
                    Console.Write("A is enormous!");
            }

            //ОПЕРАТОР WHILE

            int number = 1;
            while (number < 100)            // пока выполняется условия
            {
                number *= 2;                // делай инструкции в теле цикла
                Console.WriteLine(number);
            }

            int sum = 0;
            while (true)
            {
                var line = Console.ReadLine();
                if (line == "") break;
                if (line.Length > 100) continue; //запросить следующую линию
                sum += int.Parse(line);
            }

            //Для выхода из вложенного цикла приходится использовать
            //конструкцию "double break"

            sum = 0;
            while (true)
            {
                bool stop = false;
                while (true)
                {
                    sum += int.Parse(Console.ReadLine());
                    if (sum > 100)
                    {
                        stop = true;
                        break; //этот break выходит только из внутреннего цикла
                    }
                }
                if (stop)
                {
                    break; //этот break выходит из внешнего цикла по флагу stop
                }
            }

            //  FOR 
            //Суммируем все числа от 1 до 10
            sum = 0;
            for (int i = 1; i <= 10; i++)
                sum += i;

            // Чтобы сделать что-то N раз, мы делаем цикл от 0 до N. 
            // В C# принято в таких случаях делать цикл именно от 0 до i<N, 
            // а не от 1 до i<=N, например.
            for (int i = 0; i < 10; i++)
                Console.WriteLine(i);

            // Выводим все символы строки
            string str = "abc";
            for (int i = 0; i < str.Length; i++)
                Console.Write(str[i]);

            //Декремент
            for (int i = 9; i >= 0; i--)
                Console.Write(i + " ");

            Console.WriteLine();
            //Допускается произвольное изменение переменной
            for (int i = 1; i < 100; i *= 2)
                Console.Write(i + " ");

            Console.WriteLine();
            //Не обязательно инициализировать переменную
            int start = int.Parse(Console.ReadLine());
            for (; start >= 0; start--)
                Console.Write(start + " ");

            Console.WriteLine();
            //И условие тоже может быть произвольным
            for (; start * start < 5 * start; start++)
                Console.Write(start + " ");

            Console.WriteLine();

            //Проверка условия осуществляется КАЖДУЮ итерацию цикла! 
            //Поэтому в данном случае лучше ввести переменную var bound=GetBound() 
            //и сравнивать с ней, а не вызывать цикл каждый раз
            for (int i = 0; i < GetBound(); i++)
                Console.Write(i + " ");
        }

        static int GetBound()
        {
            Console.Write("!");
            return 5;
        }
    }
}
