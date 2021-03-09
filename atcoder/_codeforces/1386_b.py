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
        n = int(input())
        tx, ty = 0, 0
        dat = []
        candidates = []
        for i in range(n):
            x,y = map(int, input().split())
            dat.append( (x,y) )

        if n % 2 == 1:
            print(1)
            return
        dat.sort(key=lambda x: x[0])
        x1, y1 = dat[n // 2 - 1]
        x2, y2 = dat[n // 2]
        finalres = (x2 - x1 + 1)

        dat.sort(key=lambda x: x[1])
        x1, y1 = dat[n // 2 - 1]
        x2, y2 = dat[n // 2]
        finalres *= (y2 - y1 + 1)
        print(finalres)

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
        input = """6
3
0 0
2 0
1 2
4
1 0
0 2
2 3
3 1
4
0 0
0 1
1 0
1 1
2
0 0
1 1
2
0 0
2 0
2
0 0
0 0"""
        output = """1
4
4
4
3
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
2
1 1
1 2"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()