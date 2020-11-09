from unittest import TestCase

from python.sandeepk.stack.StackUsingArray import StackUsingArray


class TestStackUsingArray(TestCase):
    def test_push(self):
        a_stack = StackUsingArray(10)
        a_stack.push(10)
        self.assertEqual(int(a_stack.pop()), 10)

    def test_pop(self):
        a_stack = StackUsingArray(10)
        a_stack.push(6)
        self.assertEqual(int(a_stack.pop()), 6)
