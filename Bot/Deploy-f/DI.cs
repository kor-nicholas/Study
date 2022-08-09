using Deployf.Botf;

BotfProgram.StartBot(args, onConfigure: (svc, cfg) =>
{
  svc.AddTransient<ITestService, TestService>();
  svc.AddSingleton<IBotUserService, UserService>();
});

// using in WorkHelpBot
