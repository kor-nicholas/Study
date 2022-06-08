object.GetType().GetMethods()
object.GetType().GetMethod("CurrentMethod")

object.GetType().GetProperties()
object.GetType().GetProperty("CurrentPropertie")

foreach (var item in object.GetType().GetMethods())
{
	Console.WriteLine(item.Name) // name of methods
}