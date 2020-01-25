
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for q in range(q):
        qq = int(input())
        dat = []
        s = ""
        for _ in range(qq):
            x, y = map(int, input().split())
            dat.append([x, y])
            dat.sort(key=lambda a: a[0] + a[1])
        #print(dat)
        cx, cy = 0, 0
        f = True
        for i in range(qq):
            x, y = dat[i][0], dat[i][1]
            if x < cx or y < cy:
                f = False
                break
            s += "R" * (x - cx)
            s += "U" * (y - cy)
            cx,cy = dat[i][0], dat[i][1]
        if f:
            print("YES")
            print(s)
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
        input = """3
5
1 3
1 2
3 3
5 5
4 3
2
1 0
0 1
1
4 3"""
        output = """YES
RUUURRRRUU
NO
YES
RRRRUUU"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()