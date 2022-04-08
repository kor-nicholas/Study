<%-- 
    Document   : newjsplab2
    Created on : 16 апр. 2021 г., 16:57:41
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba2</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="2.png" height="250" width="400"></p>
        <p></p>
        <h2 class="fig">Результат</h2>
        <p></p>
        <p class="fig"><%= request.getAttribute("result") %></p>
        <p></p>
        <div>
            <form class="fig" action="lab2form.jsp">
                <input type="submit" value="Назад(ввести ще раз x)">
            </form>
        </div>
        <p></p>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
