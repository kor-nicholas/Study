var update = await AwaitNextUpdate();
if(update.Update.Type == UpdateType.Message && Context.Update.Message.Type == MessageType.Photo))
{
    //...
}

update.Update.Message.Photo[0].FileId
