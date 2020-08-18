import unittest
class TDD_GENERATORS(unittest.TestCase):
    def test_generators(self):
        def generator_function():
            for i in range(10):
                yield i
        l=[]
        for item in generator_function():
            l.append(item)
        self.assertEqual(l, list(range(10)))
    def test_large_sets(self):
        # generator version
        def fibon(n):
            a = b = 1
            for i in range(n):
                yield a
                a, b = b, a + b
        g=fibon(1)
        self.assertEqual(next(g),1)
        self.assertRaises(StopIteration,lambda:next(g))
        g=fibon(4)
        self.assertEqual(next(g),1)
        self.assertEqual(next(g),1)
        self.assertEqual(next(g),2)
        self.assertEqual(next(g),3)
        self.assertRaises(StopIteration,lambda:next(g))
    def test_next(self):
        def generator_function():
            for i in range(3):
                yield i
        gen = generator_function()
        self.assertEqual(next(gen),0)
        self.assertEqual(next(gen),1)
        self.assertEqual(next(gen),2)
        self.assertRaises(StopIteration,lambda:next(gen))
    def test_err(self):
        int_var = 1779
        self.assertRaises(TypeError,lambda:next(int_var))
        self.assertRaises(TypeError,lambda:iter(int_var))
        my_string = "Yasoob"
        self.assertRaises(TypeError, lambda: next(my_string))
        my_iter = iter(my_string)
        self.assertEqual(next(my_iter),'Y')
        self.assertEqual(next(my_iter),'a')
if __name__ == '__main__':
    unittest.main()
