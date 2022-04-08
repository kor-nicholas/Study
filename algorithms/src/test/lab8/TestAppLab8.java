/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab8;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class TestAppLab8 {
    
    @Test
    void test(){
        App app = new App();
        
        app.init();
        assertEquals(40000,app.linearSearch(app.arr, 50));
    }
}
