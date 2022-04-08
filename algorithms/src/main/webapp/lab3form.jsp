<%-- 
    Document   : lab3form
    Created on : 16 апр. 2021 г., 17:07:47
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Form</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="3.png" height="250" width="400"></p>
        <br>
        <h4 class="fig">Завдання №19</h4>
        <h4 class="fig">Заповнити масив з k дійсних чисел та визначити розмір найдовшої зростаючої послідовності.</h4>
        <br>
        <h2 class="fig">Введiть k</h2>
        <div>
            <form action="./lab3" method="post" class="fig">
                <input type="text" name="k" placeholder="###"/>
                <input type="submit" value="ввести"/>
            </form>
        </div>
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>

