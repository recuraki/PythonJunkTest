import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def do():
        class segmentTreeSum():
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
                    self.dat[i] = self.dat[2 * i + 1] + self.dat[2 * i + 2]

            # 若干無駄なインストラクションあるのでコードレベルでマージしたほうがいいかも
            def addValue(self, i, a):
                nodeId = (self.lenTreeList - 1) + i
                self.dat[nodeId] += a
                self.setValue(i, self.dat[nodeId])

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
                return self.querySub(a, b, 0, 0, self.lenTreeList)

            def findNthValueSub(self, x, nodeId):
                """
                [2, 3, 5, 7] = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
                とマッピングされているセグメント木においてx番目に小さい値を得るための関数
                """
                # print("call findNthValueSub x={0}, nodeId={1} nodeval={2}".format(x, nodeId, self.dat[nodeId]))
                # ここから先は葉ではないノードへの処理
                if self.dat[nodeId] < x:  # このノードが要求されているよりも小さい値しか持たないとき
                    return (None, x - self.dat[nodeId])
                if nodeId >= self.lenTreeList - 1:  # nodeIfがノードのときは
                    # print(" hit node: nodeId = {0} , x = {1}, retval = {2}".format(nodeId, x, nodeId - (self.lenTreeList - 1)))
                    return (True, nodeId - (self.lenTreeList - 1))  # そのindex番号を返す
                # print(" call L()")
                resLeft = self.findNthValueSub(x, 2 * nodeId + 1)  # 左側の探索を行う
                if resLeft[0] != None:  # もし、値が入っているならそれを返す
                    # print(" call L: hit")
                    return (True, resLeft[1])
                # print(" call R()")
                resRight = self.findNthValueSub(resLeft[1], 2 * nodeId + 2)  # 右側の探索を行う
                return resRight

            def findNthValue(self, x):
                return self.findNthValueSub(x, 0)[1]

        charpos = []
        for i in range(26):
            charpos.append([])
        charused = [0] * 26
        n = int(input())
        s = input()

        l = [0] * n
        st = segmentTreeSum()
        st.load(l)
        st.build()



        targets = s[::-1]
        s = list(s)
        for i in range(n):
            x = ord(s[i]) - ord('a')
            #print(x)
            charpos[x].append(i)
        #pprint(charpos)
        #print(targets)
        res = 0
        for i in range(n):
            #print("i", i)
            tx = ord(targets[i]) - ord('a')
            used = charused[tx]
            originalpos = charpos[tx][used]
            st.setValue(originalpos, 1)
            #print("oripos", originalpos)
            charused[tx] += 1 # go next
            originalpos += st.query(originalpos+1, n)
            d = originalpos - i
            if d > 0:
                res += d
            #print("target", targets[i], d)
        print(res)


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
        input = """5
aaaza"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
cbaabc"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
icpcsguru"""
        output = """30"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()