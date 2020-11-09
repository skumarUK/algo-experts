from unittest import TestCase

from python.sandeepk.stack.StackUsingArray import StackUsingArray


class TestStackUsingArray(TestCase):

    def test_pop(self):
        a_stack = StackUsingArray()
        a_stack.push('5')
        a_stack.push('6')
        popped = a_stack.pop()
        self.assertEqual(int(popped), 6)

    def test_push(self):
        a_stack = StackUsingArray()
        a_stack.push('5')
        a_stack.push('6')
        self.assertEqual(int(a_stack.head.data), 6)
