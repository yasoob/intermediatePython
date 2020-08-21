
import unittest
class TDD_COROUTINES(unittest.TestCase):
    def test_Coroutines(self):
        def fib(n):
            a, b = 0, 1
            while a<n:
                yield a
                a, b = b, a + b
        l=[]
        for i in fib(10):
            l.append(i)
        self.assertEqual(l,[0,1,1,2,3,5,8])
        def grep(pattern):
            self.assertEqual( pattern,'coroutine')
            while True:
                line = (yield)
                if pattern in line:
                    print(line)
        search = grep('coroutine')
        next(search)
        # # Output: Searching for coroutine
        search.send("I love you")
        search.send("Don't you love me?")
        search.send("I love coroutines instead!")
        search.close()
if __name__ == '__main__':
    unittest.main()

                