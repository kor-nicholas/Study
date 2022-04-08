/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab3;

import java.text.DecimalFormat;
import java.util.Random;

/**
 *
 * @author ProBook
 */
public class Calculate3 {
    
	public static String lab3equation(float k) {

                String result = "";
		Random rand = new Random();
		float[] arr = new float[(int) k + 1];
		DecimalFormat df = new DecimalFormat("#.####");

                result += "Массив : ";
                
		for (int i = 0; i < (int) k; i++) {
			arr[i] = rand.nextFloat();
                        result += arr[i];
                        result += ", ";
		}
                
                StringBuffer stringBuffer = new StringBuffer(result);
                stringBuffer.delete(result.length() - 2, result.length());
                result = stringBuffer.toString();
                result += " ; ";

		int length = 1,
		count = 0,
		max = 0;

		for (int i = 0; i < (int) k; i++) {
			if (arr[i + 1] > arr[i]) {
				length++;
			} else if (length != 0) {
				count++;
				length = 1;
			}
		}

		int[] arr2 = new int[count + 1];

		length = 1;
		for (int i = 0, j = 0; i < (int) k && j < count; i++) {
			if (arr[i + 1] > arr[i]) {
				length++;
			} else if (length != 0) {
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
                
                result += "Розмір найдовшої зростаючої послідовності : " + max;

		return result;
	}

}