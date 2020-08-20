
import unittest
class TDD_SLOTS(unittest.TestCase):
    def test_slots(self):
        class MyClass(object):
            def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier
                self.set_up()
            def set_up(self):
                pass
        class MyClass1(object):
            # reduce the burden on your RAM
            __slots__ = ['name', 'identifier']
            def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier
                self.set_up()
            def set_up(self):
                pass
        self.assertEqual(MyClass('n','i').identifier,'i')
        self.assertEqual(MyClass1('n', 'i').identifier, 'i')
    def test_memory_usuage(self):
        # Python 3.4.3 (default, Jun  6 2015, 13:32:34)
        # Type "copyright", "credits" or "license" for more information.

        # IPython 4.0.0 -- An enhanced Interactive Python.
        # ?         -> Introduction and overview of IPython's features.
        # %quickref -> Quick reference.
        # help      -> Python's own help system.
        # object?   -> Details about 'object', use 'object??' for extra details.

        # In [1]: import ipython_memory_usage.ipython_memory_usage as imu

        # In [2]: imu.start_watching_memory()
        # In [2] used 0.0000 MiB RAM in 5.31s, peaked 0.00 MiB above current, total RAM usage 15.57 MiB

        # In [3]: %cat slots.py
        class MyClass(object):
                __slots__ = ['name', 'identifier']
                def __init__(self, name, identifier):
                        self.name = name
                        self.identifier = identifier

        num = 1024*256
        x = [MyClass(1,1) for i in range(num)]
        # In [3] used 0.2305 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 15.80 MiB

        # In [4]: from slots import *
        # In [4] used 9.3008 MiB RAM in 0.72s, peaked 0.00 MiB above current, total RAM usage 25.10 MiB

        # In [5]: %cat noslots.py
        class MyClass(object):
                def __init__(self, name, identifier):
                        self.name = name
                        self.identifier = identifier

        num = 1024*256
        x = [MyClass(1,1) for i in range(num)]
        # In [5] used 0.1758 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 25.28 MiB

        # In [6]: from noslots import *
        # In [6] used 22.6680 MiB RAM in 0.80s, peaked 0.00 MiB above current, total RAM usage 47.95 MiB
if __name__ == '__main__':
    unittest.main()

                