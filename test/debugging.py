
import unittest
class TDD_DEBUGGING(unittest.TestCase):
    def test_stop_execution(self):
        import subprocess
        # subprocess.run(["ls", "-l"])
        subprocess.run("python3 -m pdb test/args_kwargs.py", shell=True)
    def test_debugging(self):
        
        import pdb
# Set 'Whether to run code in integrated terminal' if in vscode. https://stackoverflow.com/a/54879495/2630686
        def make_bread():
            pdb.set_trace()
            # Press letter c to continue when terminal focused
            return "I don't have time"

        self.assertEqual(make_bread(),"I don't have time")
if __name__ == '__main__':
    unittest.main()

                