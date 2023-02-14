import unittest
class TDD_MUTATION(unittest.TestCase):
    def test_mutation(self):
        foo = ['hi']
        self.assertEqual(foo,['hi'])
        bar = foo
        bar += ['bye']
        self.assertEqual(foo,['hi','bye'])
    def test_never_default_mutable(self):
        def add_to(num, target=[]):
            target.append(num)
            return target

        self.assertEqual(add_to(1),[1])
        self.assertEqual(add_to(2),[1,2])
        self.assertEqual(add_to(3),[1,2,3])
        def add_to(element, target=None):
            if target is None:
                target = []
            target.append(element)
            return target
        self.assertEqual(add_to(1),[1])
        self.assertEqual(add_to(2),[2])
        self.assertEqual(add_to(3),[3])
if __name__ == '__main__':
    unittest.main()
