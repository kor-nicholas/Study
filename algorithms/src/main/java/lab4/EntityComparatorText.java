/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab4;

import java.util.Comparator;

/**
 *
 * @author ProBook
 */
public class EntityComparatorText implements Comparator<Entity>{

    @Override
    public int compare(Entity firstEntity, Entity secondEntity) {
       return firstEntity.getText().compareTo(secondEntity.getText());
        }
    
}