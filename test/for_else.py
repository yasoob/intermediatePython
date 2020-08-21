
import unittest
class TDD_FOR_ELSE(unittest.TestCase):
    def test_for_else(self):
        fruits = ['apple', 'banana', 'mango']
        l=[]
        for fruit in fruits:
            l.append(fruit.capitalize())
        self.assertEqual(l,['Apple','Banana','Mango'])
    def test_else_clause(self):
        container = []
        not_found_in_container=lambda x:self.assertEqual(x,[])
        for item in container:
            if search_something(item):
                # Found it!
                process(item)
                break
        else:
            # Didn't find anything..
            not_found_in_container(container)
        prime=[]
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                # loop fell through without finding a factor
                prime.append(n)
        self.assertEqual(prime,[2,3,5,7])
if __name__ == '__main__':
    unittest.main()

                