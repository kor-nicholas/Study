/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab3;

/**
 *
 * @author ProBook
 */
public class Task1_lection {
    
    public static void main (String[] args) {
        Task1_lection object = new Task1_lection();
        
        //object.p11b(8, 3);
        //object.p113(2, 10);
        //object.p1121(10);
        //object.reverseInt(456);
    }
    
    // алгоритмы
    private int a, b, c, n, k, i;
    
    // поменять местами значение переменных
    public void p11b(int a, int b) {
        sout("a <- -> b");
        sout(a,b);
        a += b; // a = a + b
        b = a - b; // b = a + b - b = a
        a -= b; // a = a + b(старое); a -= b(новое)
        sout(a,b);
    }
    
    // возвести а в степень n
    // 2 ^ 32 = 0, потому что это грань int
    public void p113 (int a, int n) {
        k = 0; // счетчик сколько раз умножать
        b = 1; // результат
        sout("a^b");
        sout(a,n);
        if (n < 0) {
            sout("должно быть позитивное число");
            b = 0;
        } else if (n < 1) {
            sout(b);
        } else {
            while (k++ != n) {
                // k != n; k++
                b *= a;
            }
            sout(b);
        }
        sout(b);
    }
    
    // Вывести послидовность квадратов N чисел
    public void p1121 (int n) {
        k = 0;
        int square = 0;
        sout(square);
        
        while (k != n) {
            square += k;
            k++;
            square += k;
            sout(square);
        }
    }
    
    // Записати число в зворотньому порядку
    public void reverseInt(int startInt) {
        int reverseInt = 0;
        k = startInt;
        
        while (k != 0) {
            reverseInt = reverseInt * 10 + k % 10;
            k /= 10;
        }
        sout(reverseInt);
    }
    
    
    // Дополнительные методы для удобства вывода
    public void sout (String message) {
        System.out.println(message);
    }
    
    public void sout (Number a) {
        System.out.println("result = " + a);
    }
    
    public void sout (Number a, Number b) {
        System.out.println("a = " + a + " ; b = " + b);
    }
    
    public void sout (Number a, Number b, Number c) {
        System.out.println("a = " + a + " ; b = " + b + " ; c = " + c);
    }
    // Number - родительский класс int, float, ...
}
