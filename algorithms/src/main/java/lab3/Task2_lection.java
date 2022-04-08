/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab3;

import java.util.Random;

/**
 *
 * @author ProBook
 */
public class Task2_lection {
    
    // Массивы + класс Random
    
    Random random = new Random();
    Random rand = new Random(5);
    // Если передаем в класс число, то 
    // постоянно получаем одну и ту же последовательность
        
    
    public int[] arrayIntRandom (int arrayLength, int arrayMax) {
        int[] result = new int[arrayLength]; // Статические массивы
        // int[result] = {1,2,3,4,5};
        
        for (int i = 0; i<arrayLength ; i++) {
            result[i] = random.nextInt(arrayMax + 1); // рандомное число до arrayMax
        }
        return result;
    }
    
    // Для вывода массива на экран 
    public String arrayPrint (int[] intArray) {
        String result = "{";
        
        // цикл for each - в переменную i помещаются все елменты массива
        for (int i : intArray) {
            result += i + ", ";
        }
        // удаление 2 последних елементов
        result = result.substring(0, result.length()-2);
        result += "}";
        return result;
    }
    
    // Генерация массива от 1 до n
    public int[] arrayRange(int n) {
        int[] result = new int[n];
        for (int i = 0; i < n ;i++) {
            result[i] = i + 1;
        }
        return result;
    }
    
    // Перемешование
    public int[] arrayShuffle (int[] array) {
        Random rand = new Random();
        
        int temp;
        int ar1 = array.length;
        for (int i = 0; i < ar1 ;i++) {
            int indexToSwap = rand.nextInt(ar1);
            temp = array[indexToSwap];
            array[indexToSwap] = array[i];
            array[i] = temp;
        }
        return array;
    }
    
    // последовательность из квадратов первых n N чисел
    public String arrayString(int n) {
        String result = "";
        for (int i = 0; i <= n ;i++) {
            result += i*i;
        }
        return result;
    }
}
