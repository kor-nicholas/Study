using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Study_CSharp_Design
{
    internal class ReferenceTypeAndTypeValue
    {
        private void Method()
        {
            static void UpdateNumber(int n)
            {
                n++;
            }

            static void UpdateArray1(int[] a)
            {
                a[0]++;
            }

            static void UpdateArray2(int[] a)
            {
                a = new int[3];
                a[0]++;
            }

            static void Main()
            {
                int n;
                n = 1;
                UpdateNumber(n);
                Console.WriteLine(n); // 1 - так как int, double, bool, ... типы-значения, то есть при передаче как аргумент, 
                // создается их локальная копия, которая не меняется

                int[] a = new int[3];
                UpdateArray1(a);
                Console.WriteLine(a[0]); // 1 - так как массивы, List. Dictionary, String, ... ссылочные типы, то есть при передаче
                // как аргумент, передается ссылка на память, где лежат даны объекты

                a = new int[3];
                UpdateArray2(a);
                Console.WriteLine(a[0]); // 0 - так как ссылка перенаправляется на новый объект

                // https://imgur.com/a/KU3EJpT

            }
        }
    }
}
