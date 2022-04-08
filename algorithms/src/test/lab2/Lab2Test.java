package knu.fit.ist.ta2.lab2;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import static java.lang.Math.log;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class Lab2Test {

    @Test
    void test1() {
        EquationSample equationSample = new EquationSample();
        assertEquals((log(5)/(-9*(5*5)-3*5+9)),equationSample.solve(5),0.01f);
        assertEquals(Integer.MAX_VALUE, equationSample.solve(0.847f), 0.001f);
        assertEquals(Integer.MAX_VALUE, equationSample.solve(-1.18f), 0.01f);
    }
}
