import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import math
    INF = 1 << 63
    def do():
        dat = []
        n = int(input())
        for _ in range(n): dat.append(input())
        import collections
        c = collections.Counter(dat)
        x = c.most_common(1)[0]
        print(x[0])

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
snuke
snuke
takahashi
takahashi
takahashi"""
        output = """takahashi"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
takahashi
takahashi
aoki
takahashi
snuke"""
        output = """takahashi"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
a"""
        output = """a"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()