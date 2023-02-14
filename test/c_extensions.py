from ctypes import *
import unittest
class TDD_C_EXTENSIONS(unittest.TestCase):
    def test_c_extensions(self):
        import subprocess
        # subprocess.run(["ls", "-l"])
        subprocess.run("gcc -shared -Wl,-install_name,adder.so -o test/adder.so -fPIC test/add.c", shell=True)

        #load the shared object file
        adder = CDLL('test/adder.so')

        #Find sum of integers
        res_int = adder.add_int(4,5)
        self.assertEqual (res_int,9)

        #Find sum of floats
        a = c_float(5.5)
        b = c_float(4.1)

        add_float = adder.add_float
        add_float.restype = c_float
        self.assertEqual (add_float(a, b),9.600000381469727)
if __name__ == '__main__':
    unittest.main()
