import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        a = dat[0] + dat[1]
        for i in range(2, n):
            if dat[i] >= a:
                print(1,2, i+1)
                return
        print(-1)


    q = int(input())
    import bisect
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
        input = """3
7
4 6 11 11 15 18 20
4
10 10 10 11
3
1 1 1000000000"""
        output = """2 3 6
-1
1 2 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()