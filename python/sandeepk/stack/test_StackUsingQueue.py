from unittest import TestCase

from python.sandeepk.stack.StackUsingQueue import StackUsingQueue


class TestStackUsingQueue(TestCase):

    def test_push(self):
        stack = StackUsingQueue()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(int(stack.top()), 30)
        self.assertEqual(int(stack.size()), 3)

    def test_pop(self):
        stack = StackUsingQueue()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(int(stack.pop()), 30)
        self.assertEqual(int(stack.pop()), 20)
        self.assertEqual(int(stack.top()), 10)
        self.assertEqual(int(stack.size()), 1)

    def test_pop_1(self):
        stack = StackUsingQueue()
        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()
        self.assertEqual(int(stack.top()), -1)
        self.assertEqual(stack.size(), 0)

