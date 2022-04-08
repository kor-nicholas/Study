<%-- 
    Document   : lab5
    Created on : 17 мая 2021 г., 21:26:56
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="knu.fit.ist.ta2.lab5.App"%>
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
        <%! App app = new App();%>
        <p class="fig"><% app.setWord(request.getAttribute("result").toString());%></p>
        <br>
        <p class="fig"><b>Текст : </b></p>
        <p class="fig"><%= app.getText()%></p>
        <h1 class="fig">Результат виконання завдання</h1>
        <p class="fig"><b>1.</b> Список iндексiв слова: <%= app.task1()%></p>
        <p class="fig"><b>2.</b> Список об'эектiв: <%= app.task2()%></p>
        <p class="fig"><b>3.</b> Лiнiйний та бiнарний пошук: <%= app.task3()%></p>
        <br>
        <div>
            <form class="fig" action="lab5form.jsp">
                <input type="submit" value="Назад(ввести ще раз слово)">
            </form>
        </div>
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>

