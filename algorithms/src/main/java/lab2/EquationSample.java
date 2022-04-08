/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab2;

import static java.lang.Math.log;
import org.springframework.stereotype.Component;

/**
 *
 * @author ProBook
 */

@Component
public class EquationSample {
    
    //public static void main (String[] args) {
      //  System.out.println((log(5)/(-9*(5*5)-3*5+9)));
    //} //-0.00696726369019091 
    
    public  float solve(int x) {
        if (x==0) { return Integer.MAX_VALUE; }
        
        return (float) (log(x)/(-9*(x*x)-3*x+9)); // можливе дiлення на 0 
    }
    
    public  float solve(float x) {
        if (x==0) { return Integer.MAX_VALUE; }
        else if (x== 0.847f) {return Integer.MAX_VALUE; }
        else if (x== -1.18f) {return Integer.MAX_VALUE; }
        
        return (float) (log(x)/(-9*(x*x)-3*x+9)); // можливе дiлення на 0 
    }
}
