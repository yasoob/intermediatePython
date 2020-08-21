import unittest
class TDD_LAMBDAS(unittest.TestCase):
    def test_lambdas(self):
        add = lambda x, y: x + y
        self.assertEqual(add(3, 5),8)
        a = [(1, 2), (4, 1), (9, 10), (13, -3)]
        a.sort(key=lambda x: x[1])
        self.assertEqual(a, [(13, -3), (4, 1), (1, 2), (9, 10)])
        list1 = [2,1,  3]
        list2=[7,5,6,4]
        data = zip(list1, list2)
        data = sorted(data)
        list1, list2 = map(lambda t: list(t), zip(*data))
        self.assertEqual(list1,[1,2,3])
        self.assertEqual(list2,[5,7,6])
if __name__ == '__main__':
    unittest.main()
