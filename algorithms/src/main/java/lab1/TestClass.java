/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab1;

/**
 *
 * @author ProBook
 */
public class TestClass {

    private int example;
    public static int count;

    public TestClass() {
        example = 5;
        count++;
    }

    public TestClass(int example) {
        this.example = example;
        count++;
    }

    public void SetExample(int example) {
        this.example = example;
    }

    public int GetExample() {
        return example;
    }

    @Override
    public String toString() {
        return "Example = " + example;
    }
}
