import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    numv = int(input())
    e = []
    for i in range(e):
        e.append([])
    for i in range(numv):
        dat = list(map(int, input().split()))
        for j in dat:
            e[i].append(j)
            e[j].append(i)

    # 事前計算
    parent


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
        input = """8
3 1 2 3
2 4 5
0
0
0
2 6 7
0
0
4
4 6
4 7
4 3
5 2"""
        output = """1
1
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()