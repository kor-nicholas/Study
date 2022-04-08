<%-- 
    Document   : lab4
    Created on : 19 апр. 2021 г., 10:38:49
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="knu.fit.ist.ta2.lab4.Simple"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba 4</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="4.png" height="250" width="400"></p>
        <h1 class="fig">Текст</h1>
        <%! Simple simple = new Simple();%>
        <br>
        <p class="fig"><%= simple.getText()%></p>
        <br>
        <h1 class="fig">Завдання до тексту</h1>
        <br>
        <p>1) Очищений текст : <%= simple.task1()%></p>
        <br>
        <p>2) Загальна кiлькiсть слiв у текстi : <%= simple.task2()%></p>
        <br>
        <p>3) Кiлькiсть унiкальних слiв у текстi : <%= simple.task3()%></p>
        <br>
        <p>Варiант №13</p>
        <br>
        <p>4) Визначити перші 3 слова, що зустрічаються найчастіше : <%= simple.task4() %></p>
        <br>
        <p>5) Визначити кількість слів що не містять літеру b : <%= simple.task5() %></p>
        <br>
        <p>6) Визначити кількість слів, що мають рівно 3  літери : <%= simple.task6() %></p>
        <br>
        <p>7) Визначити перші 8 трьохлітерні послідовності у словах тексту, що зустрічаються найчастіше : <%= simple.task7() %></p>
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>

