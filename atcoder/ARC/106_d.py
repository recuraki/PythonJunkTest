import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    m = 998244353
    n, m = map(int, input().split())
    dat = map(int, input().split())
    dat = list(dat)

    # k = 1からnまでの k の和
    def sigma1(n):
        return n * (n + 1) // 2

    res = [0] * 310

    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for
    print(total)

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
        input = """3 3
1 2 3"""
        output = """12
50
216"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 10
1 1 1 1 1 1 1 1 1 1"""
        output = """90
180
360
720
1440
2880
5760
11520
23040
46080"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 5
1234 5678"""
        output = """6912
47775744
805306038
64822328
838460992"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()