"""
セグメントツリー
base = 2 ** (len(l)-1).bit_length() と定義する。その文字列のビット上以上の2の階乗。の2倍。
親ノード: (n-1) // 2
子ノード: 2n+1, 2n+2
initしたlistのiのノードの配列番号: n^base - 1 + i

■段数の数え方
node番号iが与えられた時、ツリーの中でそれが段目かは、ルートノードを0段目とするなら( (i + 1).bit_length() - 1 )段目

リストの段数はd段 とするなら、dは0始まりで
d = (len(l) - 1).bit_length()     # dが0始まり
d = (len(l) - 1).bit_length() + 1 # dが1始まりならこっち

このため、返還前の元のリストlにおいて, node番号iの深さは「一番下のノードを0とすると」d段目
d=(len(l) - 1).bit_length() - ( (i + 1).bit_length() - 1 )
(これは一段上がると+1する変数)
"""


# 初めての実装
# https://www.creativ.xyz/segment-tree-entrance-999/
# が良かった
class segmentTreeMin():
    # とりあえず9 * 12桁
    inf = 2**31 - 1
    dat = []
    lenTreeList = -1
    depthTreeList = 0

    def __init__(self):
        pass

    def load(self, l):
        # len(l)個よりも大きい2の二乗を得る
        self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
        self.depthTreeList = (len(l) - 1).bit_length() # 木の段数(0 origin)
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
        #print("setValue: {0}, {1}".format(i, a))
        nodeId = (self.lenTreeList - 1) + i
        #print(" first nodeId: {0}".format(nodeId))
        self.dat[nodeId] = a
        while nodeId != 0:
            nodeId = (nodeId - 1) // 2
            #print(" next nodeId: {0}".format(nodeId))
            self.dat[nodeId] = min(self.dat[nodeId * 2 + 1], self.dat[nodeId * 2 + 2])

    def querySub(self, a, b, nodeId, l, r):
        """
        [a,b) 区間の親クエリに対するノードnodeへ[l, r)の探索をデリゲート
        区間については、dataの添え字は0,1,2,3,4としたときに、
        [0,3)なら0,1,2の結果を返す
        """
        #print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        if (r <= a or b <= l):
            return self.inf
        if a <= l and r <= b:
            #print(" > return(have): {0}".format(self.dat[nodeId]))
            return self.dat[nodeId]
        resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
        resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
        #print(" > return(lr): {0}".format(min(resLeft, resRight)))
        return min(resLeft, resRight)

    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.lenTreeList)

# 区間和
class segmentTreeSum():
    initValue = 0
    dat = []
    lenTreeList = -1
    depthTreeList = 0

    def __init__(self):
        pass

    def load(self, l):
        # len(l)個よりも大きい2の二乗を得る
        self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
        self.depthTreeList = (len(l) - 1).bit_length() # 木の段数(0 origin)
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
        #print("setValue: {0}, {1}".format(i, a))
        nodeId = (self.lenTreeList - 1) + i
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
        return self.querySub(a, b, 0, 0, self.lenTreeList)


# 対象となる文字の
# 単なる数, 右に連続している個数, 左に連続している個数, 連続している数
# をカウントします
# cons: consecutive
# dataは
# char=入っているデータ, cnt, consLeft, consRight, consLen
class segmentTreeCharCount():
    dat = []
    lenTreeList = -1
    targetChar = None
    depthTreeList = 0
    lenPaddingEntry = 0

    def __init__(self):
        pass

    def load(self, l, tc):
        self.targetChar = tc
        # len(l)個よりも大きい2の二乗を得る
        self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
        self.depthTreeList = (len(l) - 1).bit_length() # 木の段数(0 origin)
        # lenPaddingEntryは[1,2,3,4,5]を与えたなら[1,2,3,4,5,None,None,None]として扱ったので3を返す
        self.lenPaddingEntry = 2 ** (len(l) - 1).bit_length() - len(l) # 何エントリを補完したか

        self.dat = [[None, 0, 0, 0, 0]] * (self.lenTreeList * 2)
        # 値のロード
        for i in range(len(l)):
            if l[i] == self.targetChar:
                self.dat[self.lenTreeList - 1 + i] = [l[i], 1, 1, 1, 1]
            else:
                self.dat[self.lenTreeList - 1 + i] = [l[i], 0, 0, 0, 0]
        self.build()

    def funcSegmentValueById(self, nodeId):
        l = self.dat[nodeId * 2 + 1]
        r = self.dat[nodeId * 2 + 2]
        return self.funcSegmentValue(l, r, nodeId)

    def funcSegmentValue(self, lNode, rNode, parentNodeId):
        print("funcSegmentValue parentNode={0}".format(parentNodeId))
        print("L:")
        lchar, lcnt, lconsLeft, lconsRight, lconsLen = lNode
        print(lNode)
        print("R:")
        rchar, rcnt, rconsLeft, rconsRight, rconsLen = rNode
        print(rNode)

        # ORにしてみた
        if lchar is None or rchar is None:
            nchar = None
        elif rchar is not None:
            nchar = rchar
        elif lchar is not None:
            nchar = lchar
        ncnt = lcnt + rcnt

        nconsLeft = lconsLeft
        #print("searchdepth = {0}".format(self.depthTreeList - ((parentNodeId + 1).bit_length() - 1)))
        if lcnt == 2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())):
            #print("child!L!")
            nconsLeft += rconsLeft

        nconsRight = rconsRight
        if rcnt == 2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())):
            #print("child!R!")
            nconsRight += lconsRight

        # 右端の場合、null
        if rchar == None:
            nconsRight += lconsLeft
        if lchar == None:
            nconsLeft += rconsRight

        # ルートの場合、右のノードを合算するときに右のノードの左端の連続文字列数が足りなくても
        # パディング分と会うなら、左のノードの右端の連続文字列数と合算する
        if parentNodeId == 0 and rconsLeft == 2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())) - self.lenPaddingEntry:
            #print("root special cur={0} add={1}".format(nconsRight, rconsLeft))
            #print(lNode)
            #print(rNode)
            nconsRight += rconsLeft

        #print("update n={0}, max({1},{2},{3},{4},{5}".format(parentNodeId, nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft))
        nconsLen = max(nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft)
        res = [nchar, ncnt, nconsLeft, nconsRight, nconsLen]
        print("Return{0}".format(res))
        return res

    # char=入っているデータ, cnt, consLeft, consRight, consLen
    def build(self):
        for nodeId in range(self.lenTreeList - 2, -1, -1):
            # 重要：このコードはリストを生成しなおすので代入に直すこと！
            self.dat[nodeId] = self.funcSegmentValueById(nodeId)

    def setValue(self, i, a):
        """
        set a to list[i]
        """
        #print("setValue: {0}, {1}".format(i, a))
        nodeId = (self.lenTreeList - 1) + i
        #print(" first nodeId: {0}".format(nodeId))
        self.dat[nodeId] = a
        if a == self.targetChar:
            self.dat[self.lenTreeList - 1 + i] = (a, 1, 1, 1, 1)
        else:
            self.dat[self.lenTreeList - 1 + i] = (a, 0, 0, 0, 0)

        while nodeId != 0:
            nodeId = (nodeId - 1) // 2
            #print(" next nodeId: {0}".format(nodeId))
            # sum : self.dat[nodeId] = self.dat[nodeId * 2 + 1] + self.dat[nodeId * 2 + 2]
            self.dat[nodeId] = self.funcSegmentValueById(nodeId)

    def querySub(self, a, b, nodeId, l, r):
        """
        [a,b) 区間の親クエリに対するノードnodeへ[l, r)の探索をデリゲート
        区間については、dataの添え字は0,1,2,3,4としたときに、
        [0,3)なら0,1,2の結果を返す
        """
        print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        if (r <= a or b <= l):
            print(" > None")
            return [None, 0, 0, 0, 0]
        if a <= l and r <= b:
            print(" > have: {0}".format(self.dat[nodeId]))
            return self.dat[nodeId]

        print("querySubcalc: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
        resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
        print("querySubend: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        print(" > L")
        print("  node{0}: {1}".format(2 * nodeId + 1, resLeft))
        print(" > R")
        print("  node{0}: {1}".format(2 * nodeId + 2, resRight))
        print(resRight)
        res =  self.funcSegmentValue(resLeft, resRight, nodeId)
        print(" > res")
        print(res)
        return res

    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.lenTreeList)

from pprint import pprint

"""
l = [3,0,5,6,2,4]
stm = segmentTreeMin()
stm.load(l)
stm.build()
print(stm.dat)
print(stm.query(0, 3))
print(stm.query(2, 6))
"""

l = list("xaaxaaa")
l = list("xaaaaa0A")
st = segmentTreeCharCount()
st.load(l, "a")
st.build()
#st.setValue(2, "x")
#st.setValue(4, "x")
#pprint(st.dat)
print("---")
pprint(st.query(1,4))
#pprint(st.dat)
