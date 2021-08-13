import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n = int(input())
        s = input()
        for i in range(n):
            if s[i] == "1":
                if (i % 2)  == 0:
                    print("Takahashi")
                    return
                else:
                    print("Aoki")
                    return
    do()


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
        input = """5
00101"""
        output = """Takahashi"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
010"""
        output = """Aoki"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()