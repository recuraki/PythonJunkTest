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
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))
        dat = list(set(dat))
        dat.sort()
        #print(dat)
        l = len(dat)
        c = 1
        res = -1
        if x < dat[0]:
            print(x)
        else:
            for i in range(l):
                d = dat[i] - c
                if x >= d:
                    x -= d
                else:
                    break
                c = dat[i]
            #print(res, c, x, i)
            if res == -1:
                res = c + x
            res += i
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
        input = """6
1 3
102
6 2
3 1 1 5 7 10
1 100
100
11 1
1 1 1 1 1 1 1 1 1 1 1
1 1
1
4 57
80 60 40 20"""
        output = """3
5
101
2
2
60"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()