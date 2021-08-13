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

    INF = 1 << 63
    def do():
        import random
        def is_prime(q, k=50):
            q = abs(q)
            if q == 2: return True
            if q < 2 or q & 1 == 0: return False

            d = (q - 1) >> 1
            while d & 1 == 0:
                d >>= 1

            for i in range(k):
                a = random.randint(1, q - 1)
                t = d
                y = pow(a, t, q)
                while t != q - 1 and y != 1 and y != q - 1:
                    y = pow(y, 2, q)
                    t <<= 1
                if y != q - 1 and t & 1 == 0:
                    return False
            return True

        def factorization(n):
            arr = []
            temp = n
            for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
                if temp % i == 0:
                    cnt = 0
                    while temp % i == 0:
                        cnt += 1
                        temp //= i
                    arr.append([i, cnt])
            if temp != 1:
                arr.append([temp, 1])
            if arr == []:
                arr.append([n, 1])
            return arr


        n = int(input())
        dat = list(map(int, input().split()))
        nokori = []
        for x in dat:
            if x > 3 and is_prime(x): continue
            nokori.append(x)
        if len(nokori) == 0:
            print(1)
            return

        for x in nokori:
            l = factorization(x)
            for prime, _ in l:




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
5
1 5 2 4 6
4
8 2 5 10
2
1000 2000
8
465 55 3 54 234 12 45 78"""
        output = """3
3
2
6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()