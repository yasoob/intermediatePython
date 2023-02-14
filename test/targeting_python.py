from __future__ import print_function
# from future.builtins.disabled import *
import unittest
class TDD_TARGETING_PYTHON(unittest.TestCase):
    def test_targeting_python(self):
        print
        # Output:
        self.assertTrue(callable(print))
    def test_compatible(self):
        try:
            import urllib.request as urllib_request  # for Python 3
            print('??')
        except ImportError:
            import urllib2 as urllib_request  # for Python 2
            print(urllib_request)
    def test_Obsolete_Python2_builtins(self):
        self.assertRaises(NameError,lambda:apply())
if __name__ == '__main__':
    unittest.main()
