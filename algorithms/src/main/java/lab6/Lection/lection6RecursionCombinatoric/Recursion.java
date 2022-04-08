/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6.Lection.lection6RecursionCombinatoric;

/**
 *
 * @author ProBook
 */
public class Recursion {

    public int sum(int n) {

        if (n >= 1) {
            return n + sum(n - 1);
        }
        return n;
    }

    public int tailSum(int result, int n) {

        if (n <= 1) {
            return result + n;
        }
        return tailSum(result + n, n - 1);
    }

    public int iterationSum(int n) {
        int result = 0;

        while (n > 0) {
            result += n;
            n--;
        }

        return result;
    }

    public int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public String toBinary(int n) {
        if (n <= 1) {
            return String.valueOf(n);
        }
        return toBinary(n / 2) + String.valueOf(n % 2);
    }

}
