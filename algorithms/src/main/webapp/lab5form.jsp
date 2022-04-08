<%-- 
    Document   : lab5form
    Created on : 17 мая 2021 г., 21:26:35
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba5</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="5.png" height="250" width="400"></p>
        <br>
        <h1 class="fig">Завдання</h1>
        <p class="fig">Варіант13. 1.Удосконалити алгоритм sortApproach1 та застосувати його для аналізу тексту з минулої лабораторної роботи </p> 
        <p class="fig">2.Згенерувати список  24693 об'єктів з полями типу String та short.</p>    
        <p class="fig">3.Створити та реалізувати алгорими сортування ( binarySearch ) та пошуку  ( linearSearch ) для згенерованого у п.2 списку </p>
        <br>
        <h2 class="fig">Введiть слово</h2>
        <div>
            <form action="./lab5" method="post" class="fig">
                <input type="text" name="word"/>
                <input type="submit" value="вiдправити"/>
            </form>
        </div>
        <p></p>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
