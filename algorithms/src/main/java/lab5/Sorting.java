/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author ProBook
 */
public class Sorting {

    public List<Integer> sortApproach1(List<Integer> unsortedList) {

        int s, t; //temp indexes

        List<Integer> result = new ArrayList<>();
        result.addAll(unsortedList);

        int n = result.size() - 1;
        int k = -1; //all unsorted

        //Put current minimal element into its place
        while (k != n) {
            s = k + 1;
            t = s;

            //find minimal elevent (index s) in index rang [k,n]
            while (t != n) {
                t++;
                if (result.get(t) < result.get(s)) {
                    s = t;
                }
            }

            // exchange elements with indexes s and k+1
            t = result.get(k + 1);
            result.set(k + 1, result.get(s));
            result.set(s, t);

            k++;
        }

        return result;
    }

    public int linearSearch(ListObject find, List<ListObject> list) {

        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).equals(find)) {
                return list.indexOf(list.get(i));
            }
        }
        
        return -1;
    }

    public int linearSearch(ListObject find, int start, List<ListObject> list) {

        for (int i = start; i < list.size(); i++) {
            if (list.get(i).equals(find)) {
                return list.indexOf(list.get(i));
            }
        }
        return -1;
    }

    public int linearSearch(ListObject find, int start, int finish, List<ListObject> list) {

        for (int i = start; i < finish; i++) {
            if (list.get(i).equals(find)) {
                return list.indexOf(list.get(i));
            }
        }
        return -1;
    }

    public int binarySearch(ListObject find, List<ListObject> sortedList) {

        int start = 0;
        int n = sortedList.size() - 1;
        while (n > 1) {

            if (start + n > sortedList.size()) {
                start--;
            }
            n = (n + 1) / 2;

            if (sortedList.get(n + start).equals(find)) {
                return sortedList.indexOf(sortedList.get(start + n));
            } else if (sortedList.get(n + start).getSh() < find.getSh()) {
                start = start + n;
            }

        }

        return sortedList.size() - 1;
    }
}
