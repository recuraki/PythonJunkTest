import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class segmentTreeOR():
        initValue = 0
        dat = []
        lenTreeList = -1
        depthTreeList = 0
        lenOriginalList = -1

        def __init__(self):
            pass

        def load(self, l):
            # len(l)個よりも大きい2の二乗を得る
            self.lenOriginalList = len(l)
            self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
            self.depthTreeList = (len(l) - 1).bit_length()  # 木の段数(0 origin)
            self.dat = [self.initValue] * (self.lenTreeList * 2)
            # 値のロード
            for i in range(len(l)):
                self.dat[self.lenTreeList - 1 + i] = l[i]
            self.build()

        def build(self):
            for i in range(self.lenTreeList - 2, -1, -1):
                self.dat[i] = self.dat[2 * i + 1] | self.dat[2 * i + 2]

        def setValue(self, i, a):
            """
            set a to list[i]
            """
            # print("setValue: {0}, {1}".format(i, a))
            nodeId = (self.lenTreeList - 1) + i
            # print(" first nodeId: {0}".format(nodeId))
            self.dat[nodeId] = a
            while nodeId != 0:
                nodeId = (nodeId - 1) // 2
                # print(" next nodeId: {0}".format(nodeId))
                self.dat[nodeId] = self.dat[nodeId * 2 + 1] | self.dat[nodeId * 2 + 2]

        def querySub(self, a, b, nodeId, l, r):
            """
            [a,b) 区間の親クエリに対するノードnodeへ[l, r)の探索をデリゲート
            区間については、dataの添え字は0,1,2,3,4としたときに、
            [0,3)なら0,1,2の結果を返す
            """
            # print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
            if (r <= a or b <= l):
                return self.initValue
            if a <= l and r <= b:
                return self.dat[nodeId]
            resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
            resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
            return resLeft | resRight

        def query(self, a, b):
            return self.querySub(a, b, 0, 0, self.lenTreeList)

    ### ここまでライブラリ ###

    n = int(input())
    s = input()
    sl = list(s)
    sl = list(map(lambda x: ord(x) - ord("a"), sl))
    l = list(map(lambda x: 1 << x, sl))
    st = segmentTreeOR()
    st.load(l)

    q = int(input())
    for _ in range(q):
        ty, x, y = input().split()
        x = int(x)
        if ty == "1":
            nind = ord(y[0]) - ord("a") # 置き換える文字のaからの距離
            st.setValue(x-1, 1 << nind)
        elif ty == "2":
            x = int(x) - 1 # 1 origin -> 0 origin
            y = int(y)  # こっちは開区間なのでこのまま
            res = 0
            cnt = st.query(x, y)
            print(bin(cnt).count("1")) # popcount()
        else:
            print("error")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = 30000
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7"""
        output = """3
1
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()