/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6.Lection.lection6RecursionCombinatoric;

import java.util.ArrayList;
import static java.util.Collections.swap;
import java.util.List;

/**
 *
 * @author ProBook
 */
public class Combinatoric {

    private void permutationsInternal(List<Integer> sequence, List<List<Integer>> permutations, int index) {
        if (index == sequence.size() - 1) {
            permutations.add(new ArrayList<>(sequence));
        }

        for (int i = index; i < sequence.size(); i++) {
            swap(sequence, i, index);
            permutationsInternal(sequence, permutations, index + 1);
            swap(sequence, i, index);
        }

    }

    public List<List<Integer>> generatePermutations(List<Integer> sequence) {
        List<List<Integer>> permutations = new ArrayList<>();
        permutationsInternal(sequence, permutations, 0);
        return permutations;
    }
    
    

    private void powerSetInternal(
            List<Character> set, List<List<Character>> powerset, List<Character> accumulator, int index) {
        if (index == set.size()) {
            powerset.add(new ArrayList<>(accumulator));
        } else {
            accumulator.add(set.get(index));
            powerSetInternal(set, powerset, accumulator, index + 1);
            accumulator.remove(accumulator.size() - 1);
            powerSetInternal(set, powerset, accumulator, index + 1);
        }
    }

    public  List<List<Character>> generatePowerset(List<Character> sequence) {
        List<List<Character>> powerset = new ArrayList<>();
        powerSetInternal(sequence, powerset, new ArrayList<>(), 0);
        return powerset;
    }

}
