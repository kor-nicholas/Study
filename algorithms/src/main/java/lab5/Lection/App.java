/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5.Lection;

import java.util.List;

/**
 *
 * @author ProBook
 */
public class App {

    private static long time;

    public static void main(String[] args) {

// -------------------------------------- Сортировка ----------------------------------------------------------------    
        
        int maxItems = 1000000;
        Sorting sorting = new Sorting(maxItems);

        //System.out.println("======= Unsorted =======");
        //System.out.println(sorting.getUnsortedList());

        /* System.out.println("======= Sorting Approach1 =======");
        time = System.currentTimeMillis();
        System.out.println(sorting.sortApproach1());
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
        
        System.out.println("======= Sorting Approach2 =======");
        time = System.currentTimeMillis();
        System.out.println(sorting.sortApproach2());
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
        
        System.out.println("======= Merge =======");
        System.out.println(sorting.getUnsortedList().subList(0, 5));
        System.out.println(sorting.getUnsortedList().subList(5, 10));
        
        System.out.println(sorting.mergeLists(
        sorting.getUnsortedList().subList(0, 5),
        sorting.getUnsortedList().subList(5, 10)));
        
        
        
        System.out.println("======= Sorting Approach3 =======");
        time = System.currentTimeMillis();
        System.out.println(sorting.sortApproach3());
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
         */
        
// ------------------------------------------ Поиск -----------------------------------------------------------------        
        
        Searching searching = new Searching();

        System.out.println("======= Sorted =======");
        List<Integer> list = sorting.sortApproach3();

        int find = list.get(list.size() - 1);

        /*System.out.println("======= Linear search =======");
        time = System.currentTimeMillis();
        System.out.println(searching.linearSearch(find, list));
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
        
        System.out.println("======= Binary search =======");
        
        
        time = System.currentTimeMillis();
        System.out.println(searching.binarySearch(find, list));
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
        
        
        
        System.out.println("======= Jump search =======");
        
        
        time = System.currentTimeMillis();
        System.out.println(searching.jumpSearch(find, list, maxItems / 100));
        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);*/
 /*  }*/
 
 /* ----------------------------------------- Много-поточный поиск --------------------------------------------------
        MultiThreadSearch mts = new MultiThreadSearch(find, list.subList(0, maxItems / 2));
        MultiThreadSearch mts1 = new MultiThreadSearch(find, list.subList(maxItems / 2, list.size()));

        time = System.currentTimeMillis();

        new Thread(mts).start();
        new Thread(mts1).start();
        
       
        System.out.println("======= Linear search =======");

        System.out.println(searching.linearSearch(find, list.subList(maxItems / 3, list.size())));

        System.out.println("time (ms):" + (System.currentTimeMillis() - time));

        System.out.println("======= MultiThread Linear search =======");
        System.out.println(mts.getSearchResults());
        System.out.println(mts1.getSearchResults());

        time = System.currentTimeMillis() - time;
        System.out.println("time (ms):" + time);
         */
    }
}
