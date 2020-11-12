class Node:
    def __init__(self, value):
        self.value = value;
        self.prev = None;


class StackLinker:
    currentNode = Node;

    def __init__(self):
        self.currentNode = None;

    def push(self,value):
        nextnode = Node(value);
        nextnode.prev = self.currentNode;
        self.currentNode = nextnode;

    def pop(self):
        if (self.currentNode is None):
            return 'Stack is Empty';

        pop_val = self.currentNode.value;
        self.currentNode = self.currentNode.prev;
        return pop_val;


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None;
#         self.prev = None;
#
#
# class StackLinker:
#     currentNode = Node(None);
# #    def __init__(self):
#
#     def push(self,value):
#         nextnode = Node(value);
#         nextnode.prev = StackLinker.currentNode;
#         StackLinker.currentNode = nextnode;
#
#     def pop(self):
#         pop_val = StackLinker.currentNode.value;
#         StackLinker.currentNode = StackLinker.currentNode.prev;
#         return pop_val;










