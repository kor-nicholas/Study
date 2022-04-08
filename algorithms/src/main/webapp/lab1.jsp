<%-- 
    Document   : lab1
    Created on : 16 апр. 2021 г., 16:36:02
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="knu.fit.ist.ta2.lab1.TestClass"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba1</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="1.png" height="250" width="400"></p>
        <p></p>
        
        <%! TestClass clas = new TestClass();
        TestClass clas2 = new TestClass(6); %>
        
        <p class="fig"><%= "Count (TestClass) : " + TestClass.count + '\n'%></p>
        <p class="fig"><%= "Count (clas) : " + clas.count + '\n'%></p>
        <p class="fig"><%= "Count (clas2) : " + clas2.count + '\n'%></p>
        
        <% clas.SetExample(9);
        int sum = clas.GetExample() + clas2.GetExample();%>
        
        <p class="fig"><%= "Get_1 : " + clas.GetExample() + '\n'%></p>
        
        <p class="fig"><%= clas.toString() + '\n'%></p>
        
        <p class="fig"><%= "Get_2 : " + clas2.GetExample() + '\n'%></p>
        
        <p class="fig"><%= clas2.toString() + '\n'%></p>
        
        <p class="fig"><%= "sum = " + sum + '\n'%></p>
        
        <p></p>
        <p></p>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
