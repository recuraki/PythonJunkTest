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


"""

odd, odd
min, maxにして、maxこの短冊を作る
min側は、min //2
3 -> 1
5 -> 2
で、min//2 * max

なるべく3にきる。
--
1のとき、
2 -> 1 = 2
3 -> 1 =3
4 -> 2 =2+2
5 -> 2 =3+2
6 -> 2 = 3+3
7 -> 3 = 3,2,2で
8 -> 3 = 3,3,2で
9 -> 3 = 3,3,3
"""
def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def f(n, m): # nを切っていく
        if m == 1:
            can = math.ceil(n / 3)  # can make 3
            ans = can * m
            return ans

        if n % 3 == 0:
            can = (n // 3) # can make 3
            ans = can * m
            return ans
        if n % 3 == 1:
            can = (n // 3) # can make 3
            ans = can * m
            ans += math.ceil(m / 3)
            return ans
        if n % 3 == 2:
            can = (n // 3) # can make 3
            ans = can * m
            ans += math.ceil(m / 3) * 2
            return ans



    def do():
        n, m = map(int, input().split())
        if n == 1 or m == 1: # 1 is special
            print(f(max(n, m), 1))
            return
        print(min(f(n,m ), f(m, n)))

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
1 3
2 2
2 5
3 5"""
        output = """1
2
4
5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1 2
1 3
1 4
1 5
1 6
1 7
5 6
1 12
2 12
3 12"""
        output = """1
1
2
2
2
3
10
4
8
12"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()