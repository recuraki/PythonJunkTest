import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    lines = []
    line_dat = []

    for i in range(n + 1):
        lines.append((i, 0))

    for i in range(n - 1):
        a, b = map(int, input().split())
        lines[a] = (a, lines[a][1] + 1)
        lines[b] = (b, lines[b][1] + 1)
        line_dat.append((a,b))

    lines.sort(key=lambda x: -x[1])
    dat_c = list(map(int, input().split()))
    dat_c.sort(reverse=True)

    cans = []
    dat_cans = []
    for i in range(100001):
        cans.append((i, 0))
    for i in range(len(dat_c)):
        cans[dat_c[i]] = (cans[dat_c[i]][0], cans[dat_c[i]][1] + 1)

    for i in range(100001):
        if cans[i][1] != 0:
            dat_cans.append((i, cans[i][1]))

    res = [-1] * (n + 1)

    for i in range(n):
        res[lines[i][0]] = dat_c[i]

    c = 0
    orig = []

    dat_cans.sort(key = lambda x: -x[0])
    print("")
    print("dat_cans")
    print(dat_cans)
    print("lines")
    print(lines)
    print("line_dat")
    print(line_dat)
    print("dat_c")
    print(dat_c)
    for i in range(len(dat_cans)):
        t = []
        for j in range(dat_cans[i][1]):
            t.append( lines[c][0] )
            c=c+1
        orig.append(t)

    print("orig")
    print(orig)

    import itertools
    sug = list(itertools.product(*orig))
    print(sug)


    # コスト計算
    lines.remove((0, 0))
    cost = 0
    for i in range(len(line_dat)):
        cost += min( res[line_dat[i][0]], res[line_dat[i][1]])

    res = res[1:]
    print(cost)
    print(" ".join(list(map(lambda x:str(x), res))))



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
        logging.info("test_input_1")
        input = """5
1 2
2 3
3 4
4 5
1 2 3 4 5"""
        output = """10
1 2 3 4 5"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """5
1 2
1 3
1 4
1 5
3141 59 26 53 59"""
        output = """197
59 26 3141 59 53"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()