import unittest
class TDD_GLOBAL_RETURN(unittest.TestCase):
    def test_global_return(self):
        def add(value1, value2):
            result=value1 + value2
            return result
        add(3, 5)
        self.assertRaises(NameError,lambda:result)
        result = add(3, 5)
        self.assertEqual(result, 8)
        def add(value1,value2):
            global result1
            result1 = value1 + value2
        add(3,5)
        self.assertEqual(result1,8)
    def test_multiple_return(self):
        def profile():
            global name
            global age
            name = "Danny"
            age = 30
        profile()
        self.assertEqual(name,'Danny')
        self.assertEqual(age,30)
        def profile():
            name = "Danny"
            age = 30
            return (name, age)
        profile_data = profile()
        self.assertEqual(profile_data[0],'Danny')
        self.assertEqual(profile_data[1],30)
        def profile():
            name = "Danny"
            age = 30
            return name, age
        profile_name, profile_age = profile()
        self.assertEqual(profile_data[0],'Danny')
        self.assertEqual(profile_data[1],30)
    def test_namedtuple(self):
        from collections import namedtuple
        def profile():
            Person = namedtuple('Person', 'name age')
            return Person(name="Danny", age=31)
        # Use as namedtuple
        p = profile()
        self.assertIsInstance(p, object)
        self.assertEqual(p.name,'Danny')
        self.assertEqual(p.age,31)
        # Use as plain tuple
        p = profile()
        self.assertEqual(p[0],'Danny')
        self.assertEqual(p[1],31)
        # Unpack it immediatly
        name, age = profile()
        self.assertEqual(name,'Danny')
        self.assertEqual(age,31)
if __name__ == '__main__':
    unittest.main()
