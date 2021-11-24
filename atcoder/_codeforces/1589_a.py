import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)

    def lcmList(l):
        x = 1
        for i in range(len(l)):
            x = lcm(x, l[i])
        return x

    """
    >>> gcdList([3])
    3
    >>> gcdList([3,6])
    3
    >>> gcdList([12, 18])
    6
    >>> gcdList([12, 18, 7])
    1"""

    def gcdList(l):
        x = 0
        for i in range(len(l)):
            x = math.gcd(x, l[i])
        return x

    import math
    INF = 1 << 63
    def do():
        a, b = map(int, input().split())
        oa, ob = a, b
        c = a + b
        com = lcmList([a,b,c])
        #print(a,b,c,com)
        a = com // a
        b = com // b
        c = com // c
        #print(a, b, c)
        x = a - c
        y = c - b
        x, y = y, x
        #print((x/oa) + (y/ob), (x+y) / (oa+ob))
        print(x,y)

    # n questions
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
1 1
2 3
3 5
6 9"""
        output = """-1 1
-4 9
-18 50
-4 9"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()