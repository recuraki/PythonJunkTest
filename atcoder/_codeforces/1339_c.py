import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        import collections
        import math
        dat = list(map(int, input().split()))
        xm = min(dat)
        dat = list(map(lambda x: x - xm, dat))
        #print(dat)
        mv = dat[0]
        res = 0
        for i in range(1, n):
            #print("i:", i , "mv:",mv, "dat[i]", dat[i])
            di = mv - dat[i]
            if di <= 0:
                mv = dat[i]
                continue
            #print(di)
            x = math.floor(math.log(di, 2))
            x = x + 1
            #print(" diff:", di, "x:", x)
            res = max(res, x)
        #print("RESULT")
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
        input = """4
4
1 7 6 5
5
1 2 3 4 5
2
5 1
3
32 1 0"""
        output = """2
0
3
6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()