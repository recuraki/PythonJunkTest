import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    inf = 2 ** 31 - 1
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
                return self.inf
            if a <= l and r <= b:
                # print(" > return(have): {0}".format(self.dat[nodeId]))
                return self.dat[nodeId]
            resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
            resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
            # print(" > return(lr): {0}".format(min(resLeft, resRight)))
            return min(resLeft, resRight)

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


    import heapq

    st = segmentTreeMin()
    ll = [inf] * 200100
    st.load(ll)

    yochien = []
    deleteQueue = []

    for i in range(200100):
        yochien.append([])
        deleteQueue.append([])

    for i in range(200100):
        heapq.heapify(yochien[i])
        heapq.heapify(deleteQueue[i])

    n, q = map(int, input().split())

    enjiRate = [0] * (n + 1)
    yoshienNONinzu = [0] * 200100 # 幼稚園ごとの人数
    currentyochien = [-1] * (n+1)

    for i in range(n):
        a, b = map(int, input().split())
        enjiRate[i + 1] = a # rate
        currentyochien[i + 1] = b
        heapq.heappush(yochien[b], -a)
        yoshienNONinzu[b] += 1

    allmin = 99999999999999

    for i in range(200100):
        if yoshienNONinzu[i] == 0:
            continue
        x = heapq.heappop(yochien[i])
        #print("yo", i, x)
        allmin = min(allmin, -x)
        st.setValue(i, -x)
        heapq.heappush(yochien[i], x)

    #print("default allmin", st.query(0, 200101))
    #print("rate", enjiRate[:10])

    for loop in range(q):
        idouenji, nextyochien = map(int, input().split())
        prevyochien = currentyochien[idouenji]
        currentyochien[idouenji] = nextyochien

        enji_no_rate = enjiRate[idouenji]
        yoshienNONinzu[prevyochien] -= 1
        yoshienNONinzu[nextyochien] += 1
        if yoshienNONinzu[prevyochien] == 0: # 0人になったらカウント対象外
            st.setValue(prevyochien, inf)

        #print("enji ", idouenji, prevyochien, nextyochien, "rate", enji_no_rate)

        # next 幼稚園の処理
        heapq.heappush(yochien[nextyochien], -enji_no_rate)
        x = heapq.heappop(yochien[nextyochien])
        heapq.heappush(yochien[nextyochien], x)
        st.setValue(nextyochien, -x)
        #print("next-max", nextyochien, x)

        # prev 幼稚園の処理
        heapq.heappush(deleteQueue[prevyochien], -enji_no_rate)

        while len(deleteQueue[prevyochien]) > 0:
            target = heapq.heappop(deleteQueue[prevyochien])
            imanotsuyoi = heapq.heappop(yochien[prevyochien])
            if target == imanotsuyoi:
                continue
            else:
                heapq.heappush(yochien[prevyochien], imanotsuyoi)
                heapq.heappush(deleteQueue[prevyochien], imanotsuyoi)
                break

        if len(yochien[prevyochien])> 0:
            x = heapq.heappop(yochien[prevyochien])
            heapq.heappush(yochien[prevyochien], x)
            st.setValue(prevyochien, -x)
            #print("prev-max", prevyochien, x)

        print(st.query(0, 200101))


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
        input = """6 3
8 1
6 2
9 3
1 1
2 2
1 3
4 3
2 1
1 2"""
        output = """6
2
6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
4208 1234
3056 5678
1 2020
2 2020"""
        output = """3056
4208"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()