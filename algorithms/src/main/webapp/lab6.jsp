<%-- 
    Document   : lab6
    Created on : 21 мая 2021 г., 10:34:50
    Author     : ProBook
--%>

<%@page contentType="text/html" pageEncoding="UTF-8" import="knu.fit.ist.ta2.lab6.App"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Laba6</title>
        <style>
        	.fig {
        		text-align: center;
        	}
        </style>
    </head>
    <body>
        <p class="fig"><img src="6.png" height="250" width="400"></p>
        <br>
        <%! App app = new App();int[] arrayInt = app.task1();int[] arrayInt2 = app.task2();%>
        <p><b>Варіант13</b></p>
        <p><b>1</b>.Створити симетричне бінарне дерево пошуку з елементів:</p>
        <p>{4, 11, 2, 9, 6, 16, 8, 3}.</p>
        <p>(написати окремий метод для визначення порядку додавання елементів до дерева)</p>
        <p><b>2</b>.Вивести на екран початкове дерево та результати виконання операцій над ним, що розглядалися на занятті</p>
        <br>
        
        <p class="fig"><b>Початкове бiнарне дерево</b></p>
        
        <table align="center">
            <tr>
                <td></td>
                <td>
                    <samp><%=arrayInt[0]%></samp>
                    <br>
                </td>
                <td></td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: 30px;">/</samp>
                    <br>
                    <samp style="margin-right: 50px;"><%=arrayInt[1]%></samp>
                    <br>
                </td>
                <td></td>
                <td>
                    <samp style="margin-left: 30px;">\</samp>
                    <br>
                    <samp style="margin-left: 50px;"><%=arrayInt[2]%></samp>
                    <br>
                </td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: 20px;">\</samp>
                    <br>
                    <samp style="margin-left: 40px;"><%=arrayInt[3]%></samp>
                    <br><samp style="margin-left: 45px;">\</samp>
                </td>
                <td></td>
                <td>
                    <samp style="margin-left: 22px;">/</samp>
                    <br>
                    <samp style="margin-left: 10px;"><%=arrayInt[4]%></samp>
                    <br><samp>/</samp>
                </td>
                <td>
                    <samp style="margin-left: 15px;">\</samp>
                    <br>
                    <samp style="margin-left: 30px;"><%=arrayInt[5]%></samp>
                    <br><br>
                </td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: 50px;"><%=arrayInt[6]%></samp>
                </td>
                <td></td>
                <td>
                    <samp style="margin-left: -5px;"><%=arrayInt[7]%></samp>
                </td>
            </tr>
        </table>
        
        <br>
        
        <p class="fig"><b>Симетричне бiнарне дерево</b></p>
        
        <table align="center">
            <tr>
                <td></td>
                <td>
                    <samp><%=arrayInt[0]%></samp>
                    <br>
                </td>
                <td></td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: 30px;">/</samp>
                    <br>
                    <samp style="margin-right: 50px;"><%=arrayInt[2]%></samp>
                    <br>
                </td>
                <td></td>
                <td>
                    <samp style="margin-left: 30px;">\</samp>
                    <br>
                    <samp style="margin-left: 50px;"><%=arrayInt[1]%></samp>
                    <br>
                </td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: -15px;">/</samp>
                    <br>
                    <samp style="margin-left: -30px;"><%=arrayInt[5]%></samp>
                    <br>
                </td>
                <td></td>
                <td>
                    
                    <samp style="margin-left: -45px;">\</samp>
                    <br>
                    <samp style="margin-left: -30px;"><%=arrayInt[4]%></samp>
                    <br>
                </td>
                <td>
                    <samp style="margin-left: -30px;">/</samp>
                    <br>
                    <samp style="margin-left: -40px;"><%=arrayInt[3]%></samp>
                    <br>
                </td>
            </tr>
            <tr>
                <td>
                    <samp style="margin-left: 55px;">\</samp>
                    <br>
                    <samp style="margin-left: 60px;"><%=arrayInt[7]%></samp>
                </td>
                <td></td>
                <td>
                    <samp style="margin-left: 15px;">/</samp>
                    <br>
                    <samp style="margin-left: 10px;"><%=arrayInt[6]%></samp>
                </td>
            </tr>
        </table>
        
        <br>
        <p class="fig"><a href="index.jsp">Home</a></p>
    </body>
</html>
