
import unittest
class TDD_TERNARY_OPERATORS(unittest.TestCase):
    def test_ternary_operators(self):
        is_nice = True
        state = "nice" if is_nice else "not nice"
        self.assertEqual(state,'nice')
    def test_bool(self):
        nice = True
        personality = ("mean", "nice")[nice]
        self.assertEqual(personality,'nice')
        personality1 = ( "nice","mean")[nice]
        self.assertEqual(personality1, 'mean')
        condition = True
        self.assertEqual(2 if condition else 1/0,2)
        self.assertRaises(ZeroDivisionError,lambda:(1/0, 2)[condition])
    def test_shorthand_ternary(self):
        self.assertTrue(True or "Some")
        self.assertEqual(False or "Some",'Some')
        output = None
        msg = output or "No data returned"
        self.assertEqual(msg,'No data returned')
    def test_default_parameter(self):
        def my_function(real_name, optional_display_name=None):
            optional_display_name = optional_display_name or real_name
            return (optional_display_name)
        self.assertEqual(my_function("John"),'John')
        self.assertEqual(my_function("Mike", "anonymous123"),'anonymous123')
if __name__ == '__main__':
    unittest.main()

                