import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        class BinaryIndexTreeSum:
            #
            # BE
            #
            def __init__(self, n):  # [1-n]を作る
                self.size = n
                self.tree = [0] * (n + 1)

            def sum(self, i):  # [1-i]のsumを取る(閉区間なことに注意)
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

            def add(self, i, x):
                assert i > 0  # bitなので1-indexed
                while i <= self.size:
                    self.tree[i] += x
                    i += i & -i

            def rangesumCloseOpen(self, i, j):  # [i, j) の和 Close-Open
                assert i > 0  # bitなので1-indexed
                assert i <= j
                return self.sum(j - 1) - self.sum(i - 1)

        n, q, x = map(int, input().split())
        dat = list(map(int, input().split()))
        tmp = dat + dat
        bit = BinaryIndexTreeSum(2*n)
        for i in range(n*2):
            bit.add(i+1, tmp[i])
        qs = []
        buf = [] # (あと何個必要, 次の位置)
        basecount = x // sum(dat) # xを埋めるために必要な週のかず。のこり = x * basecount
        basenokori = x - (sum(dat) * basecount) # これが残り
        for _ in range(q): qs.append(int(input()))
        base = 0 # ここまでで積み上げた数
        print("nokori", basenokori)
        for i in range(n):
            # [ok, ng) for max value
            # (ng, ok] for min value
            # CATION: ok is result  (NOT mid)
            def func(mid):
                return bit.rangesumCloseOpen(i+1, mid+1+1) <= basenokori
            ok = i
            ng = 2*n+1
            while (abs(ok - ng) > 1):
                mid = (ok + ng) // 2;
                if (func(mid)):
                    ok = mid
                else:
                    ng = mid
            print("from", i , "to", (ok+1) % n, bit.rangesumCloseOpen(i+1, ok+1+1))
            j = ok
            base += dat[i]
            buf.append( (j - i + 1) )
        print(buf)
        tmp = []
        visited = [-1] * n
        cur = 0
        route = []
        turn = 0
        cnt = [0] * n
        for i in range(n*10):
            if visited[cur] == -1:
                visited[cur] = turn
                #print("tu", cur, turn, parent)
            cnt[cur] += 1
            nxt = cur + buf[cur]
            nxt %= n
            turn += 1
            cur = nxt
        tmp = []
        for i in range(n):
            tmp.append( (-cnt[i], visited[i], i) )
        tmp.sort()
        print(tmp)
        loopstart = tmp[0][2]
        route = []
        cur = 0
        loopstartind = -1
        loopstartcnt = 0
        if loopstart == cur:
            loopstartind = 0
        print(buf, cur)
        turn = 0
        while True:
            print("turn", turn, cur)
            if cur == loopstart: loopstartcnt += 1
            if loopstartcnt == 2: break
            if cur == loopstart and loopstartind == -1:
                loopstartind = turn
            route.append(buf[cur])
            nxt = cur + buf[cur]
            nxt %= n
            cur = nxt
            turn += 1
        print("r", route)
        print("sind", loopstartind)
        rr = route[loopstartind:]
        for x in qs:
            x -= 1
            if x < len(route):
                print(route[x])
            else:
                x -= loopstartind
                print(rr[x% len(rr)])



    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """3 2 5
3 4 1
1
2"""
        output = """2
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 5 20
5 8 5 9 8 7 4 4 8 2
1
1000
1000000
1000000000
1000000000000"""
        output = """4
5
5
5
5"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_2")
        input = """3 1 1
1 1 1
1"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()