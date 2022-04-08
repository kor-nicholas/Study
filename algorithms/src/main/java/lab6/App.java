/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6;

/**
 *
 * @author ProBook
 */
public class App {
    // Варіант13. 
    //1.Створити симетричне бінарне дерево пошуку з елементів:
    //{4, 11, 2, 9, 6, 16, 8, 3}.
    //(написати окремий метод для визначення порядку додавання елементів до дерева)
 
    //2.Вивести на екран початкове дерево та результати виконання операцій над ним, що розглядалися на занятті
    
    // Теория : 
    // Бiнарне дерево - на графах коли з каждого елемента (круга) виходить не бIЛьше 2 стрiлочок
    // Вiдсортоване - влiво значення менше; вправо - значення бiльше
    
    Tree tree = new Tree();
    
    public int[] task1() {
        
        tree.add(4);
        tree.add(11);
        tree.add(2);
        tree.add(9);
        tree.add(6);
        tree.add(16);
        tree.add(8);
        tree.add(3);
        
        return tree.arrayValueInRoot();
    }
    
    public int[] task2() {
        tree.mirrorTree(tree.root);
        
        return tree.arrayValueInRoot();
    }
    
}
