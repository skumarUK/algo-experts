import unittest
from stackFromArray import StackArray

class TestStackArray(unittest.TestCase):

    def setUp(self):
        self.stack_array = StackArray();

    def test_push(self):

        self.stack_array.push(10)
        self.stack_array.push(20)
        self.stack_array.push(30)
        self.assertEqual(self.stack_array.pop(),30);
        self.assertEqual(self.stack_array.top, 1);
        self.assertEqual(self.stack_array.pop(), 20);
        self.assertEqual(self.stack_array.pop(), 10);
        self.assertEqual(self.stack_array.pop(),'Stack is Empty');


if __name__ == '__main__':
    unittest.main();