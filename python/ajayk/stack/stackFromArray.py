class StackArray:

    def __init__(self):
        self.top = -1;
        self.stack_array = [];

    def push(self,value):
        self.top += 1;
        self.stack_array.insert(self.top,value);


    def pop(self):
        if (self.top == -1):
            return 'Stack is Empty';
        top_val = self.stack_array.pop(self.top);
        self.top -= 1;
        return top_val;







