
import unittest
class TDD_EXCEPTIONS(unittest.TestCase):
    def test_Exceptions(self):
        try:
            file = open('test.txt', 'rb')
        except IOError as e:
            pass
            # print('An IOError occurred. {}'.format(e.args[-1]))
        self.assertRaises(IOError, lambda: open('test.txt', 'rb'))
    def test_Handling_multiple_exceptions(self):
        try:
            file = open('test.txt', 'rb')
        except (IOError, EOFError) as e:
            # print("An error occurred. {}".format(e.args[-1]))
            pass
        try:
            file = open('test.txt', 'rb')
        except EOFError as e:
            # print("An EOF error occurred.")
            raise e
        except IOError as e:
            # print("An error occurred.")
            pass
        try:
            file = open('test.txt', 'rb')
        except Exception as e:
            self.assertRaises(FileNotFoundError,lambda:(_ for _ in ()).throw(e))
    def test_finally(self):
        try:
            i=0
            file = open('test.txt', 'rb')
        except IOError as e:
            # print('An IOError occurred. {}'.format(e.args[-1]))
            i+=1
        finally:
            self.assertEqual(i,1)
    def test_try_else_clause(self):
        try:
            print('I am sure no exception is going to occur!')
            i=0
        except Exception:
            print('exception')
        else:
            # any code that should only run if no exception occurs in the try,
            # but for which exceptions should NOT be caught
            print('This would only run if no exception occurs. And an error here '
                'would NOT be caught.')
            i+=1
        finally:
            self.assertEqual(i,1)
if __name__ == '__main__':
    unittest.main()

                