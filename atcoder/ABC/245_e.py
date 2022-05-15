
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

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i): # 1-origin, [i,x]
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    def do():
        n, m = map(int, input().split())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        datc = list(map(int, input().split()))
        datd = list(map(int, input().split()))

        l = []
        for x in datb:l.append(x)
        for x in datd:l.append(x)
        zatsu = sorted(set(l))
        zatsuTable = dict()
        zatsuTableRev = dict()
        for ind, value in enumerate(zatsu):
            zatsuTable[value] = ind
            zatsuTableRev[ind] = value
        newl = []

        choco = []
        box = []
        for i in range(n):
            a,b = data[i], datb[i]
            choco.append( (a,zatsuTable[b] +1) ) # bitするので+1
        for i in range(m):
            c, d = datc[i], datd[i]
            box.append( (c, zatsuTable[d] +1) ) # bitするので+1
        bit = Bit(len(zatsuTable) + 1)
        bitmax = len(zatsuTable) + 1
        #print(bitmax, zatsuTable)
        choco.sort(reverse=True)
        box.sort(reverse=True)
        from collections import deque
        choco = deque(choco)
        box = deque(box)
        #print(choco)
        #print(box)
        while len(choco) > 0:
            a, b = choco.popleft()
            #print("try ", a,zatsuTableRev[b-1])
            # 使えるboxを出してくる
            while len(box) > 0:
                c, d = box[0]
                if c >= a: # 使える
                    c, d = box.popleft()
                    #print("can use box", c, zatsuTableRev[d-1])
                    bit.add(d, 1)
                else: # 使えない場合
                    break # 取り出さずにbreak
            canuse = bit.sum(bitmax) - bit.sum(b - 1) # bよりも大きいものが1つでもあるか？
            if canuse == 0: # もしないならダメ
                print("No")
                return
            # 何を減らすか調べる bin search

            # [ok, ng) for max value
            # (ng, ok] for min value
            # CATION: ok is result  (NOT mid)
            def func(mid):
                canuse = bit.sum(mid)
                canuse -= bit.sum(b - 1)
                if canuse > 0: return True
                return False
            ok = bitmax
            ng = b - 1
            while (abs(ok - ng) > 1):
                mid = (ok + ng) // 2;
                if(func(mid)) :ok = mid;
                else : ng = mid;
            #print("use", ok, bitmax, b-1)
            bit.add(ok, -1)
        print("Yes")






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
        input = """2 3
2 4
3 2
8 1 5
2 10 5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
1 1
2 2
100 1
100 1"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1
10
100
100
10"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1 1
10
100
10
100"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()