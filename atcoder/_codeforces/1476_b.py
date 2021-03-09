import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, k = map(int, input().split())
        dat = list(map(lambda x: int(x), input().split()))
        prev = dat[0]
        print(dat)
        res = 0
        for i in range(1, n):
            curval  = dat[i] * 100
            prevval = prev * k
            print(curval, prevval, curval/prevval)






    q = int(input())
    for _ in range(q):
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
        input = """2
4 1
20100 1 202 202
3 100
1 1 1"""
        output = """99
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()