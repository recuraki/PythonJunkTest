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
    # https://tjkendev.github.io/procon-library/python/range_query/rsq_ruq_segment_tree_lp.html
    class segmentTree():
        initValue = 0
        dat = []
        lenTreeLeaf = -1
        depthTreeList = 0
        lenOriginalList = -1
        func = None
        funcPropagateToChild = None
        lazy = None
        N = -1

        def load(self, l):
            self.N = len(l)
            self.lenOriginalList = self.N  # original nodes
            self.depthTreeList = (self.N - 1).bit_length()  # Level of Tree
            self.lenTreeLeaf = 2 ** self.depthTreeList  # leaf of node, len 5 -> 2^3 = 8
            self.dat = [self.initValue] * (self.lenTreeLeaf * 2)
            self.lazy = [self.initValue] * (self.lenTreeLeaf * 2)  # lazy propagete buffer

            # Load Function
            for i in range(len(l)):
                self.dat[self.lenTreeLeaf - 1 + i] = l[i]
            self.build()

        def build(self):
            for i in range(self.lenTreeLeaf - 2, -1, -1):
                self.dat[i] = self.func(self.dat[2 * i + 1], self.dat[2 * i + 2])
                # print("build: node", i, "child is ", self.dat[2 * i + 1], self.dat[2 * i + 2] ,"then I am ", self.dat[i])

        # just wrapper, get node value and op and put it
        def addValue(self, ind, value):
            nodeId = (self.lenTreeLeaf - 1) + ind
            self.dat[nodeId] += value
            self.setValue(ind, self.dat[nodeId])

        # set value to node, recalc parents NODEs
        def setValue(self, ind, value):
            nodeId = (self.lenTreeLeaf - 1) + ind
            self.dat[nodeId] = value
            while nodeId != 0:
                nodeId = (nodeId - 1) // 2
                self.dat[nodeId] = self.func(self.dat[nodeId * 2 + 1], self.dat[nodeId * 2 + 2])

        def nodelistFromLR(self, l, r, withchild=False):
            L = (l + self.lenTreeLeaf) >> 1
            R = (r + self.lenTreeLeaf) >> 1

            lc = 0 if l & 1 else (L & -L).bit_length()
            rc = 0 if r & 1 else (R & -R).bit_length()

            res = []
            for i in range(self.depthTreeList + (1 if withchild else 0)):
                if rc <= i:
                    res.append(R - 1)
                if L < R and lc <= i:
                    res.append(L - 1)
                L = L >> 1
                R = R >> 1
            return res

        def rangeAdd(self, l, r, x):
            plist = self.nodelistFromLR(l, r)
            self.propagete(plist)

            L = self.lenTreeLeaf + l
            R = self.lenTreeLeaf + r
            # print(">>before", self.lazy, L, R)
            value = x
            while L < R:
                if R & 1:
                    R -= 1
                    # print(">>> updateR", R-1, value)
                    self.lazy[R - 1] = self.func(self.lazy[R - 1], value)
                    self.dat[R - 1] = self.func(self.dat[R - 1], value)
                if L & 1:
                    # print(">>> updateL", L-1, value)
                    self.lazy[L - 1] = self.func(self.lazy[L - 1], value)
                    self.dat[L - 1] = self.func(self.dat[L - 1], value)
                    L += 1
                L = L >> 1
                R = R >> 1
                value = self.funcRangePropagetToParent(value)
                # print(">>>END cur", L, R)
            # print(">>after", self.lazy)

            for node in plist:
                self.dat[node] = self.func(self.dat[2 * node + 1], self.dat[2 * node + 2])

        def propagete(self, plist):
            for nodeId in plist[::-1]:
                " this function will be call from top to down"
                # print("propagete", nodeId, "curlazyval =", self.lazy[nodeId])
                if self.lazy[nodeId] == self.initValue:
                    continue
                if nodeId < (self.lenTreeLeaf - 1):  # if this node has childs
                    propageteValue = self.funcPropagateToChild(self.lazy[nodeId])
                    # print(" > propagate to node")
                    self.lazy[2 * nodeId + 1] = self.func(self.lazy[2 * nodeId + 1], propageteValue)
                    self.lazy[2 * nodeId + 2] = self.func(self.lazy[2 * nodeId + 2], propageteValue)
                    self.dat[2 * nodeId + 1] = self.func(self.dat[2 * nodeId + 1], propageteValue)
                    self.dat[2 * nodeId + 2] = self.func(self.dat[2 * nodeId + 2], propageteValue)
                else:
                    # print(" > do nothing")
                    pass
                # Feedback to myself value
                # self.dat[nodeId] = self.func(self.dat[nodeId], self.lazy[nodeId])
                self.lazy[nodeId] = self.initValue

        def query(self, l, r):
            # print("query()", l, r)
            plist = self.nodelistFromLR(l, r)
            self.propagete(plist)

            L = self.lenTreeLeaf + l
            R = self.lenTreeLeaf + r

            view = []
            res = self.initValue
            while L < R:
                if R & 1:
                    R -= 1
                    # print(">>>checkR", R-1, "value", self.dat[R-1])
                    res = self.func(res, self.dat[R - 1])
                if L & 1:
                    # print(">>>checkL", L-1, "value", self.dat[L-1])
                    res = self.func(res, self.dat[L - 1])
                    L += 1
                L = L >> 1
                R = R >> 1
            return res

    class segmentTreeMin(segmentTree):
        def __init__(self):
            self.func = lambda x, y: min(x, y)
            self.funcPropagateToChild = lambda parentValue: parentValue
            self.funcRangePropagetToParent = lambda currentValue: currentValue
            self.initValue = 2 * 10 ** 9

    import sys
    #input = sys.stdin.readline



    from pprint import pprint

    def do():
        n = int(input())
        dat = sorted(list(map(int, input().split())))
        buf = []
        l, res = 0, 1
        for i in range(n-1):
            buf.append( abs(dat[i] - dat[i+1]) )
        #print(buf)
        RangeMinQuery = segmentTreeMin()
        RangeMinQuery.load(buf)
        for r in range(1, n):
            mm = dat[r] # max is R
            while RangeMinQuery.query(l, r) < mm:
                l += 1
                if l == r: break
            if l == r: break
            res = max(res, (r-l+1))
        print(res)

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
        input = """6
4
-1 -2 0 0
7
-3 4 -2 0 -4 6 1
5
0 5 -3 2 -5
3
2 3 1
4
-3 0 2 0
6
-3 -2 -1 1 1 1"""
        output = """4
5
4
1
3
4"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1
8
-100 -99 -98 -97 -10 -5 0 2 4 5"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()