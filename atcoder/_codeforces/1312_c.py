import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    q = int(input())
    for _ in range(q):
        import math
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        if dat[0] == 0:
            print("YES")
            continue
        ma = math.ceil(math.log(dat[0], k))
        for i in range(ma, -1, -1):
            dat.sort()
            for j in range(n):
                if dat[j] == 0:
                    continue
                if dat[j] >= (k ** i):
                    dat[j] -= (k ** i)
                    break
        if sum(dat) == 0:
            print("YES")
        else:
            print("NO")




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
4 100
0 0 0 0
1 2
1
3 4
1 4 1
3 2
0 1 3
3 9
0 59049 810"""
        output = """YES
YES
NO
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()