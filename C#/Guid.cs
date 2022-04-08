using System;

namespace Study_CSharp_Design.Start_CSharp_
{
    internal class Guid
    {
        private void Method()
        {
            var guid6 = System.Guid.NewGuid();

            System.Guid guid = System.Guid.NewGuid(); // 7277d9bc-f26e-4882-b073-de7ef4eb8436
            System.Guid guid1 = System.Guid.Empty; // 00000000-0000-0000-0000-000000000000
            System.Guid guid2 = System.Guid.Parse("12345678-1234-1234-1234-123456789012"); // 12345678-1234-1234-1234-123456789012
            guid = System.Guid.NewGuid(); // ac168235-7add-4dda-9c2b-b2854cc3e016
            System.Guid guid3 = guid;
            // нужно юзать System, так как выдает ошибку (что типо у проекта есть свой Guid)

            System.Guid.TryParse("12345678-1234-1234-1234-123456789012", out guid) // пытается преобразовать guid-строку в guid
                // которую передаем 2 параметром; если получилось передать в guid - true, если нет - false и передает null в guid
        }
    }
}
