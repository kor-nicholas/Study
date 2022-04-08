<%-- 
    Document   : lab2form
    Created on : 16 апр. 2021 г., 16:58:15
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
        <p class="fig"><img src="2.png" height="250" width="400"></p>
        <br>
        <h3 class="fig">Формула : ln(x)/-9x^2-3x+9</h3>
        <br>
        <h2 class="fig">Введiть x</h2>
        <div>
            <form action="./lab2" method="post" class="fig">
                <input type="text" name="x" placeholder="формат : ###.###"/>
                <input type="submit" value="вiдправити"/>
            </form>
        </div>
        <p></p>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
