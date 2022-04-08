using TemplateCSharpBot;
using System;
using System.Threading;
using System.Threading.Tasks;
using Telegram.Bot;
using Telegram.Bot.Extensions.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.ReplyMarkups;


namespace TemplateCSharpBot
{
    class Program
    {
        private static TelegramBotClient _bot = new TelegramBotClient(Config.Token);

        public static async Task Main(string[] args)
        {
            Console.WriteLine("Bot is start");

            using var cts = new CancellationTokenSource();

            ReceiverOptions receiverOptions = new() { AllowedUpdates = { } };
            _bot.StartReceiving(Handlers.HandleUpdateAsync,
                Handlers.HandleErrorAsync,
                receiverOptions,
                cts.Token);

            Console.ReadLine();

            cts.Cancel();

        }
    }
}