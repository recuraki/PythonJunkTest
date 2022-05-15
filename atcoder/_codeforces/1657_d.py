
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
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def prime_list_eratosthenes(n):
        import math
        if n == 1:
            return []
        if n == 2:
            return [2]
        prime = [2]
        limit = math.sqrt(n)
        data = [i + 1 for i in range(2, n, 2)]
        while True:
            p = data[0]
            if limit < p:
                return prime + data
            prime.append(p)
            data = [e for e in data if e % p != 0]

    def do():
        n, c = map(int, input().split())
        my = []
        ma = 10**6 + 10000
        primes = prime_list_eratosthenes(ma+10000)
        table = [0] * (ma + 10000)
        for _ in range(n):
            cost, dmg, hp = map(int, input().split())
            my.append( (cost, dmg, hp) )
            x = dmg * hp
            table[cost] = max(table[cost], x)
        #print(table[:20])
        for i in range(1, ma + 10):
            j = 0
            while i * primes[j] <= (ma + 10):
                nxt = i * primes[j]
                table[nxt] = max(table[nxt], table[i]*primes[j])
                j += 1

        cur = 0
        for i in range(0, ma+2):
            cur = max(table[i], cur)
            table[i] = cur

        teki = []
        m = int(input())
        #print(table[:20])
        from bisect import bisect_right
        ans = []
        for _ in range(m):
            dmg, hp = map(int, input().split())
            x = hp * dmg
            ind = bisect_right(table, x)
            if ind > c: ans.append(-1)
            else: ans.append(ind)
        print(*ans)


    # 1 time
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
        input = """3 10
3 4 6
5 5 5
10 3 4
3
8 3
5 4
10 15"""
        output = """5 3 -1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 15
14 10 3
9 2 2
10 4 3
7 3 5
4 3 1
6
11 2
1 1
4 7
2 1
1 14
3 3"""
        output = """14 4 14 4 7 7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 13
13 1 9
6 4 5
12 18 4
9 13 2
5 4 5
2
16 3
6 2"""
        output = """12 5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()