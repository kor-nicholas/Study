using System;
using System.Threading;
using System.Threading.Tasks;
using MyList_;
using Telegram.Bot;
using Telegram.Bot.Extensions.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.ReplyMarkups;


namespace DeliveryPizza
{
    class Program
    {
        private static TelegramBotClient _bot = new TelegramBotClient(Config.Token);

        public static async Task Main(string[] args)
        {
            Console.WriteLine("Bot is start");

            BaseProduct.products.Add(new Product(1, "Бiлiбао", "Подвійні мисливські ковбаски, солодкий маринований перець, оливки, соус Песто, соус Барбекю. Додайте сирний чи ковбасний бортик та отримайте соус в подарунок", 211, "AgACAgIAAxkBAAMJYbn2un0nMZRie1-o0AVz03PH8moAAsy5MRuMwNBJlvqBHU8Cl3EBAAMCAANzAAMjBA"));
            BaseProduct.products.Add(new Product(2, "Маргарита", "Томати, Моцарела, соус Песто, соус Класичний. Додайте сирний чи ковбасний бортик та отримайте соус в подарунок", 181, "AgACAgIAAxkBAAMLYbn2zG58rqoEHgMadMGNFKmKYTUAAs25MRuMwNBJgiI0pDKZEycBAAMCAANzAAMjBA"));
            BaseProduct.products.Add(new Product(3, "Годфазер", "Мисливські ковбаски, Корнішони, Бекон, Цибуля, Печериці, соус Барбекю. Додайте сирний чи ковбасний бортик та отримайте соус в подарунок ", 227, "AgACAgIAAxkBAAMNYbn22e2He-qi7G-rGbDsIUCN0F0AAs65MRuMwNBJmJx7Ge0YUVIBAAMCAANzAAMjBA"));
            BaseProduct.products.Add(new Product(4, "Мiт супрiм", "Шинка, філе Куряче, Бекон, Пепероні, Телятина, соус Класичний. Додайте сирний чи ковбасний бортик та отримайте соус в подарунок", 263, "AgACAgIAAxkBAAMPYbn26EQnSm4vQzPE_279nPMnJ1sAAs-5MRuMwNBJGyfkUQrXmw4BAAMCAANzAAMjBA"));

            using var cts = new CancellationTokenSource();

            ReceiverOptions receiverOptions = new() {AllowedUpdates = { }};
            _bot.StartReceiving(Handlers.HandleUpdateAsync,
                Handlers.HandleErrorAsync,
                receiverOptions,
                cts.Token);

            Console.ReadLine();

            cts.Cancel();

        }
    }
}