import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline

    
    from pprint import pprint
    import itertools
    from bisect import bisect_left, bisect_right
    def do():
        n = int(input())
        from copy import deepcopy
        dat = [0] + list(map(int, input().split()))
        buf = [0] * (n+1)
        fres = 0
        for i in range(n, 0, -1):
            nextNode = i + dat[i]
            buf[i] = dat[i]
            if nextNode < (n + 1):
                buf[i] += buf[nextNode]
            fres = max(fres, buf[i])
            fres = max(fres, dat[i])
        print(fres)



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
        input = """4
5
7 3 1 2 3
3
2 1 4
6
2 1000 2 3 995 1
5
1 1 1 1 1"""
        output = """7
6
1000
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()