import unittest
class TDD_ARGS_KWARGS(unittest.TestCase):
    def test_args_kwargs(self):
        def test_var_args(f_arg, *argv):
            return f_arg,*argv
        arg=test_var_args('yasoob', 'python', 'eggs', 'test')
        self.assertEqual(arg, ('yasoob', 'python', 'eggs', 'test'))
    def test_kwargs(self):
        def greet_me(**kwargs):
            l=[]
            for key, value in kwargs.items():
                l.append("{0} = {1}".format(key, value))
            return l
        self.assertEqual(greet_me(name="yasoob"),['name = yasoob'])
    def test_call(self):
        def test_args_kwargs(arg1, arg2, arg3):
            return (arg1, arg2, arg3)
        # first with *args
        args = ("two", 3, 5)
        self.assertIsInstance(args,tuple)
        t=test_args_kwargs(*args)
        self.assertEqual(t,args)
        # now with **kwargs:
        kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
        self.assertIsInstance(kwargs,dict)
        t1=test_args_kwargs(**kwargs)
        self.assertCountEqual(t1, tuple(kwargs.values()))
        t2=test_args_kwargs('two', *(3,), **{'arg3': 5})
        self.assertCountEqual(t2,args)
        self.assertRaises(SyntaxError, lambda: eval("test_args_kwargs('two', **{'arg3': 5}, *(3,))"))
    def test_monkey_patching(self):
        class someclass():
            pass
        def get_info(self, *args):
            return "Test data"
        someclass.get_info = get_info
        ins = someclass()
        self.assertEqual(ins.get_info(),'Test data')
if __name__ == '__main__':
    unittest.main()
