/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab6.Lection.lection7TreeGraph;

import java.util.LinkedList;
import java.util.Queue;

/**
 *
 * @author ProBook
 */
public class Tree {

    Node root;
    
    public Node getRoot() {
        return root;
    }
    
    public void printRoot(Node root) {
        
        Queue<Node> level = new LinkedList<>();
        level.add(root);
        
        while(!level.isEmpty()) {
            Node node = level.poll();
            System.out.println(node.value + " ");
            if (node.left != null) {
                level.add(node.left);
            }
            if (node.right != null) {
                level.add(node.right);
            }
        }
    }
    
    public void mirrorTree(Node root) {
        if(null == root) {
            return;
        }
        mirrorTree(root.left);
        mirrorTree(root.right);
        Node swapNode = root.left;
        root.left = root.right;
        root.right = swapNode;
        return;
    }

    private Node addRecursive(Node current, int value) {
        if (current == null) {
            return new Node(value);
        }

        if (value < current.value) {
            current.left = addRecursive(current.left, value);
        } else if (value > current.value) {
            current.right = addRecursive(current.right, value);
        } else {
            // value already exists
            return current;
        }

        return current;
    }

    public void add(int value) {
        root = addRecursive(root, value);
    }

    private boolean containsNodeRecursive(Node current, int value) {
        if (current == null) {
            return false;
        }
        if (value == current.value) {
            return true;
        }
        return value < current.value
                ? containsNodeRecursive(current.left, value)
                : containsNodeRecursive(current.right, value);
    }

    public boolean containsNode(int value) {
        return containsNodeRecursive(root, value);
    }
}
