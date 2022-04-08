using System;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Channels;
using System.Threading.Tasks;
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;

namespace TemplateCSharpBot
{
    public class Handlers
    {
        #region Error

        public static Task HandleErrorAsync(ITelegramBotClient botClient, Exception exception,
            CancellationToken cancellationToken)
        {
            var ErrorMessage = exception switch
            {
                ApiRequestException apiRequestException =>
                    $"Telegram API Error:\n[{apiRequestException.ErrorCode}]\n{apiRequestException.Message}",
                _ => exception.ToString()
            };

            Console.WriteLine(ErrorMessage);
            return Task.CompletedTask;
        }

        #endregion

        public static async Task HandleUpdateAsync(ITelegramBotClient botClient, Update update,
            CancellationToken cancellationToken)
        {
            var handler = update.Type switch
            {
                UpdateType.Message => BotOnMessageReceived(botClient, update.Message!),
                UpdateType.CallbackQuery => BotOnCallbackQueryReceived(botClient, update.CallbackQuery!),
            };

            try
            {
                await handler;
            }
            catch (Exception exception)
            {
                await HandleErrorAsync(botClient, exception, cancellationToken);
            }
        }

        private static async Task BotOnMessageReceived(ITelegramBotClient botClient, Message message)
        {
            if (message.Type == MessageType.Text)
            {
                await botClient.SendTextMessageAsync(message.Chat.Id, "Знакомлюсь :)");
            }
            else if (message.Type == MessageType.Photo)
            {
                //Console.WriteLine($"PhotoID: {message.Photo[0].FileId}");
            }
        }

        #region Keyboards

        #region Inline

        //private static InlineKeyboardMarkup ButtonToManager()
        //{
        //    return new InlineKeyboardMarkup(new[]
        //        {
        //            InlineKeyboardButton.WithUrl(
        //                text: "Задать вопрос менеджеру",
        //                url: $"https://t.me/{Config.ManagerNickname}"
        //            )
        //        }
        //    );
        //}

        private static IReplyMarkup ButtonOrder(int id)
        {
            return new InlineKeyboardMarkup(new[]
                {
                    InlineKeyboardButton.WithCallbackData(
                        text: "Заказать",
                        callbackData: $"{id}"
                    )
                }
            );
        }

        #endregion

        #region Reply

        private static IReplyMarkup StartButtons()
        {
            return new ReplyKeyboardMarkup(
                new[]
                {
                    new KeyboardButton[] {"Меню", "О компании"}
                })
            { ResizeKeyboard = true };
        }

        #endregion

        #endregion

        #region CallBack

        private static async Task BotOnCallbackQueryReceived(ITelegramBotClient botClient, CallbackQuery callback)
        {
            await botClient.AnswerCallbackQueryAsync(callback.Id, "При вводе адреса доставки, введите -> Адрес: ... (и ваш адрес вместо точек)", cacheTime: 20);

            await botClient.SendTextMessageAsync(callback.Message.Chat.Id,
                "Введите ваш адрес (с пометкой Адрес: ...)");

        }

        #endregion

        #region More

        private static double CompoundInterest(int p, int r, int n, int t)
        {
            return Math.Round(p * Math.Pow((1 + (double)r / 100 / n), n * t));
        }

        #endregion

    }
}