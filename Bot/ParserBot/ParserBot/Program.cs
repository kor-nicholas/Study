global using Deployf.Botf;
using Telegram.Bot.Types.Enums;
using ParserBot.Services;
using ParserBot.Abstractions;

class Program : BotfProgram
{
    readonly ILogger<Program> _logger;
    private IParserService _parser;
    private IDataService _dataService;

    public static void Main(string[] args) => StartBot(args, onConfigure: (svc, cfg) =>
    {
        svc.AddTransient<IParserService, ParserService>();
        svc.AddTransient<IDataService, DataService>();
        svc.AddLogging();
    });

    public Program(ILogger<Program> logger, IParserService parserService, IDataService dataService)
    {
        _logger = logger;
        _parser = parserService;
        _dataService = dataService;

    }

    [Action("Start")]
    [Action("/start", "start the bot")]
    public async Task Start()
    {
        KButton("Так✅");
        KButton("Нi❌");

        await Send("Привiт, я Кабура🖐\n\nМене прислали з космому, щоб допомогти тобi обрати найвигiднiший та найкращий товар " +
            "на нашому сайтi♨️\n\nТи готовий вiдправитись в нашу з тобою подорож до свiту комфорту🛳 затишку🛋 та красивого життя🏂 ?");
    }

    [Action("Так✅")]
    public async Task Yes()
    {
        Button("Автомобiлi🏎");
        Button("Робота💼");
        await Send("👇 Тодi обирай категорiю 👇");

        var testQuery = await AwaitQuery(async () => await Error());

        if (testQuery == "Автомобiлi🏎")
        {
            foreach (var add in _dataService.GetCarsFromJson())
            {
                Button("Перейти до оголошення", add.Link);
                PushL($"<b>{add.Title}</b>\n\n" +
                    $"{add.Description}\n\n" +
                    $"Цiна: {add.Price}\n\n" +
                    $"Мiсто: {add.City}\n\n" +
                    $"Дата публікації: {add.PublicationDate}");
                Photo(add.Photo);
                await Send();

                await Task.Delay(2000);
            }

            await ButtonBack();
        }
        else if (testQuery == "Робота💼")
        {
            foreach (var add in _dataService.GetVacanciesFromJson())
            {
                Button("Перейти до оголошення", add.Link);
                PushL($"<b>{add.Title}</b>\n\n" +
                    $"Сфера дiяльностi: {add.JobSegment}\n\n" +
                    $"Зайнятiсть: {add.JobTime}\n\n" +
                    $"Досвiд: {add.Expirience}\n\n" +
                    $"Зарплата: {add.Salary}\n\n" +
                    $"Мiсто: {add.City}\n\n" +
                    $"Дата публікації: {add.PublicationDate}");
                Photo(add.Photo);
                await Send();

                await Task.Delay(2000);
            }

            await ButtonBack();
        }
        
    }

    [Action("Нi❌")]
    public async Task No()
    {
        await ButtonBack();
    }

    [Action("/update_data", "get request and update data")]
    public async Task CreateRequestAndSaveNewData()
    {
        Button("Автомобiлi🏎");
        Button("Робота💼");
        await Send("Яку категорiю будемо парсити?");

        var parseGoal = await AwaitQuery(async () => await Error());

        if (parseGoal == "Автомобiлi🏎")
        {
            if (await _parser.ParseCarAdds("https://auto.kufar.by/l/cars/mercedes-benz"))
            {
                await Send("Данi збережено");

                await ButtonBack();
            }
            else
            {
                await Send("Сталася помилка при парсингу/збереженнi файлу");
            }
        }
        else if (parseGoal == "Робота💼")
        {
            if (await _parser.ParseVacancyAddsAsync("https://www.kufar.by/l/vakansii"))
            {
                await Send("Данi збережено");

                await ButtonBack();
            }
            else
            {
                await Send("Сталася помилка при парсингу/збереженнi файлу");
            }
        }
    }

    [Action("/help", "all commands")]
    public async Task Help()
    {
        await Send("/start - start the bot\n/request - get request and save data");

        await ButtonBack();
    }

    [Action("🔙Назад")]
    public async Task Back()
    {
        await Start();
    }

    public async Task ButtonBack()
    {
        KButton("🔙Назад");
        await Send("Якщо хочеш вийти в головне меню, натискай на кнопку 👇"); 
    }

    [Action("Error")]
    public async Task Error()
    {
        await Send("Я не понимаю что ты имеешь ввиду😢");
    }

    /*
     * await Send($"Hi! What is your name?");

        var name = await AwaitText(() => Send("Use /start to try again"));
        await Send($"Hi, {name}! Where are you from?");

        var place = await AwaitText();

        Button("Like");
        Button("Don't like");
        await Send($"Hi {name} from {place}! Nice to meet you!\nDo you like this place?");

        var likeStatus = await AwaitQuery();
        if (likeStatus == "Like")
        {
            await Send("I'm glad to heat it!\nSend /start to try it again.");
        }
        else
        {
            await Send("It's bad(\nSend /start to try it again.");
        }

        Start(); // вызовет метод Start
     */

    #region Errors

    [On(Handle.Unknown)]
    public async Task Unknown()
    {
        PushL("unknown");
        await Send();
    }

    [On(Handle.Exception)]
    public async Task Ex(Exception e)
    {
        _logger.LogCritical(e, e.Message);

        if (Context.Update.Type == UpdateType.CallbackQuery)
        {
            await AnswerCallback("Error");
        }
        else if (Context.Update.Type == UpdateType.Message)
        {
            Push("Error");
        }
    }

    [On(Handle.ChainTimeout)]
    public async Task ChainTimeout()
    {
        PushL("timeout");
    }

    #endregion

}
