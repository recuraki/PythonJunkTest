import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,m = map(int, input().split())
    dat = list(map(int, input().split()))
    total = sum(dat)
    if n < m: # color is too much
        print(-1)
    elif total < n: # cannot fill
        print(-1)
    else:
        #print("")
        res = []
        res.append(1)
        l = 1
        r = l + dat[0] - 1
        total -= dat[0]
        if r > n:
            print(-1)
        else:
            for i in range(1, m):
                #print("loopi", i, " l=",l, " r=", r, "total=", total)
                canshi = r - l
                goal = n - r
                doshi = min(canshi, total - goal)
                #print("canshi:", canshi, "goal", goal, "doshi", doshi)
                l = r - doshi + 1
                r = l + dat[i] - 1
                total -= dat[i]
                res.append(l)
            if r > n:
                print(-1)
            else:
                print(" ".join(list(map(str, res))))

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
        input = """5 3
3 2 2"""
        output = """1 2 4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_1")
        input = """10 10
1 1 1 1 1 1 1 1 2 1"""
        output = """1 3 5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()