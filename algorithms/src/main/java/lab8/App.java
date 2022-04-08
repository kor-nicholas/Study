/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab8;

import java.util.Random;

/**
 *
 * @author ProBook
 */
public class App {
    /*long time = System.currentTimeMillis(); ... ; time = System.currentTimeMillis() - time;*/
    
    Random rnd = new Random();
    int[] arr = new int[45000];
    
    public void init() {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rnd.nextInt();
        }
        arr[40000] = 50;
    }
    
    public int linearSearch(int[]arr, int elementToSearch) {
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == elementToSearch) {
                return i;
            }
        }
        
        return -1;
    }
    
    public long timeLinearSearch() {
        
        long time = System.currentTimeMillis();
        
        linearSearch(arr, 50);
        
        time = System.currentTimeMillis() - time;
        
        return time;
    }
    
    public static int binarySearch(int arr[], int elementToSearch) {

    int firstIndex = 0;
    int lastIndex = arr.length - 1;

    while(firstIndex <= lastIndex) {
        int middleIndex = (firstIndex + lastIndex) / 2;
        
        if (arr[middleIndex] == elementToSearch) {
            return middleIndex;
        }

        else if (arr[middleIndex] < elementToSearch)
            firstIndex = middleIndex + 1;

        else if (arr[middleIndex] > elementToSearch)
            lastIndex = middleIndex - 1;

    }
    
    return -1;
}
    
    public long timeBinarySearch() {
        int[] arr2 = bubbleSort(arr);
        
        long time = System.currentTimeMillis();
        
        binarySearch(arr2, 50);
        
        time = System.currentTimeMillis() - time;
        
        return time;
    }
    
    private static int[] bubbleSort(int[] arr){
     
    for(int i = arr.length-1 ; i > 0 ; i--){
        for(int j = 0 ; j < i ; j++){
            
            if( arr[j] > arr[j+1] ){
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
    return arr;
}
}
