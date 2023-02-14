from pprint import pprint
import unittest
import subprocess
import itertools


class TDD_ONE_LINERS(unittest.TestCase):
    def test_server(self):
        pass
        # subprocess.run('python3 -m http.server', shell=True)

    def test_json(self):
        subprocess.run('cat test/file.json | python -m json.tool', shell=True)

    def test_profiling(self):
        subprocess.run('python3 -m cProfile test/my_script.py', shell=True)

    def test_csv_to_json(self):
        pass
        # subprocess.run('python3 -c "import csv,json;print json.dumps(list(csv.reader(open(\'test/csv_file.csv\'))))"',shell=True)

    def test_one_liners(self):
        my_dict = {'name': 'Yasoob', 'age': 'undefined',
                   'personality': 'awesome'}
        # print(dir(my_dict))
        pprint(dir(my_dict))

    def test_list_flattening(self):
        a_list = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(list(itertools.chain.from_iterable(a_list)), [
                         1, 2, 3, 4, 5, 6])
        self.assertEqual(list(itertools.chain(*a_list)), [1, 2, 3, 4, 5, 6])

    def test_constructors(self):
        class A(object):
            def __init__(self, a, b, c, d, e, f):
                self.__dict__.update(
                    {k: v for k, v in locals().items() if k != 'self'})
        ins = A('a', 'b', 'c', 'd', 'e',  'f')
        p = ins.__dict__
        self.assertEqual(p, {
                         'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f'})
        self.assertEqual(p['a'], 'a')
        self.assertEqual(ins.a,'a')


if __name__ == '__main__':
    unittest.main()
