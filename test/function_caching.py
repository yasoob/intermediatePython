from functools import wraps
import unittest
class TDD_FUNCTION_CACHING(unittest.TestCase):
    def test_function_caching(self):
        from functools import lru_cache
        @lru_cache(maxsize=32)
        def fib(n):
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        l=([fib(n) for n in range(10)])
        self.assertEqual(l, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        fib.cache_clear()
        self.assertEqual(l, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    def test_python2_plus(self):
        def memoize(function):
            memo = {}
            @wraps(function)
            def wrapper(*args):
                try:
                    return memo[args]
                except KeyError:
                    rv = function(*args)
                    memo[args] = rv
                    return rv
            return wrapper
        @memoize
        def fibonacci(n):
            if n < 2: return n
            return fibonacci(n - 1) + fibonacci(n - 2)
        self.assertEqual(fibonacci(25),75025)
if __name__ == '__main__':
    unittest.main()
