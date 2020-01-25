import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    res = -1
    import collections
    for i in range(a, b + 1):
        s = str(i)
        c = collections.Counter(s)
        can = True
        for k in c:
            if c[k] != 1:
                can = False
        if can:
            res = i
            break


    print(res)


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
        input = """121 130"""
        output = """123"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """98766 100000"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()