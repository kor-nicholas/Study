/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class TestAppLab5 {
    
    @Test
    void test_line(){
        Sorting sorting = new Sorting();
        App app = new App();
        app.setWord("iot");
        
        assertEquals(app.getCountObjects(),sorting.linearSearch(app.listObject, app.listObjects));
    }
    
    @Test
    void test_binary(){
        Sorting sorting = new Sorting();
        App app = new App();
        app.setWord("iot");
        
        assertEquals(app.getCountObjects(),sorting.binarySearch(app.listObject, app.listObjects));
    }
    
    @Test
    void test_sort(){
        App app = new App();
        app.setWord("iot");
        app.task1();
        
        assertEquals(17,app.indexList.size());
    }
    
}
