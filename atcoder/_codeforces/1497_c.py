import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)

    def llcm(l):
        res = 1
        for x in l:
            res = lcm(res, x)
        return res, sum(l)

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do3(n, k):
        if n%2 == 0:
            x = n//2
            if x%2 == 0:
                a = x
                b = x//2
                c = x//2
                return(a,b,c)
            else:
                a = 2
                b = x-1
                c = x-1
                return(a,b,c)
        else:
            a = 1
            b = (n) // 2
            c = (n) // 2
        return (a, b, c)

    def do():
        n, k = map(int, input().split())
        if k == 3:
            a,b,c = do3(n, k)
            print(a,b,c)
            return

        res = [1] * k
        n -= k
        n += 3
        a,b,c = do3(n, 3)
        #print(res)
        res[0] = a
        res[1] = b
        res[2] = c
        #print(res)
        #print(llcm(res))
        print(" ".join(list(map(str, res))))
        return


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
        input = """5
3 3
8 3
14 3
6 4
9 5"""
        output = """1 1 1
4 2 2
2 6 6
1 2 2 1
1 3 3 1 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
8 5
"""
        output = """"""
        #self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()