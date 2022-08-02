using Deployf.Botf;

class Program : BotfProgram
{
    public static void Main(string[] args) => StartBot(args);

    [Action("/start", "описание старта")]
    public void Start()
    {
        Push("тест Push");
        PushL("тест PushL");
        PushLL("тест PushLL");
    }

    [Action("/nameof", "тест nameof")]
    public void TestNameof()
    {
        Push($"Send '{nameof(Hello)}' to me, please!");
    }

    [Action(nameof(Hello))]
    public void Hello()
    {
        Push("Hey! Thank you! That's it!");
    }

    [On(Handle.Unknown)]
    public async void Unknown()
    {
        PushL("You know.. it's very hard to recognize your command!");
        PushL("Please, write a correct text. Or use /start command");
    }
}
