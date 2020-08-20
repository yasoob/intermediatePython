
import unittest
class TDD_VIRTUAL_ENVIRONMENT(unittest.TestCase):
    def test_Virtual_Environment(self):
        import subprocess
        # subprocess.run(["ls", "-l"])
        subprocess.run("pip install virtualenv", shell=True)
if __name__ == '__main__':
    unittest.main()

                