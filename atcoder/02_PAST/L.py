import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class segmentTreeMin():
        # とりあえず9 * 12桁
        inf = 2 ** 31 - 1
        dat = []
        lenTreeList = -1
        depthTreeList = 0

        def __init__(self):
            pass

        def load(self, l):
            # len(l)個よりも大きい2の二乗を得る
            self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
            self.depthTreeList = (len(l) - 1).bit_length()  # 木の段数(0 origin)
            self.dat = [self.inf] * (self.lenTreeList * 2)
            # 値のロード
            for i in range(len(l)):
                self.dat[self.lenTreeList - 1 + i] = l[i]
            self.build()

        def build(self):
            for i in range(self.lenTreeList - 2, -1, -1):
                self.dat[i] = min(self.dat[2 * i + 1], self.dat[2 * i + 2])

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
                self.dat[nodeId] = min(self.dat[nodeId * 2 + 1], self.dat[nodeId * 2 + 2])

        def querySub(self, a, b, nodeId, l, r):
            """
            [a,b) 区間の親クエリに対するノードnodeへ[l, r)の探索をデリゲート
            区間については、dataの添え字は0,1,2,3,4としたときに、
            [0,3)なら0,1,2の結果を返す
            """
            # print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
            if (r <= a or b <= l):
                return self.inf, nodeId
            if a <= l and r <= b:
                # print(" > return(have): {0}".format(self.dat[nodeId]))
                return self.dat[nodeId], nodeId
            resLeft,ind = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
            resRight,ind = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
            # print(" > return(lr): {0}".format(min(resLeft, resRight)))
            return min(resLeft, resRight), ind

        def query(self, a, b):
            return self.querySub(a, b, 0, 0, self.lenTreeList)

        def findLeftSub(self, x, a, b, nodeId, l, r):
            """
            [a,b) 区間の中からx【以下となる】最も左のindexを返す
            これは、nodeIdではなくて、元のlistのindexである
            """
            if (r <= a or b <= l):  # 範囲外の時 Noneを返す
                return None
            if self.dat[nodeId] > x:  # このノードの最小がx出ないときはこのノードにxは含まれないのでNoneを返す
                return None
            if nodeId >= self.lenTreeList - 1:  # nodeIfがノードのときは
                # (nodeIndex, 値) を返す
                print("hit: x={0} nodeId={1}".format(x, nodeId))
                return (nodeId - self.lenTreeList + 1, self.dat[nodeId])
            print("find more L: x={0} nodeId={1}".format(x, nodeId))
            # それ以外の時は子を掘る必要があり、左から掘る
            resLeft = self.findLeftSub(x, a, b, 2 * nodeId + 1, l, (l + r) // 2)
            # 左から値が帰ってくるときは最左を返したいわけであるからその値を返す
            if resLeft is not None:
                return resLeft
            # 左からNoneが帰ってきた場合は右側を掘る
            print("find more R: x={0} nodeId={1}".format(x, nodeId))
            resRight = self.findLeftSub(x, a, b, 2 * nodeId + 2, (l + r) // 2, r)
            return resRight

        def findLeft(self, x):
            return self.findLeftSub(x, 0, self.lenTreeList, 0, 0, self.lenTreeList)

        def findLeftRange(self, x, a, b):
            return self.findLeftSub(x, a, b, 0, 0, self.lenTreeList)

    n, k, d = map(int, input().split())
    dat = list(map(int, input().split()))
    st = segmentTreeMin()
    st.load(dat)

    l = 1 + ((k - 1) * d )
    yoyuu = n - l
    if l > n:
        print(-1)
    else:
        #print(n, k, d)
        #print(n, l, yoyuu)
        res = []
        cursor = 0
        for i in range(k):
            #print("st[{0}, {1})".format(cursor, cursor + yoyuu+1))
            v, ind = st.query(cursor, cursor+yoyuu+1)
            for i in range(cursor, n):
                if dat[i] == v:
                    ind = i
                    break
            #print(yoyuu, cursor, yoyuu, ind)
            yoyuu = (cursor + yoyuu - ind)
            cursor = ind + d
            #print("i",i, "v",v, "ind",ind, "newyoyuu", yoyuu)
            res.append(v)
        print(" ".join(list(map(str, res))))


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
        input = """3 2 2
3 1 4"""
        output = """3 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 2
3 1 4"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 2 1
3 1 4"""
        output = """1 4"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """4 2 2
3 6 5 5"""
        output = """3 5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()