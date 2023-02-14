import unittest
class TDD_OBJECT_INTROSPECTION(unittest.TestCase):
    def test_Object_introspection(self):
        my_list = [1, 2, 3]
        d=dir(my_list)
        # print(d)
        self.assertIsInstance(d, list)
        self.assertTrue('copy' in d)
    def test_type_id(self):
        self.assertEqual(type(''),str)
        self.assertIsInstance('',str)
        self.assertEqual(type([]),list)
        self.assertEqual(type({}),dict)
        self.assertEqual(type(dict),type)
        self.assertEqual(type(3),int)
        name = "Yasoob"
        self.assertIsInstance(id(name),int)
    def test_inspect(self):
        import inspect
        self.assertIsInstance(inspect.getmembers(str),list)
        self.assertIsInstance(inspect.getmembers(str)[0],tuple)
if __name__ == '__main__':
    unittest.main()
