/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab3;

import org.springframework.stereotype.Component;

/**
 *
 * @author ProBook
 */


public class ForTest {
    public static int forTest(float k) {
        float[] arr = new float[(int) k + 1];

        for (int i = 0; i < k; i++) {
            arr[i] = i;
        }

        int length = 1,
            count = 0,
            max = 0;

        for (int i = 0; i < (int) k; i++) {
            if (arr[i + 1] > arr[i]) {
                length++;
            } else if (length != 1) {
                count++;
                length = 1;
            }
        }

        int[] arr2 = new int[count + 1];

        length = 1;
        for (int i = 0, j = 0; i < (int) k && j < count; i++) {
            if (arr[i + 1] > arr[i]) {
                length++;
            } else if (length != 1) {
                arr2[j] = length;
                j++;
                length = 1;
            }
        }

        max = arr2[0];
        for (int i = 0; i < count; i++) {
            if (arr2[i] > max) {
                max = arr2[i];
            }
        }

        return max; // елемент 1, але ми шукаемо РОЗМiР
    }
}