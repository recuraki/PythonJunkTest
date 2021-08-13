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

    INF = 1 << 63
    def do():
        n, q = map(int, input().split())
        s = input()
        dat = []
        for x in s:
            if x == "a": dat.append(0)
            elif x == "b": dat.append(1)
            elif x == "c": dat.append(2)
        buf = []
        for _ in range(q):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            buf.append( (a,b) )
        candidate = []
        candidate.append([0, 1, 2])
        candidate.append([0, 2, 1])
        candidate.append([1, 0, 2])
        candidate.append([1, 2, 0])
        candidate.append([2, 0, 1])
        candidate.append([2, 1, 0])
        cost = [[0] for _ in range(6)]
        #print(dat)
        for i in range(n):
            val = dat[i]
            ind = i % 3
            for k in range(len(candidate)):
                if val != candidate[k][ind]:
                    cost[k].append(cost[k][-1] + 1)
                else:
                    cost[k].append(cost[k][-1])
        for a, b in buf:
            #print("query", a, b)
            res = INF
            for k in range(len(candidate)):
                res = min(res, cost[k][b+1] - cost[k][a])
                #print(" ", k, cost[k][b+1] - cost[k][a])
            print(res)

        #print("orig", dat)
        #for x in candidate: print(x)
        #for x in cost: print(x)
        #print(cost)

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
        input = """5 4
baacb
1 3
1 5
4 5
2 3"""
        output = """1
2
0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()