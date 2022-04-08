/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab4;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import org.springframework.stereotype.Service;

/**
 *
 * @author ProBook
 */
@Service
public class StringProcessing {

    String text;
    
    public String getText() {
        return text;
    }

    public StringProcessing(String Text) {
        text = Text;
    }
    
    public StringProcessing() {
        
    }

    public List<String> getList(String text) {
        List<String> result = Arrays.asList(text.split(" "));
        return result;
    }

    public Set<String> getSet(String text) {
        Set<String> result = new HashSet<>();
        result.addAll(Arrays.asList(text.split(" ")));
        return result;
    }
}
