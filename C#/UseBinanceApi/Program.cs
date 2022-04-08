using System;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Binance.Net;
using Binance.Net.Objects;
using Binance.Net.Objects.Spot.SpotData;
using BinanceApi.UI;
using CryptoExchange.Net.Authentication;

namespace BinanceApi
{
    class Program
    {
        static void Main(string[] args)
        {
            Ui ui = new Ui();
            ui.Start();
        }
    }
}