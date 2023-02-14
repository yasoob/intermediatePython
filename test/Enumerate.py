
import unittest
class TDD_ENUMERATE(unittest.TestCase):
    def test_Enumerate(self):
        my_list = ['apple', 'banana', 'grapes', 'pear']
        d={}
        for counter, value in enumerate(my_list):
            d[counter] = value
        self.assertEqual(d,{0: 'apple', 1: 'banana', 2: 'grapes', 3: 'pear'})
        counter_list = list(enumerate(my_list, 1))
        self.assertEqual(counter_list,[(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')])
if __name__ == '__main__':
    unittest.main()

                