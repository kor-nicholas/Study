using System;
using System.Collections.Generic;
using System.Threading;


namespace SlotMachine
{
    public class App
    {
        #region Fields

        private int balance = 100, bet = 10, win;
        private int[,] arr = new int[3, 3];
        private Dictionary<int, Action> _menuOperationsDictionary;
        private Dictionary<ConsoleKey, Action> _playOperationsDictionary;

        #endregion

        #region Constructor
        
        /// <summary>
        /// Constructor without parameters to init dictionary and array
        /// </summary>
        public App()
        {
            InitMenuOperationsDictionary();
            InitPlayOperationsDictionary();
            ArrayInit(false);
        }

        #endregion

        #region Methods
        
        /// <summary>
        /// Main method to start app
        /// </summary>
        public void Start()
        {
            while (true)
            {
                ShowMenu();
                int choice = Convert.ToInt32(Console.ReadLine());

                try
                {
                    Action menuAction = _menuOperationsDictionary[choice];
                    menuAction();
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("Sorry, but your choice is incorrect. Try again ... ");
                    Thread.Sleep(2000);
                    Console.Clear();
                }
            }
        }
        
        #region Methods(Init)
        
        /// <summary>
        /// Init array <see cref="arr"/> (win or no in arguments)
        /// </summary>
        /// <param name="win"></param>
        private void ArrayInit(bool win)
        {
            Random random = new Random();

            if (!win)
            {
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        arr[i, j] = random.Next(0, 9);
                    }
                }
            }
            else
            {
                for (int i = 0; i < 3; i++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        arr[i, j] = 7;
                    }
                }
            }
        }
        
        /// <summary>
        /// Init dictionary <see cref="_menuOperationsDictionary"/>
        /// </summary>
        private void InitMenuOperationsDictionary()
        {
            _menuOperationsDictionary = new Dictionary<int, Action>()
            {
                {1, MenuOperationPlay}, // play
                {2, MenuOperationShowBalance}, // balance
                {3, MenuOperationShowInfo}, // info
                {
                    4, () =>
                    {
                        Console.Clear();
                        Console.WriteLine("\nGoodbye!");
                        Environment.Exit(0);
                    }
                }, // exit
            };
        }
        
        /// <summary>
        /// Init dictionary <see cref="_playOperationsDictionary"/>
        /// </summary>
        private void InitPlayOperationsDictionary()
        {
            _playOperationsDictionary = new Dictionary<ConsoleKey, Action>()
            {
                {ConsoleKey.F2, AddBet}, // add bet (+)
                {ConsoleKey.F3, SubtractBet}, // subtract bet (-)
                {ConsoleKey.Enter, CheckBetBeforeSpin}, // spin
                {ConsoleKey.Tab, () => bet = balance}, // max bet
                {ConsoleKey.Backspace, () => {}}, // exit to menu
            };
        }

        #endregion
        
        #region Methods(Menu)
        
        private void ShowMenu()
        {
            Console.Clear();
            Console.WriteLine("\nMenu:");
            Console.WriteLine("1. Play");
            Console.WriteLine("2. Balance");
            Console.WriteLine("3. Info");
            Console.WriteLine("4. Exit");
            Console.Write("Enter your choice: ");
        }
        
        private void ShowFirstPictureBeforeMenuOperationPlay()
        {
            Console.WriteLine("[Le Slot]");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine("|\t|  0");
            Console.WriteLine("|\t| /");
            Console.WriteLine("|\t|-");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine($"Bet: {bet}");
            Console.WriteLine($"All summ win: {win}");
            Console.WriteLine($"Balance: {balance}\n");
            Console.WriteLine("Press F2 to add Bet (+10)");
            Console.WriteLine("Press F3 to subtract Bet (-10)");
            Console.WriteLine("Press Tab to max Bet");
            Console.WriteLine("Press Enter to Spin");
            Console.WriteLine("Press BackSpace to exit to Menu");
            
            /*Console.WriteLine("Bet: {0}\nWin: {1}\nBalance: {2}\n\nPress F2 to Bet+10\nPress F3 to Bet-10\n" +
                              "Press Tab to max Bet\nPress Enter to Spin\nPress BackSpace to Menu", bet, win, balance);*/
        }
        
        /// <summary>
        /// Menu before start play game
        /// </summary>
        private void MenuOperationPlay()
        {
            ConsoleKey key;
            Console.Clear();

            do
            {
                ShowFirstPictureBeforeMenuOperationPlay();
                key = Console.ReadKey().Key;
                Console.Clear();

                try
                {
                    Action playAction = _playOperationsDictionary[key];
                    playAction();
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("Please, change key and try again ... ");
                    Thread.Sleep(2000);
                }
            } while (key != ConsoleKey.Backspace);
        }
        
        private void MenuOperationShowBalance()
        {
            Console.Clear();
            Console.WriteLine($"\nYour Balance: {balance}");
            Console.Write("\nPress Enter to exit ");
            Console.ReadKey();
        }

        private void MenuOperationShowInfo()
        {
            Console.Clear();
            Console.WriteLine("\nInfo:");
            Console.WriteLine(
                "It is a bad game. We don't force you to play in this game, because this game like casino");
            Console.Write("\nPress Enter to exit ");
            Console.ReadKey();
        }

        #endregion
        
        #region Methods(Play)

        private void AddBet()
        {
            if (bet >= balance)
            {
                Console.WriteLine("\nOn your balance not enough money\n");
                Thread.Sleep(2000);
                Console.Clear();
                bet = balance;
            }
            else
            {
                bet += 10;
            }
        }

        private void SubtractBet()
        {
            if (bet <= 10)
            {
                Console.WriteLine("\nMinimum Bet is 10. Please change Bet\n");
                Thread.Sleep(2000);
                Console.Clear();
                bet = 10;
            }
            else
            {
                bet -= 10;
            }
        }

        private void CheckBetBeforeSpin()
        {
            if (bet >= 10 && balance >= 10)
            {
                Spin();
            }
            else
            {
                Console.WriteLine("\nBet or Balance must be minimum at 10\n");
                Thread.Sleep(2000);
                Console.Clear();
            }
        }
        
        /// <summary>
        /// Start play game
        /// </summary>
        private void Spin()
        {
            Console.WriteLine("[Le Slot]");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine("| ? ? ? |");
            Console.WriteLine("|\t|");
            Console.WriteLine("|\t|--0");
            Console.WriteLine(new String('-', 9));
            Thread.Sleep(1000);

            Console.Clear();

            Console.WriteLine("[Le Slot]");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine("|\t|");
            Console.WriteLine("| ? ? ? |");
            Console.WriteLine("|\t|--0");
            Console.WriteLine(new String('-', 9));
            Thread.Sleep(1000);

            Console.Clear();

            Console.WriteLine("[Le Slot]");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine("|\t|");
            Console.WriteLine("|\t|");
            Console.WriteLine("| ? ? ? |--0");
            Console.WriteLine(new String('-', 9));
            Thread.Sleep(1000);

            Console.Clear();

            Console.WriteLine("[Le Slot]");
            Console.WriteLine(new String('-', 9));
            Console.WriteLine($"| {arr[0, 0]} {arr[0, 1]} {arr[0, 2]} |");
            Console.WriteLine($"| {arr[1, 0]} {arr[1, 1]} {arr[1, 2]} |");
            Console.WriteLine($"| {arr[2, 0]} {arr[2, 1]} {arr[2, 2]} |--0");
            Console.WriteLine(new String('-', 9));

            if (arr[1, 0] == arr[1, 1] && arr[1, 1] == arr[1, 2])
            {
                Win();
            }
            else
            {
                Lose();
            }

            Thread.Sleep(2000);

            Console.Clear();
        }

        private void Win()
        {
            balance += bet;
            win += bet;
            Console.WriteLine("You're WINNER!");
            Console.WriteLine($"You win: {bet}");
            bet = 10;
        }

        private void Lose()
        {
            balance -= bet;
            win -= bet;
            Console.WriteLine("You're a Lose!");
            Console.WriteLine($"You lose: {bet}");
            bet = 10;
        }

        #endregion

        #endregion
    }
}