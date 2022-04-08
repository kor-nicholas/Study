/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 *
 * @author ProBook
 */
@SpringBootTest
public class TestAppLab6 {
    
    @Test
    void test(){
        Tree tree = new Tree();
        
        tree.add(4);
        tree.add(11);
        tree.add(2);
        tree.add(9);
        tree.add(6);
        tree.add(16);
        tree.add(8);
        tree.add(3);
        
        assertTrue(tree.containsNode(4));
        assertTrue(tree.containsNode(11));
        assertTrue(tree.containsNode(2));
        assertTrue(tree.containsNode(9));
        assertTrue(tree.containsNode(6));
        assertTrue(tree.containsNode(16));
        assertTrue(tree.containsNode(8));
        assertTrue(tree.containsNode(3));
        
    }
}
