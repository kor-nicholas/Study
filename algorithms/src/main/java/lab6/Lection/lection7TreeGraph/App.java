/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6.Lection.lection7TreeGraph;

/**
 *
 * @author ProBook
 */
public class App {

    public static void main(String[] args) {

        /* Tree tree = new Tree();
        
        tree.add(7);
        tree.add(4);
        tree.add(8);
        tree.add(3);
        tree.add(9);
        tree.add(5);
        tree.add(6);
        tree.add(10);
        
        System.out.println(tree.containsNode(6));
        System.out.println(tree.containsNode(67));
        
        tree.traverseInOrder(tree.root);
        System.out.println("");
        tree.traversePreOrder(tree.root);
        System.out.println("");
        tree.traversePostOrder(tree.root);
        System.out.println("");
        tree.traverseLevelOrder(tree.root);
        System.out.println("");
        
        tree.delete(6);
        
        System.out.println(tree.containsNode(6));
        
        tree.traverseInOrder(tree.root);
        System.out.println("");
        tree.traversePreOrder(tree.root);
        System.out.println("");
        tree.traversePostOrder(tree.root);
        System.out.println("");
        tree.traverseLevelOrder(tree.root);
        System.out.println("");
        
        */
        
        Graph graph = new Graph();
        
        graph.addVertex("Bob");
        graph.addVertex("Alice");
        graph.addVertex("Mark");
        graph.addVertex("Rob");
        graph.addVertex("Maria");
        graph.addEdge("Bob", "Alice");
        graph.addEdge("Bob", "Rob");
        graph.addEdge("Alice", "Mark");
        graph.addEdge("Rob", "Mark");
        graph.addEdge("Alice", "Maria");
        graph.addEdge("Rob", "Maria");
        
        System.out.println(graph.depthFirstTraversal(graph, "Bob"));
        System.out.println(graph.breadthFirstTraversal(graph, "Bob"));
        
        
        
    }

}
