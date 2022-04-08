using System;
using System.Collections.Generic;

namespace Advertisement_application_2
{
    public class Menu
    {
        private List<string> list = new List<string>();
        
        public void start()
        {
            int choose;
            
            do
            {
                Console.Write("\nMenu: \n1. All list\n2. Add\n3. Delete\n4. Clear\n5. Exit\nEnter your choose: ");
                choose = Convert.ToInt32(Console.ReadLine());

                if (choose <= 0 || choose > 5)
                {
                    Console.WriteLine("Sorry, but choose correct variante!");
                }

                switch (choose)
                {
                    case 1:
                        if (list.Count != 0)
                        {
                            Console.WriteLine("\nAll list: ");
                            foreach (string i in list)
                            {
                                Console.WriteLine(i);
                            }
                        }
                        else
                        {
                            Console.WriteLine("\nList is empty");
                        }
                        break;
                    case 2:
                        Console.Write("Enter name ad: ");
                        list.Add(Convert.ToString(Console.ReadLine()));
                        Console.WriteLine("\nName is Add");
                        break;
                    case 3:
                        Console.Write("Enter name, which you want delete: ");
                        int index = list.IndexOf(Convert.ToString(Console.ReadLine()));
                        if (index != -1)
                        {
                            list.RemoveAt(index);
                            Console.WriteLine("\nName is Delete");
                        }
                        else
                        {
                            Console.WriteLine("\nThis name isn't in Ads List!");
                        }
                        break;
                    case 4:
                        list.Clear();
                        Console.WriteLine("\nList is Clear");
                        break;
                    case 5:
                        Console.WriteLine("\nGoodbye!");
                        break;
                }
            } while (choose != 5);
        }
    }
}