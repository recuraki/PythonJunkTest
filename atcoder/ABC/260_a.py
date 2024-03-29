
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def main():
        s = input()
        import collections
        c = collections.Counter(list(s))
        for k in c.keys():
            if c[k] == 1:
                print(k)
                return
        print(-1)
    main()

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """pop"""
        output = """o"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """abc"""
        output = """a"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()