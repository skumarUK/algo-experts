package stack;

import java.util.NoSuchElementException;

public class StackUsingLinkedList {

    private Node headNode;

    private class Node {
        int value;
        Node next;
    }

    public StackUsingLinkedList(){
        headNode = null;
    }


    public void push(Integer element){
        Node oldHead = headNode;
        headNode = new Node();
        headNode.value = element;
        headNode.next = oldHead;
    }

    public Integer pop(){
        if(headNode == null) throw new NoSuchElementException();
        int value = headNode.value;
        headNode = headNode.next;
        return value;
    }

}
