import unittest
class TDD_CLASSES(unittest.TestCase):
    def test_Classes(self):
        class Cal(object):
            # pi is a class variable
            pi = 3.142
            def __init__(self, radius):
                # self.radius is an instance variable
                self.radius = radius
            def area(self):
                return self.pi * (self.radius ** 2)
        a = Cal(32)
        self.assertEqual(a.area(),Cal.pi*a.radius**2)
        self.assertEqual(a.pi,3.142)
        a.pi = 43
        self.assertEqual(a.pi,43)
        b = Cal(44)
        self.assertEqual(b.area(),3.142*44**2)
        self.assertEqual(b.pi,3.142)
        b.pi = 50
        self.assertEqual(b.pi,50)
    def test_mutable_class_var(self):
        class SuperClass(object):
            superpowers = []
            def __init__(self, name):
                self.name = name
            def add_superpower(self, power):
                self.superpowers.append(power)
        foo = SuperClass('foo')
        bar = SuperClass('bar')
        self.assertEqual(foo.name,'foo')
        self.assertEqual(bar.name,'bar')
        self.assertEqual(bar.superpowers,[])
        foo.add_superpower('fly')
        self.assertEqual(bar.superpowers,['fly'])
        self.assertEqual(bar.superpowers,foo.superpowers)
    def test_new_style_class(self):
        class OldClass():
            def __init__(self):
                pass
        class NewClass(object):
            def __init__(self):
                pass
        old = OldClass()
        new = NewClass()
        self.assertIsInstance(old,object)
        self.assertIsInstance(new,object)
    def test_magic_methods(self):
        class GetTest(object):
            def __init__(self,i=0):
                self.i=i+1
            def another_method(self):
                self.i+=1
        a = GetTest()
        self.assertEqual(a.i,1)
        a.another_method()
        self.assertEqual(a.i,2)
        class GetTest(object):
            def __init__(self, name):
                self.greet=('Greetings!! {0}'.format(name))
            def another_method(self):
                print('I am another method which is not'
                    ' automatically called')
        a = GetTest('yasoob')
        self.assertEqual(a.greet,'Greetings!! yasoob')
        # Try creating an instance without the name arguments
        self.assertRaises(TypeError, lambda: GetTest())
        self.assertRaises(TypeError,lambda:a['name'])
    def test_getitem(self):
        class GetTest(object):
            def __init__(self):
                self.info = {
                    'name':'Yasoob',
                    'country':'Pakistan',
                    'number':12345812
                }
            def __getitem__(self,i):
                return self.info[i]
        foo = GetTest()
        self.assertEqual(foo['name'],'Yasoob')
        self.assertEqual(foo['number'],12345812)
if __name__ == '__main__':
    unittest.main()
