/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab4;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;

/**
 *
 * @author ProBook
 */
public class Demo {
    private List<Entity> resultList;

    public void calculateResult(Collection<String> listIn) {

        Iterator<String> iterator = listIn.iterator();
        resultList = new ArrayList<>();
        while (iterator.hasNext()) {
            Entity tempEntity = new Entity(iterator.next(), 1);

            if (resultList.contains(tempEntity)) {
                resultList.get(resultList.indexOf(tempEntity)).countIncrement();
            } else {
                resultList.add(tempEntity);
            }
        }

    }

    public void calculateResult(Collection<String> listIn, int sequenceCount) {
        resultList = new ArrayList<>();
        Iterator<String> iterator = listIn.iterator();

        while (iterator.hasNext()) {
            String word = iterator.next();

            if (word.length() >= sequenceCount) {
                for (int i = 0; i < word.length() - sequenceCount; i++) {
                    String tempResult = word.substring(i, i + sequenceCount);
                    Entity tempEntity = new Entity(tempResult, 1);

                    if (resultList.contains(tempEntity)) {
                        resultList.get(resultList.indexOf(tempEntity)).countIncrement();
                    } else {
                        resultList.add(tempEntity);
                    }
                }

            }

        }

    }

    public List<Entity> getResultList() {
        resultList.sort(new EntityComparatorCount()
                .reversed()
                .thenComparing(new EntityComparatorText()));
        return resultList;
    }
}
