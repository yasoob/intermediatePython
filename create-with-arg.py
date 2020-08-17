import sys,os

print(sys.argv)


def main():
    l = sys.argv[1].split("/")
    alist = [
        [
            l[-1].upper(),
            l[-1],
            ','+sys.argv[2] if len(sys.argv)>=3 else ''
        ]
        ]
    dirName = '/'.join(l[:-1])
    # Create target directory & all intermediate directories if don't exists
    try:
        print("Directory " , dirName ,  " Created ")
        os.makedirs(dirName)
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
    for item in alist:
        f = open(sys.argv[1] + ".py", "w+")
        # for i in range(10):
        #      f.write("This is line %d\r\n" % (i+1))
        content = """
import unittest{2}
class TDD_{0}(unittest.TestCase):
    def test_{1}(self):

if __name__ == '__main__':
    unittest.main()

                """
        f.write(content.format(item[0], item[1],item[2]))
        f.close()


if __name__ == "__main__":
    main()
