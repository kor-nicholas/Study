package knu.fit.ist.ta2.lab3;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class TestApp {

    @Test
    void test1() {
        assertEquals(5,ForTest.forTest(5));
        assertEquals(10,ForTest.forTest(10));
    }
    
    /*Повторить тест 10 раз
    @RepeatedTest(10)
    void test() {
    
    }*/
}
