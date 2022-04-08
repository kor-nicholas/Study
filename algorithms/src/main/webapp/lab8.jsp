<%-- 
    Document   : lab8
    Created on : 24 мая 2021 г., 17:32:58
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="knu.fit.ist.ta2.lab8.App"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba8</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="8.png" height="250" width="400"></p>
        <br>
        <%! App app = new App();%>
        
        <h3><b>Задача</b>: Знайти iндекс числа 50 в массивi за допомогою алгоритму лiнiйного та бiнарного пошуку</h3>
        <p><b>Вхiднi данi</b>: </p>
        <p>Кiлькiсть елементiв: 45000</p>
        <%app.init();%>
        <br>
        <p><b>Назва алгоритму</b>: LinearSearch</p>
        <p><b>Час</b>: <%=app.timeLinearSearch()%>ms</p>
        <p><b>Складнiсть(Big-O)</b>: O(N)</p>
        <br>
        <p><b>Назва алгоритму</b>: BinarySearch</p>
        <p><b>Час</b>: <%=app.timeBinarySearch()%>ms</p>
        <p><b>Складнiсть(Big-O)</b>: O(log(N)</p>
        
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
