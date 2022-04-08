/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab3;

import java.text.DecimalFormat;
import org.springframework.stereotype.Service;

/**
 *
 * @author ProBook
 */
@Service
public class Lab3View {
    
    DecimalFormat df = new DecimalFormat("##.###");
    
    public String showResult (String kString) {
        
        Float k = Float.parseFloat(kString);
        
        if (k <= 0) {
            return "Неправильно ведено k, число повинно бути позитивним та не дорiвнювати 0";
        }else {
            return knu.fit.ist.ta2.lab3.Calculate3.lab3equation(k);
        }
    }
}
