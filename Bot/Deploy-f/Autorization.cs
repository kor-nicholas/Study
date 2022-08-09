/*
#FAQ #идентификация и #авторизация

Вот пример с разделением по ролям Deployf.Botf.ScheduleExample

 (https://github.com/deploy-f/botf/tree/master/Examples/Deployf.Botf.ScheduleExample)
 Тут есть роль админа.

Как использовать:

1. Реализовываем сервис для получения ролей из UserId
UserService.cs
 (https://github.com/deploy-f/botf/blob/master/Examples/Deployf.Botf.ScheduleExample/UserService.cs)
 
 2. Регистрируем его 
Program.cs:15
 (https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Examples/Deployf.Botf.ScheduleExample/Program.cs#L15)
 
 3. Проверяем пользователя перед каждым его сообщением(можно делать на /start например, это уже детали реализации)
MainController.cs:45
 (https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Examples/Deployf.Botf.ScheduleExample/MainController.cs#L45)
 
 4. SlotController.Admin.cs:6
 (https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Examples/Deployf.Botf.ScheduleExample/SlotController.Admin.cs#L6)
 Вот тут проверяем например на наличие роли, если есть то выполняем обработку сообщения. 
 Так-же можно вешать атрибут на контроллер, и тогда все экшены будут проверяться на соответствии роли, а с помощью [AllowAnonymous] 
 можно открывать некоторые для всех

5. С помощью Handle.Unauthorized отлавливаем неавторизованых ребят, или у которых нет нужной роли
MainController.cs:75
 (https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Examples/Deployf.Botf.ScheduleExample/MainController.cs#L75)
 
 Нужно иметь ввиду что роли это довольно бесформенная штука. Можете их добавлять кому и как угодно. 
 Единственный интерфес доступа к ним -  IBotUserService.GetUserIdWithRoles
UserService.cs:17 (https://github.com/deploy-f/botf/blob/f308e95e42f8ed04281f6c5930974f32e2de385b/Examples/Deployf.Botf.ScheduleExample/UserService.cs#L17)

WorkHelpBot - пример где юзал
*/

