using System;
using System.Collections.Generic;
using System.Threading;
using Binance.Net;
using Binance.Net.Objects;
using Binance.Net.Objects.Spot.SpotData;
using CryptoExchange.Net.Authentication;
using CryptoExchange.Net.Objects;

namespace BinanceApi.UI
{
    public class Ui
    {
        #region Fields

        private string _apiKey;
        private string _secretKey;
        private BinanceClient _client;
        private WebCallResult<BinanceAccountInfo> _accountInfo;
        private IEnumerable<BinanceBalance> _balances;
        private Dictionary<int, Action> _menuDictionary;

        #endregion

        #region Constructor

        public Ui()
        {
            InitBinanceClient();
            InitAccountInfo();
            InitBalances();
            InitMenuDictionary();
        }

        #endregion

        #region Methods

        #region Init

        private void InitBinanceClient()
        {
            try
            {
                if (_apiKey.Length < 64 || _secretKey.Length <= 64)
                {
                    throw new Exception("Length apiKey and secretKey must be equal 64");
                }

                BinanceClient.SetDefaultOptions(new BinanceClientOptions()
                {
                    ApiCredentials = new ApiCredentials(_apiKey, _secretKey),
                    //LogLevel = LogLevel.Debug,
                    //LogWriters = new List<ILogger> { new ConsoleLogger() }
                });
                BinanceSocketClient.SetDefaultOptions(new BinanceSocketClientOptions()
                {
                    ApiCredentials = new ApiCredentials(_apiKey, _secretKey),
                    //LogLevel = LogLevel.Debug,
                    //LogWriters = new List<ILogger> { new ConsoleLogger() }
                });

                _client = new BinanceClient();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private void InitAccountInfo()
        {
            try
            {
                _accountInfo = _client.General.GetAccountInfoAsync().Result;
                if (!_accountInfo.Success)
                {
                    throw new Exception("Object accountInfo can't create");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private void InitBalances()
        {
            try
            {
                if (_accountInfo.Success)
                {
                    _balances = _accountInfo.Data.Balances;
                    if (_balances == null)
                    {
                        throw new Exception("Can't create object balances");
                    }
                }
                else
                {
                    throw new Exception("Object accountInfo can't create");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private void InitMenuDictionary()
        {
            try
            {
                _menuDictionary = new Dictionary<int, Action>()
                {
                    {1, InputAndSetApiKeyAndSecretKey},
                    {2, ShowPricePair},
                    {3, ShowAllBalancesAccount},
                    {4, ShowBalanceForCoin},
                    {5, () => Environment.Exit(0)},
                };
                if (_menuDictionary == null)
                {
                    throw new Exception("Can't init menuDictionary");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        #endregion

        #region ShowBalance

        private void ShowAllBalancesAccount()
        {
            //Console.Clear();

            Console.WriteLine("All coins in your balance\n");

            try
            {
                foreach (var balance in _balances)
                {
                    Console.WriteLine($"Quantity {balance.Asset}: {balance.Total}");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        private void ShowBalanceForCoin()
        {
            //Console.Clear();

            Console.Write("Enter coin, that you want watch prise: ");
            string coin = Console.ReadLine();

            try
            {
                if (_balances == null)
                {
                    throw new NullReferenceException();
                }

                foreach (var balance in _balances)
                {
                    if (balance.Asset == coin)
                    {
                        Console.WriteLine($"Quantity {balance.Asset}: {balance.Total}");
                    }
                    else
                    {
                        throw new Exception("Any balance haven't this Asset");
                    }
                }
            }
            catch (NullReferenceException)
            {
                Console.WriteLine("Balances is null");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        #endregion

        #region ShowPrice

        private async void ShowPricePair()
        {
            //Console.Clear();
            Console.Write("\nEnter first cryptocurrency in pair: ");
            string firstCrypto = Console.ReadLine();
            Console.Write("Enter second cryptocurrency in pair: ");
            string secondCrypto = Console.ReadLine();
            
            try
            {
                var price = await _client.Spot.Market.GetPriceAsync($"{firstCrypto}{secondCrypto}");
                Console.WriteLine($"Price {firstCrypto}/{secondCrypto}: {price.Data.Price}");
                if (!price.Success)
                {
                    throw new Exception("Can't create object price");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        #endregion

        #region Other

        private void InputAndSetApiKeyAndSecretKey()
        {
            //Console.Clear();

            Console.Write("\nEnter apiKey: ");
            _apiKey = Console.ReadLine();
            if (_apiKey.Length < 64)
            {
                throw new Exception("Length apiKey must be equal 64");
            }

            Console.Write("\nEnter secretKey: ");
            _secretKey = Console.ReadLine();
            if (_secretKey.Length < 64)
            {
                throw new Exception("Length secretKey must be equal 64");
            }
            
            InitBinanceClient();
        }

        private void ShowMenu()
        {
            //Console.Clear();

            Console.WriteLine("\nMenu: ");
            Console.WriteLine("1. Set ApiKey and SecretKey");
            Console.WriteLine("2. Show price crypto pair");
            Console.WriteLine("3. Show all cryptocurrency balances");
            Console.WriteLine("4. Show the balance of a specific cryptocurrency");
            Console.WriteLine("5. Exit");
            Console.Write("Enter your choice: ");
        }

        public void Start()
        {
            while (true)
            {
                ShowMenu();
                int choice = Convert.ToInt32(Console.ReadLine());

                try
                {
                    Action operation = _menuDictionary[choice];
                    operation();
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("Choice is incorrect");
                    Thread.Sleep(2000);
                    Console.Clear();
                }
            }
        }

        #endregion

        #endregion
    }
}