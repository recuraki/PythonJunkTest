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
        def do2(l, r, depth):
            if l == r:
                res[l] = depth
                return
            if l > r:
                return
            #print("do2",l, r ,depth)
            maxVal = max(dat[l : r+1])
            maxInd = None
            for i in range(l, r + 1):
                if maxVal == dat[i]:
                    maxInd = i
                    break
            res[maxInd] = depth

            do2(l, maxInd - 1, depth + 1)
            do2(maxInd + 1, r, depth + 1)

        n = int(input())
        dat = list(map(int, input().split()))
        res = [-1] * n
        do2(0, n-1, 0)
        print(" ".join(list(map(str, res))))

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
        input = """3
5
3 5 2 1 4
1
1
4
4 3 1 2"""
        output = """1 0 2 3 1
0
0 1 3 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()