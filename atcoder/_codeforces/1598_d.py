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


    """
    引き算で考える
    トータルの点をn個として

    全ての3点を選ぶ組み合わせは nC3

    ある2点が違反する全ての数は各x,yに対して、
     (x count - 1 + y count - 1個) * (n-2)
     前半 = 今の点と重なる個数 (sameな場所から自分を抜いているので正しい)
     後半
    """

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        def nCr(n, r):
            import math
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
        n = int(input())
        #print()
        dat = []
        datx = []
        daty = []
        from collections import Counter
        for i in range(n):
            x, y = map(int, input().split())
            datx.append(x)
            daty.append(y)
        # all choose case
        res = nCr(n, 3)
        countx = Counter(datx)
        county = Counter(daty)
        dup3 = 0
        for i in range(n):
            x, y = datx[i], daty[i]
            samelineNodes = countx[x] - 1 + county[y] - 1 # With out me
            dup3 += nCr(countx[x] - 1, 2)
            dup3 += nCr(county[y] - 1, 2)
            #res -= (countx[x]-1) * (county[y]-1)
        print(dup3, res - dup3 // 3)
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
        input = """1
3
3 1
3 2
3 3"""
        output = """3
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()