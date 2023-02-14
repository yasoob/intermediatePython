
import unittest
class TDD_DATA_STRUCTURE(unittest.TestCase):
    def test_set_data_structure(self):
        some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

        duplicates = []
        for value in some_list:
            if some_list.count(value) > 1:
                if value not in duplicates:
                    duplicates.append(value)

        self.assertEqual(duplicates, ['b', 'n'])
        duplicates1 = list(set([x for x in some_list if some_list.count(x) > 1]))
        self.assertCountEqual(duplicates1,duplicates)
    def test_intersection(self):
        valid = set(['yellow', 'red', 'blue', 'green', 'black'])
        input_set = set(['red', 'brown'])
        self.assertEqual(input_set.intersection(valid),{'red'})
    def test_difference(self):
        valid = set(['yellow', 'red', 'blue', 'green', 'black'])
        input_set = set(['red', 'brown'])
        self.assertEqual(input_set.difference(valid),{'brown'})
        self.assertEqual(valid.difference(input_set),{'yellow','blue','green','black'})
        a_set = {'red', 'blue', 'green'}
        self.assertIsInstance(a_set,set)

if __name__ == '__main__':
    unittest.main()

                