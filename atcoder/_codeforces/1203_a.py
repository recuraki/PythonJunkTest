
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for qq in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        can1 = True
        can2 = True
        cur = dat[0]
        for i in range(n):
            if dat[i] == 1:
                p1 = i
                break
        #print("dat")
        #print(dat)
        #print(p1)
        # clockか確認
        lorig = list(range(1, n+1))
        t = n - p1
        col = lorig[t:] + lorig[:t]
        #print(col)
        for i in range(n):
            if dat[i] != col[i]:
                can1 = False


        for i in range(n):
            if dat[i] == n:
                p1 = i
                break
        #print(p1)
        lorig = list(range(n, 0, -1))
        t = n - p1
        col = lorig[t:] + lorig[:t]
        #print(col)
        for i in range(n):
            if dat[i] != col[i]:
                can2 = False

        print("YES" if can1 or can2 else "NO")
class TestClass(unittest.TestCase):
    maxDiff = 100000
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
4
1 2 3 4
3
1 3 2
5
1 2 3 5 4
1
1
5
3 2 1 5 4"""
        output = """YES
YES
NO
YES
YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()