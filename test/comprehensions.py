from collections.abc import Iterable
import unittest
class TDD_COMPREHENSIONS(unittest.TestCase):
    def test_comprehensions(self):
        multiples = [i for i in range(30) if i % 3 == 0]
        self.assertEqual(multiples,[0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
        squared = []
        for x in range(10):
            squared.append(x**2)
        self.assertEqual(squared, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
        squared1=[x**2 for x in range(10)]
        self.assertEqual(squared,squared1)
    def test_dict(self):
        mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

        mcase_frequency = {
            k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
            for k in mcase.keys()
        }
        self.assertEqual(mcase_frequency,{'a':17,'b':34,'z':3})
        self.assertEqual({v: k for k, v in mcase.items()},{10:'a',34:'b',7:'A',3:'Z'})
    def test_set(self):
        squared = {x**2 for x in [1, 1, 2]}
        self.assertEqual(squared,{1,1,4})
    def test_generator(self):
        multiples_gen = (i for i in range(10) if i % 3 == 0)
        self.assertIsInstance(multiples_gen, Iterable)
        l=[]
        for x in multiples_gen:
            l.append(x)
        self.assertEqual([0,3,6,9],l)
        self.assertEqual(list(multiples_gen),[])

if __name__ == '__main__':
    unittest.main()

                