/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5.Lection;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

/**
 *
 * @author ProBook
 */
public class Sorting {

    private Random rnd = new Random(1);
    private List<Integer> unsortedList;

    public List<Integer> getUnsortedList() {
        return unsortedList;
    }

    Sorting(int arrayLength) {

        //List init
        this.unsortedList = new ArrayList<>();
        for (int i = 0; i < arrayLength; i++) {
            unsortedList.add(rnd.nextInt(arrayLength));
        }

    }

    public List<Integer> sortApproach1() {

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

    //insertion sort
    public List<Integer> sortApproach2() {

        int s, t; //temp indexes

        List<Integer> result = new ArrayList<>();
        result.addAll(unsortedList);

        int n = result.size() - 1;
        int k = 0;

        while (k != n) {
            t = k + 1;

            while (t > 0 && result.get(t) < result.get(t - 1)) {
                s = result.get(t);
                result.set(t, result.get(t - 1));
                result.set(t - 1, s);
                t--;
            }

            k++;

        }

        return result;
    }

    public List<Integer> mergeLists(List<Integer> inputList1, List<Integer> inputList2) {
        List<Integer> result = new ArrayList<>();
        int i1 = 0;
        int i2 = 0;

        while (i1 < inputList1.size() || i2 < inputList2.size()) {
            if (!(i1 < inputList1.size())) {
                result.add(inputList2.get(i2));
                i2++;

            } else if (!(i2 < inputList2.size())) {
                result.add(inputList1.get(i1));
                i1++;
            } else {
                if (inputList1.get(i1) <= inputList2.get(i2)) {
                    result.add(inputList1.get(i1));
                    i1++;

                } else {
                    result.add(inputList2.get(i2));
                    i2++;

                }

            }
        }

        return result;
    }

    //merge Sorting
    public List<Integer> sortApproach3() {

        int p, q, r, t;

        List<Integer> result = new ArrayList<>();
        result.addAll(unsortedList);

        int n = result.size() - 1;

        int k = 1;

        while (k < n) {
            List<Integer> tempList = new ArrayList<>();
            t = 0;
            while (t < n+1) {
                p = t;
                q = t + k;
                if (q > n + 1) {
                    q = n + 1;
                }
                r = t + 2 * k;
                if (r > n + 1) {
                    r = n + 1;
                }
                t = r;

               
                tempList.addAll(mergeLists(result.subList(p, q), result.subList(q, r)));
                

            }

            result = tempList;

            k *= 2;
        }

        return result;
    }

    public List<Integer> sortApproach4() {

        List<Integer> result = unsortedList;

        return result;
    }

    public List<Integer> sortApproach5() {

        List<Integer> result = unsortedList;

        return result;
    }
}
