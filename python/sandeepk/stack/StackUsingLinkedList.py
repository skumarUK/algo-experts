class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLinkedList:
    head = Node

    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            raise Exception('Empty Stack')
        ele = self.head.data
        self.head = self.head.next
        print('successfully popped value from stack')
        return ele

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print('successfully push data to stack')


# a_stack = StackUsingArray()
# while True:
#     print('push <value>')
#     print('pop ')
#     print('quit')
#     do = input('what would you like to do? ').split()
#
#     operation = do[0].strip().lower()
#     if operation == 'push':
#         a_stack.push(int(do[1]))
#     elif operation == 'pop':
#         popped = a_stack.pop()
#         if popped is None:
#             print('Stack is Empty')
#         else:
#             print('Popped value: ', int(popped))
#     elif operation == 'quit':
#         break
