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
public class Task0_lection {
    
    public static void main (String[] args) {
        // присвоение значений
        Task0_lection object = new Task0_lection ();
        object.valueProcessing(5); // 5, так как разные объекты
        object.referenceProcessing(9); // 10, так как это ссылки на один и тот же объект
        object.stringProcessing(3); // 3, потому что у класса String сначала старое значение стираеться и потом присваивается новое (как и int, float, ...)
    }
    
    public void valueProcessing(int a) {
        int b = a;
        int c = b; // 2 разных объекта
        c++;
        System.out.println("value b = " + b);
    }
    
    public void referenceProcessing (int a) {
        SomeInt b = new SomeInt (a);
        SomeInt c = b; // ссылки (веревочки) на один и тот же объект
        c.intField++;
        System.out.println("reference b = " + b.intField);
    }
    
    class SomeInt {
        public int intField;
        
        SomeInt (int intField) {
            this.intField = intField;
        }
    }
    
    public void stringProcessing (int a) {
        String b = "" + a;
        String c = b;
        c = "" + ++a;
        System.out.println("String b = " + b);
    }
}
