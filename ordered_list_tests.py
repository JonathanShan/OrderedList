import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple1(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)
        t_list.add(5)
        t_list.add(6)
        self.assertEqual(t_list.python_list(), [1,2,3,4,5,6])
        self.assertEqual(t_list.python_list_reversed(), [6,5,4,3,2,1])
        self.assertEqual(t_list.index(4), 3)
        self.assertFalse(t_list.remove(7))
        t_list.add(7)
        self.assertEqual(t_list.add(1), None)
        self.assertTrue(t_list.remove(7))
        self.assertEqual(t_list.pop(4), 5)
        self.assertEqual(t_list.index(10), None)
        self.assertRaises(IndexError, t_list.pop, 10)
        self.assertTrue(t_list.search(6))
        self.assertFalse(t_list.search(8))
if __name__ == '__main__': 
    unittest.main()
