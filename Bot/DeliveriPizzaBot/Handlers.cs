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
using MyList_;

namespace DeliveryPizza
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

            /*var handler = update.Type;
            
            switch (handler)
            {
                case UpdateType.Message:
                    await BotOnMessageReceived(botClient, update.Message!);
                    break;
                case UpdateType.CallbackQuery:
                    await BotOnCallbackQueryReceived(botClient, update.CallbackQuery);
                    break;
            }*/

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
                if (message.Text == "/start")
                {
                    await CommandStart(botClient, message);
                }
                else if (message.Text == "/getid")
                {
                    await botClient.SendTextMessageAsync(message.Chat.Id, $"Ваш ChatId: {message.Chat.Id}");
                }
                else if (message.Text == "/getgroupid")
                {
                    await botClient.SendTextMessageAsync(message.Chat.Id, $"ID групы: {message.Chat.Id}");
                }
                else if (message.Text == "/add" && message.Chat.Id == Config.AdminId)
                {
                    await CommandAdd(botClient, message);
                }
                else if (message.Text.Split(" ")[0] == "/addName" && message.Chat.Id == Config.AdminId)
                {
                    await CommandAddName(botClient, message, message.Text.Split(" ")[1]);
                }
                else if (message.Text.Split(" ")[0] == "/addDescription" && message.Chat.Id == Config.AdminId)
                {
                    await CommandAddDescription(botClient, message, message.Text.Split(" ")[1]);
                }
                else if (message.Text.Split(" ")[0] == "/addPrise" && message.Chat.Id == Config.AdminId)
                {
                    int prise = Convert.ToInt32(message.Text.Split(" ")[1]);
                    await CommandAddPrise(botClient, message, prise);
                }
                else if (message.Text == "/show" && message.Chat.Id == Config.AdminId)
                {
                    foreach (var product in BaseProduct.products)
                    {
                        await botClient.SendTextMessageAsync(message.Chat.Id,
                            $"Id: {product.GetId()}\nName: {product.GetName()}\nPrise: {product.GetPrise()}");
                    }
                }
                else if (message.Text.Split(" ")[0] == "/delete" && message.Chat.Id == Config.AdminId)
                {
                    int id = Convert.ToInt32(message.Text.Split(" ")[1]);
                    Console.WriteLine($"ID = {id}");
                    BaseProduct.products.RemoveAt(id - 1);
                    await botClient.SendTextMessageAsync(message.Chat.Id, "Пицца была удалена");
                }
                else if (message.Text == "/statistic" && message.Chat.Id == Config.AdminId)
                {
                    await botClient.SendTextMessageAsync(Config.AdminId,
                        $"Вся прибыль комании = {BaseOrder.orders[0].GetProfit()}\n\n" +
                        $"Рекомендации по грамотному распределению прибыли: \n" +
                        $"Зарплаты куръеров-> {(double)BaseOrder.orders[0].GetProfit() / 10}(10%)\n" +
                        $"Зарплата директора-> {(double)BaseOrder.orders[0].GetProfit() * 3 / 10}(30%)\n" +
                        $"Реклама + расходы компании-> {(double)BaseOrder.orders[0].GetProfit() * 3 / 10}(30%)" +
                        $"\nВложения(депозит)-> {(double)BaseOrder.orders[0].GetProfit() * 3 / 10}(30%)\n" +
                        $"(/calculatedeposit чтобы расчитать прибыль после вклада)");
                }
                else if (message.Text == "/calculatedeposit" && message.Chat.Id == Config.AdminId)
                {
                    int profit = BaseOrder.orders[0].GetProfit() * 3 / 10;
                    await botClient.SendTextMessageAsync(Config.AdminId, $"Вся сумма вклада = {profit}\n" +
                                                                         $"\nпри 5% на 1 год доход будет составлять -> {CompoundInterest(profit, 5, 1, 1)}\n" +
                                                                         $"при 5% на 5 лет доход будет составлять -> {CompoundInterest(profit, 5, 1, 5)}\n" +
                                                                         $"при 5% на 10 лет доход будет составлять -> {CompoundInterest(profit, 5, 1, 10)}\n" +
                                                                         $"при 5% на 15 лет доход будет составлять -> {CompoundInterest(profit, 5, 1, 15)}\n" +
                                                                         $"при 5% на 20 лет доход будет составлять -> {CompoundInterest(profit, 5, 1, 20)}\n" +
                                                                         $"\nпри 10% на 1 год доход будет составлять -> {CompoundInterest(profit, 10, 1, 1)}\n" +
                                                                         $"при 10% на 5 лет доход будет составлять -> {CompoundInterest(profit, 10, 1, 5)}\n" +
                                                                         $"при 10% на 10 лет доход будет составлять -> {CompoundInterest(profit, 10, 1, 10)}\n" +
                                                                         $"при 10% на 15 лет доход будет составлять -> {CompoundInterest(profit, 10, 1, 15)}\n" +
                                                                         $"при 10% на 20 лет доход будет составлять -> {CompoundInterest(profit, 10, 1, 20)}\n" +
                                                                         $"\nпри 15% на 1 год доход будет составлять -> {CompoundInterest(profit, 15, 1, 1)}\n" +
                                                                         $"при 15% на 5 лет доход будет составлять -> {CompoundInterest(profit, 15, 1, 5)}\n" +
                                                                         $"при 15% на 10 лет доход будет составлять -> {CompoundInterest(profit, 15, 1, 10)}\n" +
                                                                         $"при 15% на 15 лет доход будет составлять -> {CompoundInterest(profit, 15, 1, 15)}\n" +
                                                                         $"при 15% на 20 лет доход будет составлять -> {CompoundInterest(profit, 15, 1, 20)}\n");

                    await botClient.SendTextMessageAsync(Config.AdminId,
                        $"\nРекомендация: \n{CompoundInterest(profit, 15, 1, 20) * 7 / 10}(70%) реинвестировать в бизнес\n{CompoundInterest(profit, 15, 1, 20) * 3 / 10}(30%) можно оставить себе");
                }
                else if (message.Text.Split(" ")[0] == "/delivery" && message.Chat.Id == Config.AdminId)
                {
                    foreach (var person in BasePerson.persons)
                        await botClient.SendTextMessageAsync(person.GetChatId(), message.Text.Substring(9,message.Text.Length - 9));
                }
                else if (message.Text == "/commands" && message.Chat.Id == Config.AdminId)
                {
                    await botClient.SendTextMessageAsync(Config.AdminId, "/add - начать добавление пиццы");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/addName [название] - добавить название пиццы в меню");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/addDescription [описание] - добавить описание пиццы в меню");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/addPrise [цена] - добавить цену пиццы в меню");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(message.Chat.Id, "/show - просмотреть список пицц");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/delete [ID] - удалить пиццу из меню");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId,
                        "/statistic - для просмотра прибыли компании");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/calculatedeposit - расчитать депозит");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId,
                        "/delivery [сообщение] - для рассылки всем пользователям бота");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId, "/getid - просмотреть свой ChatId");
                    Thread.Sleep(500);
                    await botClient.SendTextMessageAsync(Config.AdminId,
                        "/getgroupid - просмотреть id группы (нужно ввести команду из группы)");
                }
                else if (message.Text == "Меню")
                {
                    await Menu(botClient, message);
                }
                else if (message.Text == "О компании")
                {
                    AboutCompany(botClient, message);
                }
                else if (message.Text == "Назад")
                {
                    await CommandStart(botClient, message);
                }
                else if (message.Text.Contains("Адрес:") || message.Text.Contains("Адрес") || message.Text.Contains("адрес:") || message.Text.Contains("адрес"))
                {
                    foreach (var person in BasePerson.persons)
                        if (person.GetChatId() == message.Chat.Id)
                            person.SetAddress(message.Text);
                    
                    await botClient.SendTextMessageAsync(message.Chat.Id,
                        "Введите номер телефона(с кодом страны вначале, например +38): ");
                }
                else if (message.Text.Contains("+38"))
                {
                    foreach (var person in BasePerson.persons)
                    {
                        if (person.GetChatId() == message.Chat.Id)
                        {
                            person.SetPhone(message.Text);
                            
                            await botClient.SendTextMessageAsync(Config.GroupId,
                                $"Заказ от @{person.GetUserName()}\n\nИмя и фамилия: {message.Chat.FirstName} {message.Chat.LastName}\n" +
                                $"Телефон: {person.GetPhone()}\n\nИнформаци о пицце:\nНазвание - {BaseProduct.GetProductForId(person.GetOrderId()).GetName()}\nЦена - {BaseProduct.GetProductForId(person.GetOrderId()).GetPrise()}\n\n" +
                                $"Адрес доставки: {person.GetAddress()}", replyMarkup: new ReplyKeyboardRemove());
                            
                            BaseOrder.orders.Add(new Order(BaseOrder.orders.Length, BaseProduct.GetProductForId(person.GetOrderId()).GetPrise()));

                            await botClient.SendTextMessageAsync(message.Chat.Id,
                                "Спасибо за ваш заказ, приходите еще 🙂");
                        }
                    }
                }
            }
            else if (message.Type == MessageType.Photo)
            {
                //Console.WriteLine($"PhotoID: {message.Photo[0].FileId}");
                await CommandAddPhotoId(botClient, message, message.Photo[0].FileId);
            }
        }

        #region Start

        private static async Task<Message> CommandStart(ITelegramBotClient botClient, Message message)
        {
            bool add = true;

            for (int i = 0; i < BasePerson.persons.Length; i++)
                if (BasePerson.persons[i].GetChatId() == message.Chat.Id)
                    add = false;

            if (add)
            {
                BasePerson.persons.Add(new Person());
                BasePerson.persons[BasePerson.persons.Length - 1].SetId(BasePerson.persons.Length + 1);
                BasePerson.persons[BasePerson.persons.Length - 1].SetChatId(message.Chat.Id);
                BasePerson.persons[BasePerson.persons.Length - 1].SetUserName(message.Chat.Username);
            }

            return await botClient.SendTextMessageAsync(message.Chat.Id, $"Привет {message.Chat.FirstName} {message.Chat.LastName},\n\nМы рады видеть тебя с нами. Выбирай скорей что хочешь сделать с помощью кнопок 👇", replyMarkup: StartButtons());
        }

        #endregion

        #region Add

        private static async Task CommandAdd(ITelegramBotClient botClient, Message message)
        {
            BaseProduct.products.Add(new Product());
            BaseProduct.products[BaseProduct.products.Length - 1].SetId(BaseProduct.products.Length);
            await botClient.SendTextMessageAsync(Config.AdminId, "Можете начинать добавлять пиццу");
        }

        private static async Task CommandAddName(ITelegramBotClient botClient, Message message, string name)
        {
            BaseProduct.products[BaseProduct.products.Length - 1].SetName(name);
            await botClient.SendTextMessageAsync(message.Chat.Id, "Название установлено");
        }
        
        private static async Task CommandAddDescription(ITelegramBotClient botClient, Message message, string description)
        {
            BaseProduct.products[BaseProduct.products.Length - 1].SetDescription(description);
            await botClient.SendTextMessageAsync(message.Chat.Id, "Описание установлено");
        }
        
        private static async Task CommandAddPrise(ITelegramBotClient botClient, Message message, int prise)
        {
            BaseProduct.products[BaseProduct.products.Length - 1].SetPrise(prise);
            await botClient.SendTextMessageAsync(message.Chat.Id, "Цена установлена");
            Thread.Sleep(500);
            await botClient.SendTextMessageAsync(message.Chat.Id, "Отправьте фото пиццы");
        }
        
        private static async Task CommandAddPhotoId(ITelegramBotClient botClient, Message message, string photoId)
        {
            BaseProduct.products[BaseProduct.products.Length - 1].SetPhotoId(photoId);
            await botClient.SendTextMessageAsync(message.Chat.Id, "Фото установлено");
        }

        #endregion

        #region Menu

        private static async Task Menu(ITelegramBotClient botClient, Message message)
        {
            foreach (var product in BaseProduct.products)
            {
                await botClient.SendPhotoAsync(message.Chat.Id, product.GetPhotoId(),
                    $"Название: {product.GetName()}\n\nОписание: {product.GetDescription()}\n\nЦена: {product.GetPrise()}", replyMarkup: ButtonOrder(product.GetId()));
                Thread.Sleep(200);
            }
            
            Thread.Sleep(300);

            FuncToBack(botClient, message);
        }

        #endregion
        
        #region About company

        private static void AboutCompany(ITelegramBotClient botClient, Message message)
        {
            botClient.SendTextMessageAsync(message.Chat.Id, "Мы, самая огромная компания в мире\n\nНа рынке приготовления пиццы уже много-много лет\n\n...\n\nЕсли остались еще вопросы - напишите нашему менеджеру и он с радостью вам поможет", replyMarkup: ButtonToManager());
            Thread.Sleep(500);
            FuncToBack(botClient, message);
        }
        
        #endregion

        #region Back

        private static void FuncToBack(ITelegramBotClient botClient, Message message)
        {
            botClient.SendTextMessageAsync(message.Chat.Id, "Для выхода в Главное меню - нажмите на кнопку Назад 👇",
                replyMarkup: ButtonToBack());
        }

        #endregion

        #region Keyboards

        #region Inline

        private static InlineKeyboardMarkup ButtonToManager()
        {
            return new InlineKeyboardMarkup(new[]
                {
                    InlineKeyboardButton.WithUrl(
                        text: "Задать вопрос менеджеру",
                        url: $"https://t.me/{Config.ManagerNickname}"
                    )
                }
            );
        }

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
                }) {ResizeKeyboard = true};
        }
        
        private static IReplyMarkup ButtonToBack()
        {
            return new ReplyKeyboardMarkup(
                new[]
                {
                    new KeyboardButton[] {"Назад"}
                }) {ResizeKeyboard = true};
        }

        #endregion

        #endregion

        #region CallBack

        private static async Task BotOnCallbackQueryReceived(ITelegramBotClient botClient, CallbackQuery callback)
        {
            foreach (var person in BasePerson.persons)
            {
                if (person.GetChatId() == callback.Message.Chat.Id)
                {
                    person.SetOrderId(Convert.ToInt32(callback.Data));
                }
            }
            
            await botClient.AnswerCallbackQueryAsync(callback.Id, "При вводе адреса доставки, введите -> Адрес: ... (и ваш адрес вместо точек)",cacheTime: 20);

            await botClient.SendTextMessageAsync(callback.Message.Chat.Id,
                "Введите ваш адрес (с пометкой Адрес: ...)");

        }

        #endregion

        #region More

        private static double CompoundInterest(int p, int r, int n, int t)
        {
            return Math.Round(p * Math.Pow((1 + (double) r / 100 / n), n * t));
        }

        #endregion

    }
}