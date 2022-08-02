global using Deployf.Botf;
using Telegram.Bot.Types.Enums;

class Program : BotfProgram
{
    public static void Main(string[] args) => StartBot(args);

    readonly ILogger<Program> _logger;

    public Program(ILogger<Program> logger)
    {
        _logger = logger;
    }

    [Action("Start")]
    [Action("/start", "start the bot")]
    public async Task Start()
    {
        // https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Deployf.Botf/System/UpdateContextExtensions.cs
        // FromId - user id
        // ChatId - chat id
        // Context.GetUsername()
        // Button("Text", "callBackData")
        // Button("Text", "https://[url]")
        
        await Send($"Hi! What is your name?");

        var name = await AwaitText(() => Send("Use /start to try again"));
        await Send($"Hi, {name}! Where are you from?");

        var place = await AwaitText();

        Button("Like");
        Button("Don't like");
        await Send($"Hi {name} from {place}! Nice to meet you!\nDo you like this place?");

        var likeStatus = await AwaitQuery();
        if(likeStatus == "Like")
        {
            await Send("I'm glad to heat it!\nSend /start to try it again.");
        }
        else
        {
            await Send("It's bad(\nSend /start to try it again.");
        }
    }

    [On(Handle.Unknown)]
    public async Task Unknown()
    {
        PushL("unknown");
        await Send();
    }

    [On(Handle.Exception)]
    public async Task Ex(Exception e)
    {
        _logger.LogCritical(e, "Unhandled exception");

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
}
