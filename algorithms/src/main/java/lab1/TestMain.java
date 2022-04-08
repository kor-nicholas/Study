/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab1;

import java.text.DecimalFormat;
import static javax.swing.text.html.parser.DTDConstants.PI;

/**
 *
 * @author ProBook
 */
public class TestMain {
    public static void main(String[] args) {
        TestClass clas = new TestClass();
        TestClass clas2 = new TestClass(6);

        System.out.println("Count (about) : " + TestClass.count);

        clas.SetExample(9);
        System.out.println("Get_1 : " + clas.GetExample());
        System.out.println(clas.toString());

        System.out.println("Get_2 : " + clas2.GetExample());
        System.out.println(clas2.toString());

        System.out.println("Count (after) : " + TestClass.count);
        
        DecimalFormat df = new DecimalFormat("#.##");
        System.out.println(df.format(PI));
        
        float f1 = 2.035f;
        float f2 = 2.036f;
        
        
        System.out.println(Math.abs(f1-f2)<=0.01f);
        
        
    }
}
