class StackUsingArray:

    def __init__(self, size):
        self.stack = [size]
        self.size = size
        self.top = -1

    def push(self, data):
        if self.is_full():
            print('Stack is Full')
        else:
            self.top += 1
            self.stack[self.top] = data
            print('Successfully pushed element to stack')

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            popped = self.stack[self.top]
            self.top -= 1
            print('Successfully popped element from stack')
            return popped

    def is_full(self):
        return self.top == self.size-1

    def is_empty(self):
        return self.top == -1
