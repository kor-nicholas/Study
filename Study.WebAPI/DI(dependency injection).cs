namespace HelloWorldWebApi_Cat_.Study
{
    public class DI_dependency_injection_
    {
        // 1. Фактически создания объекта в другом классе (то есть 1 класс зависит от 2) - dependency (зависимость)

        public class MyClass1
        {
            public MyClass1()
            {
                var myClass2Object = new MyClass2(); // класс 2 зависит от класса 1
            }
        }

        public class MyClass2
        {

        }

        // Injection (внедрять) - контролировать при добавлении зависимости в класс / метод ... (что угодно)



        // 2. Работа с сервисами (более подходит) -> https://www.youtube.com/watch?v=cPJGT8Xms1I (если коротко, то : 
        // мы создаем свой сервис (через интерфейс), потом добавлеям его в классе Startup ко всем внутренним сервисам
        // после чего, можем юзать его в любой точке проекта, для удобства через интерфейс)
}
