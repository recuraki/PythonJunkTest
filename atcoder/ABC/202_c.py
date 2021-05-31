import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))
    datc = list(map(int, input().split()))
    for i in range(n):
        x = datc[i] - 1
        datc[i] = datb[x]
    #print(data)
    #print(datc)
    import collections
    d = collections.defaultdict(int)
    for x in datc:
        d[x] += 1
    res = 0
    for x in data:
        res += d[x]
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
        input = """3
1 2 2
3 1 2
2 3 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1 1 1
1 1 1 1
1 2 3 4"""
        output = """16"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
2 3 3
1 3 3
1 1 1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()