import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        q = int(input())
        for _ in range(q):
            x,y = map(int, input().split())
            a,b,c,d,e,f = list(map(int, input().split()))
            if x < 0 and y < 0:
                x=-x
                y=-y
                a,b,c,d,e,f =d,e,f,a,b,c

            res = 10 ** 20

            def calc(x, y):
                # tate first
                tatecost = 10** 20
                if x == 0:
                    tatecost = 0
                elif x > 0:
                    tatecost = min(tatecost, x * f)
                    tatecost = min(tatecost, x * (a+e))
                elif x < 0:
                    tatecost = min(tatecost, -x * c)
                    tatecost = min(tatecost, -x * (b+d))
                # right cost
                yokocost = 10** 20
                if y == 0:
                    yokocost = 0
                elif y > 0:
                    yokocost = min(yokocost, y * b)
                    yokocost = min(yokocost, y * (a+c))
                elif y < 0:
                    yokocost = min(yokocost, y * e)
                    yokocost = min(yokocost, y * (f+d))
                #print("cost", tatecost, yokocost)
                #print(a,b,c,d,e,f)
                #print("target", x, y)
                res = tatecost + yokocost
                return res
            res = calc(x, y)

            if x > 0:
                res = min(res, x * a + calc(0, y - x))
            elif x < 0:
                res = min(res, -x * c + calc(0, y))

            if y > 0:
                res = min(res, y * a + calc(x-y, 0))

            print(res)
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
        input = """2
-3 1
1 3 5 7 9 11
1000000000 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """18
1000000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()