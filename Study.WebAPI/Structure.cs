/*

Слоенная архитектура

Хотелки: 
1. Безопасно
2. Легко поддерживали
3. Быстро написать код
4. Быстро работал код 

Interface / UI - через что пользователь обращается к нашей системы (запросы)
   | - control flow             ↑
   ↓ поток управления программы |
Domain / BusinessLogic  BL - логика программы (модели, exceptions, обращение к базе, сторонние сервисы/api)
   |                            ↑ поток управления зависимостями
   ↓                            | - dependency flow
+ Abstractions / Core
DataAccess / DAL / DB - слой для хранения и обработки данных 

classLibrary - проект

newsapi.org - сайт для АПИ
kornylotereshchenko685@your-mai.xyz
9084645f877f464996448527814fb8c2

*/