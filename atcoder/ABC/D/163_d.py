import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(a, d, n, l):
        return (n*(a+l) // 2)

    n, k = map(int, input().split())
    maxnum = n + 1
    res = 0
    mod = 10**9 + 7

    for i in range(k, n+2):
        #print("---")
        #print(i)
        l = do(0      , 1, i, i - 1)
        #print((0      , 1, i, i - 1))

        r = do(n+1 - i, 1, i,     n)
        #print((n+1 - i, 1, i,     n))

        #print(i, l, r, r-l+1)
        res += r-l+1
        res %= mod
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
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """200000 200001"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """141421 35623"""
        output = """220280457"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()