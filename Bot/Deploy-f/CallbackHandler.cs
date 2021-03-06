using Deployf.Botf;

using WorkHelpBot.Models.Output;

public class TestController : BotController
{
	// Problem - in callback Telegram we can send only string(utf-8, 64 symbols)
	[Action("/test")]
	public async Task Test()
	{
		RowButton("test1", Q(OnSelectTest1, "test1"));
		RowButton("test2", Q(OnSelectTest2, "test2"));
		PushL("Test");
		await Send();
	}

	[Action]
	public async Task OnSelectTest1(string test)
	{
		PushL($"{test}");
		await Send();
	}

	[Action]
	public async Task OnSelectTest2(string test)
	{
		PushL($"{test}");
		await Send();
	}
}
