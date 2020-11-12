import unittest
from stackFromLinkList import StackLinker

class TestStackLinker(unittest.TestCase):

    def setUp(self):
        self.mystack = StackLinker();

    def tearDown(self):
        pass;

    def test_stack(self):
        self.mystack.push(10);
        self.mystack.push(20);
        self.assertEqual(self.mystack.currentNode.value,20)
        self.assertEqual(self.mystack.currentNode.prev.value, 10)
        self.assertEqual(self.mystack.pop(),20)
        self.assertEqual(self.mystack.pop(), 10)
        self.assertEqual(self.mystack.currentNode, None)

    def test_func(self):
        print("Inside Pop");
        self.mystack.push(-10);
        with self.assertRaises(ValueError) as context:
            print ("Raised Value Error")
            self.mystack.pop()

if __name__ == '__main__':
    unittest.main()






