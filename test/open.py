
import unittest
class TDD_OPEN(unittest.TestCase):
    def test_open(self):
        with open('test/photo.jpg', 'rb') as f:
            jpgdata = f.read()
        self.assertIsInstance(jpgdata,bytes)
        f.close()
    def test_io(self):
        import io

        with open('test/photo.jpg', 'rb') as inf:
            jpgdata = inf.read()

        if jpgdata.startswith(b'\xff\xd8'):
            text = u'This is a JPEG file (%d bytes long)\n'
        else:
            text = u'This is a random file (%d bytes long)\n'

        with io.open('test/summary.txt', 'w', encoding='utf-8') as outf:
            outf.write(text % len(jpgdata))
        inf.close()
        outf.close()
        f=open('test/summary.txt')
        data = f.read()
        self.assertEqual(data,'This is a JPEG file (28573 bytes long)\n')
        f.close()
if __name__ == '__main__':
    unittest.main()

                