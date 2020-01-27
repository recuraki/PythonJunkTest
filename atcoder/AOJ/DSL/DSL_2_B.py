import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class segmentTreeSum():
        initValue = 0
        dat = []
        lenData = -1

        def __init__(self):
            pass

        def load(self, l):
            # len(l)個よりも大きい2の二乗を得る
            self.lenData = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
            self.dat = [self.initValue] * (self.lenData * 2)
            # 値のロード
            for i in range(len(l)):
                self.dat[self.lenData - 1 + i] = l[i]
            self.build()

        def build(self):
            for i in range(self.lenData - 2, -1, -1):
                self.dat[i] = self.dat[2 * i + 1] + self.dat[2 * i + 2]

        # 若干無駄なインストラクションあるのでコードレベルでマージしたほうがいいかも
        def addValue(self, i, a):
            nodeId = (self.lenData - 1) + i
            self.dat[nodeId] += a
            self.setValue(i, self.dat[nodeId])

        def setValue(self, i, a):
            """
            set a to list[i]
            """
            #print("setValue: {0}, {1}".format(i, a))
            nodeId = (self.lenData - 1) + i
            #print(" first nodeId: {0}".format(nodeId))
            self.dat[nodeId] = a
            while nodeId != 0:
                nodeId = (nodeId - 1) // 2
                #print(" next nodeId: {0}".format(nodeId))
                self.dat[nodeId] = self.dat[nodeId * 2 + 1] + self.dat[nodeId * 2 + 2]

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
            return resLeft + resRight

        def query(self, a, b):
            return self.querySub(a, b, 0, 0, self.lenData)

    initVal = 0
    n, q = map(int, input().split())
    dat = [initVal] * n
    st = segmentTreeSum()
    st.load(dat)
    st.build()
    #print(st.dat)
    for _ in range(q):
        # indexの入力が1 originなので注意 (以下で-1しているのはそのため)
        cmd, a, b = map(int, input().split())
        if cmd == 0: # update
            st.addValue(a - 1, b)
        else:
            print(st.query(a - 1 , b + 1 -1))


class TestClass(unittest.TestCase):
    maxDiff = 10000
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 13
0 1 1
0 2 3
1 1 1
1 2 2
1 1 2
0 1 4
1 1 1
1 2 2
1 1 2
0 1 4
1 1 1
1 2 2
1 1 2"""
        output = """1
3
4
5
3
8
9
3
12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()