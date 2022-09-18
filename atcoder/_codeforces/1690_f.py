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




    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        s = input()
        dat = list(map(int, input().split()))

        for i in range(len(dat)):
            dat[i] -= 1
        #print(dat)
        visited = [False] * n
        cycles = []
        for i in range(n):
            if visited[i]: continue
            route = []
            cur = i
            while visited[cur] is False:
                visited[cur] = True
                route.append((cur, dat[cur]))
                cur = dat[cur]
            cycles.append(sorted(route))
        #print(cycles)

        from copy import deepcopy
        buf = []
        for route in cycles:
            inits = []
            rr = []
            for cur, nxt in route:
                inits.append(s[cur])
                rr.append(nxt)
            zatsu = sorted(set(rr))
            zatsuTable = dict()
            zatsuTableRev = dict()
            for ind, value in enumerate(zatsu):
                zatsuTable[value] = ind
                zatsuTableRev[ind] = value
            newl = []
            for x in rr:
                newl.append(zatsuTable[x])
            route = newl

            cnt = 0
            curs = deepcopy(inits)
            #print("----", newl)
            #print("0", curs, )
            while True:
                cnt += 1
                news = []
                for i in rr:
                    news.append(curs[zatsuTable[i]])
                curs = news
                #print(cnt, curs)
                if inits == curs:
                    break
            buf.append(cnt)

        #print(buf)

        import math
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)

        def lcmList(l):
            x = 1
            for i in range(len(l)):
                x = lcm(x, l[i])
            return x

        print(lcmList(buf))



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
        input = """3
5
ababa
3 4 5 2 1
5
ababa
2 1 4 5 3
10
codeforces
8 6 1 7 5 2 9 3 10 4"""
        output = """1
6
12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()