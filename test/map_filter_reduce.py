
import unittest
class TDD_MAP_FILTER_REDUCE(unittest.TestCase):
    def test_map_filter_reduce(self):
        items = [1, 2, 3, 4, 5]
        squared = []
        for i in items:
            squared.append(i ** 2)
        self.assertEqual(squared,[1,4,9,16,25])
        squared1 = list(map(lambda x: x**2, items))
        self.assertEqual(squared, squared1)
        def multiply(x):
            return (x*x)
        def add(x):
            return (x+x)

        funcs = [multiply, add]
        value=[]
        for i in range(5):
            value .append( list(map(lambda x: x(i), funcs)))
        self.assertEqual(value,[[0,0],[1,2],[4,4],[9,6],[16,8]])
    def test_filter(self):
        number_list = range(-5, 5)
        less_than_zero = list(filter(lambda x: x < 0, number_list))
        self.assertEqual(less_than_zero,[-5,-4,-3,-2,-1])
    def test_reduce(self):
        product = 1
        list = [1, 2, 3, 4]
        for num in list:
            product=product * num
        self.assertEqual(product, 24)
        from functools import reduce
        product1 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
        self.assertEqual(product1,24)
        product1 = reduce((lambda x, y: x * y), [ 3, 4])
        self.assertEqual(product1,12)

if __name__ == '__main__':
    unittest.main()

                