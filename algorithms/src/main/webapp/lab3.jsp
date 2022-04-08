<%-- 
    Document   : lab3
    Created on : 16 апр. 2021 г., 17:07:22
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba3</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="3.png" height="250" width="400"></p>
        <br>
        <h1 class="fig">Результат</h1>
        <p class="fig"><%= request.getAttribute("result") %></p>
        <div>
            <form action="lab3form.jsp" class="fig">
                <input type="submit" value="Назад(ввести ще раз k)">
            </form>
        </div>
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
