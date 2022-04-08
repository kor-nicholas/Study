/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab2;

import static java.lang.Math.log;

/**
 *
 * @author ProBook
 */
public class Calculate {
    
    
    public static float lab2equation (float x) {
        if (x==0) { return Integer.MAX_VALUE; }
        else if (x== 0.847f) {return Integer.MAX_VALUE; }
        
        return (float) (log(x)/(-9*(x*x)-3*x+9));
    }
}
