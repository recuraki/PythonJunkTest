import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dath = list(map(int, input().split()))
    datab = []
    ishigh = [True] * n
    for i in range(m):
        a,b = map(int, input().split())
        #print(a,b)
        a-=1
        b-=1
        #print(ishigh)
        if dath[a] >= dath[b]:
            ishigh[b] = False
        if dath[a] <= dath[b]:
            ishigh[a] = False
    #print(ishigh)
    res = 0
    for i in range(len(ishigh)):
        if ishigh[i] is True:
            res += 1
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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()