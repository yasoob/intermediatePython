
import unittest
class TDD_ARGS_KWARGS(unittest.TestCase):
    def test_args_kwargs(self):
        def test_var_args(f_arg, *argv):
            return f_arg,*argv

        arg=test_var_args('yasoob', 'python', 'eggs', 'test')
        self.assertEqual(arg,('yasoob', 'python', 'eggs', 'test'))
if __name__ == '__main__':
    unittest.main()

                