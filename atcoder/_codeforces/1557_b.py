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
        n, k = map(int, input().split())
        l = list(map(int, input().split()))
        zatsu = sorted(set(l))
        zatsuTable = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
        dat = []
        for x in l:
            dat.append(zatsuTable[x])
        res = []
        kk = 0
        #print("dat", dat)
        #tmp = [dat[0]]
        for i in range(1, n):
            #print(i, dat[i], dat[i-1])
            if dat[i] == (dat[i-1] + 1):
                #tmp.append(dat[i])
                continue
            else:
                kk += 1
                #res.append(tmp)
                #tmp = [[dat[i]]]
        #res.append(tmp)
        kk += 1
        #print(k, kk)
        if kk <= k:
            print("Yes")
        else:
            print("No")
        #print("res", res)


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
5 4
6 3 4 2 1
4 2
1 -4 0 -2
5 1
1 2 3 4 5
1 1
1"""
        output = """Yes
No
Yes
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()