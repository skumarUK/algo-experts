package stack;

import java.util.NoSuchElementException;

public class StackUsingArray {
    private Integer [] stack;
    private Integer size;
    private Integer top;

    public StackUsingArray(int size){
        stack = new Integer[size];
        size =size;
        top = -1;
    }

    public boolean isFull(){
        return top == size-1;
    }

    public boolean isEmpty(){
        return top ==-1;
    }


    public int pop(){
        if(top ==-1) throw new NoSuchElementException("Stack is Empty.");
        int ele = stack[top];
        top--;
        return ele;
    }

    public int peek(){
        if(top ==-1) throw new NoSuchElementException("Stack is Empty");
        return stack[top];
    }

    public void push(Integer element){
        if(this.isFull()) throw new IllegalStateException("Stack is Full");
        top++;
        stack[top] = element;
    }
}