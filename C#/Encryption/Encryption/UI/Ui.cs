using System;
using System.Collections.Generic;
using System.Threading;
using Encryption.HashingAlgorithms;
using Encryption.Interfaces;

namespace Encryption.UI
{
    public class Ui
    {
        #region Fields

        private IHashingAlgorithm _currentHashingAlgorithm = new Base64HashingAlgorithm();
        private Dictionary<int, Action> _operationsDictionary;
        private Dictionary<ConsoleKey, IHashingAlgorithm> _hashingAlgorithmDictionary;

        #endregion

        #region Constructor

        public Ui()
        {
            InitOperationsDictionary();
            InitHashingAlgorithmDictionary();
        }

        #endregion

        #region Methods

        public void Run()
        {
            while (true)
            {
                ShowMenu();
                int chosenOperationNumber = Convert.ToInt32(Console.ReadLine());

                try
                {
                    Action operation = _operationsDictionary[chosenOperationNumber];
                    operation(); // run operation that user has selected
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("Sorry, but choice is incorrect");
                    Console.WriteLine("Please, try again ... ");
                    Thread.Sleep(2000);
                    Console.Clear();
                }
            }
        }

        /// <summary>
        /// Init field dictionary to operations: <see cref="_operationsDictionary"/>
        /// </summary>
        private void InitOperationsDictionary()
        {
            _operationsDictionary = new Dictionary<int, Action>()
            {
                {1, ChooseEncryptionAlgorithm},
                {2, Encode},
                {3, Decode},
                {
                    4, () =>
                    {
                        Console.Clear();
                        Console.WriteLine("\nGoodbye!");
                        Environment.Exit(0);
                    }
                },
            };
        }

        /// <summary>
        /// Init field dictionary to algorithms: <see cref="_hashingAlgorithmDictionary"/>
        /// </summary>
        private void InitHashingAlgorithmDictionary()
        {
            _hashingAlgorithmDictionary = new Dictionary<ConsoleKey, IHashingAlgorithm>()
            {
                {ConsoleKey.F2, new Base85HashingAlgorithm()},
                {ConsoleKey.F3, new Base64HashingAlgorithm()},
            };
        }

        /// <summary>
        /// Output menu
        /// </summary>
        private void ShowMenu()
        {
            Console.Clear();
            Console.WriteLine("\nMenu:");
            Console.WriteLine(
                $"1. Choose encryption algorithm (default: Base64 ; current: {_currentHashingAlgorithm.ToString()})");
            Console.WriteLine("2. Encode message");
            Console.WriteLine("3. Decode message");
            Console.WriteLine("4. Exit");
            Console.Write("Enter your choice: ");
        }

        private void ChooseEncryptionAlgorithm()
        {
            Console.Clear();
            Console.WriteLine("\nPress F2 to choose Base85 hashing algorithm");
            Console.WriteLine("Press F3 to choose Base64 hashing algorithm");
            ConsoleKey key = Console.ReadKey().Key;

            try
            {
                _currentHashingAlgorithm = _hashingAlgorithmDictionary[key];
                Console.Clear();
                Console.WriteLine($"\nYou chose encryption algorithm: {_currentHashingAlgorithm.GetType()}");
                Console.WriteLine("\nPress Enter to Exit");
                Console.ReadKey();
            }
            catch (KeyNotFoundException)
            {
                Console.WriteLine("Change key and try again ...  ");
            }
        }

        private void Encode()
        {
            Console.Clear();
            Console.Write("\nEnter your message, that you want encode: ");
            string msg = Console.ReadLine();
            Console.Clear();

            string encodedMessage = _currentHashingAlgorithm.Encode(msg);
            Console.WriteLine($"\nYour encoded message: {encodedMessage}");
            Console.WriteLine("\nPress Enter to Exit");
            Console.ReadKey();

            Console.Clear();
        }

        private void Decode()
        {
            Console.Clear();
            Console.Write("\nEnter your encoded message, that you want decode: ");
            string encodedMessage = Console.ReadLine();
            Console.Clear();

            string decodedMessage = _currentHashingAlgorithm.Decode(encodedMessage);
            Console.WriteLine($"\nYour decoded message: {decodedMessage}");
            Console.WriteLine("\nPress Enter to Exit");
            Console.ReadKey();

            Console.Clear();
        }

        #endregion

    }
}