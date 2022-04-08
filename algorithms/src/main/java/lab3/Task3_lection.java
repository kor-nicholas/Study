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
public class Task3_lection {
    
    // a(3a-b)/(3b-a) - однотипний приклад
    
    private double helper (int a, int b) {
        return 3 * a - b;
    }
    
    public double calculate(int a, int b) {
        double result = a * helper(a,b) / helper(a,b);
        return result;
    }
    
}
