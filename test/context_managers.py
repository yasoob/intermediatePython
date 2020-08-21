
import unittest,io
class TDD_CONTEXT_MANAGERS(unittest.TestCase):
    def test_context_managers(self):
        with open('test/some_file', 'w') as opened_file:
            opened_file.write('Hola!')
        opened_file.close()
        f = open('test/some_file')
        data = f.read()
        self.assertEqual(data,'Hola!')
        f.close()
        file = open('some_file', 'w')
        try:
            file.write('Hola!')
            self.assertRaises(io.UnsupportedOperation, file.read)
        finally:
            file.close()
    def test_manager_class(self):
        this=self
        class File(object):
            def __init__(self, file_name, method):
                self.file_obj = open(file_name, method)
            def __enter__(self):
                return self.file_obj
            def __exit__(self, type, value, traceback):
                this.assertEqual(self.file_obj.name,'test/demo.txt')
                type and this.assertTrue(type is AttributeError)
                self.file_obj.close()
                return True
        with File('test/demo.txt', 'w') as opened_file:
            opened_file.write('Hola!')
        with File('test/demo.txt', 'w') as opened_file:
            opened_file.undefined_function('Hola!')
    def test_manager_generator(self):
        from contextlib import contextmanager

        @contextmanager
        def open_file(name):
            f = open(name, 'w')
            try:
                yield f
            finally:
                f.close()
        with open_file('test/some_file') as f:
            f.write('hola!')
            f.close()
        f=open('test/some_file')
        data = f.read()
        self.assertEqual(data, 'hola!')
        f.close()
if __name__ == '__main__':
    unittest.main()

                