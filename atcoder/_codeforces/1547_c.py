import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():





    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        _ = input()
        k, n, m = map(int, input().split())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        #print("-----------", k,n,m)
        a = b = 0
        res = []
        while True:
            if a >= n and b >= m:
                break
            #print("curk=", k)
            if a < n:
                if data[a] == 0:
                    k += 1
                    res.append(0)
                    a += 1
                    continue
                if data[a] <= k:
                    res.append(data[a])
                    a += 1
                    continue

            if b < m:
                if datb[b] == 0:
                    k += 1
                    res.append(0)
                    b += 1
                    continue
                if datb[b] <= k:
                    res.append(datb[b])
                    b += 1
                    continue

            print(-1)
            return

        print(" ".join(list(map(str, res))))

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

3 2 2
2 0
0 5

4 3 2
2 0 5
0 6

0 2 2
1 0
2 3

5 4 4
6 0 8 0
0 7 0 9

5 4 1
8 7 8 0
0"""
        output = """2 0 0 5 
0 2 0 6 5 
-1
0 6 0 7 0 8 0 9
-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()