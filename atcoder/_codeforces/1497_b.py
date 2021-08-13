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
        n, m = map(int, input().split())
        dat = list(map(lambda x: int(x) % m, input().split()))
        #print(dat)
        buf = [0] * m
        for x in dat:
            buf[x] += 1
        #print(buf)
        res = 0
        if buf[0] > 0: # 0以上なら1個
            res += 1
        if m % 2 == 0: # mが偶数なら
            for i in range(1, (m)//2):
                l, r = buf[i], buf[m-i]
                l, r = min(l,r), max(l,r)
                if l == 0 and r == 0:
                    continue
                res += 1
                if l == r:
                    continue
                if (l+1) == r:
                    continue
                res += r - (l+1)
            center = buf[m//2]
            if center != 0:
                res += 1
        else:
            for i in range(1, (m+1)//2):
                l, r = buf[i], buf[m-i]
                l, r = min(l,r), max(l,r)
                if l == 0 and r == 0:
                    continue
                res += 1
                if l == r:
                    continue
                if (l+1) == r:
                    continue
                res += r - (l+1)
        print(res)



    q = int(input())
    for _ in range(q):
        do()
    # do()



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
6 4
2 2 8 6 9 4
10 8
1 1 1 5 2 4 4 8 6 7
1 1
666
2 2
2 4"""
        output = """3
6
1
1"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
3 1
1 1 2 3 4
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()