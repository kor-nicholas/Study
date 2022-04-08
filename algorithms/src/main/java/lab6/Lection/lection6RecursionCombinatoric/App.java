/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6.Lection.lection6RecursionCombinatoric;

import java.util.Arrays;

/**
 *
 * @author ProBook
 */
public class App {
    
    public static void main(String[] args) {
        
        //Recursion recursion = new Recursion();
        
        //System.out.println(recursion.sum(10));
        
        //System.out.println(recursion.tailSum(0,10));
        
        //System.out.println(recursion.iterationSum(10));
        
       //System.out.println(recursion.fibonacci(4));
        
       //System.out.println(recursion.toBinary(52));
        
        
        Combinatoric combinatoric = new Combinatoric();
        //Integer[] input ={1,2,5};
        //System.out.println(combinatoric.generatePermutations(Arrays.asList(input)));
        
       Character[] chars ={'a','b','c','d'};
       System.out.println(combinatoric.generatePowerset(Arrays.asList(chars)));
        
        
        
    }
    
}
