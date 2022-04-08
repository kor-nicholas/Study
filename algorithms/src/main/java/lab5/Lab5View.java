/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 *
 * @author ProBook
 */
public class Lab5View {
    
    public String showWord(String word) {
        
        if (word.equals("")) {
            return "Не правильно введене слово, спробуйте ще раз";
        }
        else {
            return word;
        }
    }
    
}
