from queue import Queue


# Stack is Last in first out
# Queue is first in first out

class StackUsingQueue:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def push(self, data):
        self.curr_size += 1
        self.q2.put(data)
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        self.q = self.q2
        self.q2 = self.q1
        self.q1 = self.q

    def pop(self):
        if self.q1.empty():
            print('Stack is Empty')
        ele = self.q1.get()
        self.curr_size -= 1
        return ele

    def size(self):
        return self.curr_size

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]
