import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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

        # just wrapper
        def addValue(self, ind, value):
            nodeId = (self.lenTreeLeaf - 1) + ind
            self.dat[nodeId] += value
            self.setValue(ind, self.dat[nodeId])

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

        def findNthValueSub(self, x, nodeId):
            """
            [2, 3, 5, 7] = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
            とマッピングされているセグメント木においてx番目に小さい値を得るための関数
            """
            if self.dat[nodeId] < x:  # このノードが要求されているよりも小さい値しか持たないとき
                return (None, x - self.dat[nodeId])
            if nodeId >= self.lenTreeLeaf - 1:  # nodeIfがノードのときは
                return (True, nodeId - (self.lenTreeLeaf - 1))  # そのindex番号を返す
            resLeft = self.findNthValueSub(x, 2 * nodeId + 1)  # 左側の探索を行う
            if resLeft[0] != None:  # もし、値が入っているならそれを返す
                return (True, resLeft[1])
            resRight = self.findNthValueSub(resLeft[1], 2 * nodeId + 2)  # 右側の探索を行う
            return resRight

        def findNthValue(self, x):
            return self.findNthValueSub(x, 0)[1]

    class segmentTreeMin(segmentTree):
        def __init__(self):
            self.func = lambda x, y: min(x, y)
            self.funcPropagateToChild = lambda parentValue: parentValue
            self.funcRangePropagetToParent = lambda currentValue: currentValue
            self.initValue = 2 * 10 ** 9

    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        INF = 10 ** 18
        n, m = map(int, input().split())
        dat = list(map(int, input().split()))
        l = [0] * 1500100
        for i in range(1500100):
            l[i] = i
        import collections
        d = collections.defaultdict(int)
        st = segmentTreeMin()
        # [0,1,2,3,4....]というセグ木を構築
        for i in range(m):
            x = dat[i]
            l[x] = INF
            d[x] += 1
        st.load(l)
        finalres = st.query(0, 1500100)
        for i in range(n - m):
            # 入る値と抜ける値を得る
            outvalue = dat[i]
            invalue = dat[m+i]
            d[outvalue] -= 1
            # 抜けた値がなくなったならRMQで選ばれるようにする(値をindexに戻す)
            if d[outvalue] == 0:
                st.setValue(outvalue, outvalue)
            d[invalue] += 1
            st.setValue(invalue, INF) # その値が入った場合、選ばれてほしくないのでINFにする
            # で、この瞬間のMinの値(=index)を得る
            finalres = min(finalres, st.query(0, 1500100))
        print(finalres)
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
        input = """3 2
0 0 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 2
0 1 0"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7 3
0 0 1 2 0 1 0"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()