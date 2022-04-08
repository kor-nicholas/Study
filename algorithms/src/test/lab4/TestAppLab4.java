/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab4;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class TestAppLab4 {
    
    
    @Test
    void test () {
        Simple simple = new Simple();
        assertEquals(578,simple.task2());
        assertEquals(262,simple.task3());
        assertEquals(543,simple.task5());
        assertEquals(106,simple.task6());   
    }
}
