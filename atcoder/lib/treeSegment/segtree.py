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
"""
https://ei1333.hateblo.jp/entry/2017/12/14/000000
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

    def findLeftSub(self, x, a, b, nodeIf, l, r):
        """
        [a,b) 区間の中からxとなる最も左のindexを返す
        これは、nodeIdではなくて、元のlistのindexである
        """
        if (r <= a or b <= l): # 範囲外の時
            return None
        if self.dat[nodeIf] != x: # このノードの最小がx出ないときはこのノードにxは含まれないので
            return None
        if nodeIf >= self.lenTreeList - 1: # nodeIfがノードのとき
            return self.dat[nodeIf] #



    def findLeft(self, x):
        return self.findLeftSub(x, 0, self.lenTreeList, 0, 0, self.lenTreeList)

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
# 単なる数, 右に連続している個数, 左に連続している個数, 連続している数, (想定では端から)連続するNoneの数
# をカウントします
# cons: consecutive
# dataは
# char=入っているデータ, cnt, consLeft, consRight, consLen, noneNumの数
class segmentTreeCharCount():
    dat = []
    lenTreeList = -1
    targetChar = None
    depthTreeList = 0
    lenPaddingEntry = 0
    unitDefault = [None, 0, 0, 0, 0, 1]

    def __init__(self):
        pass

    def load(self, l, tc):
        self.targetChar = tc
        # len(l)個よりも大きい2の二乗を得る
        self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
        self.depthTreeList = (len(l) - 1).bit_length() # 木の段数(0 origin)
        # lenPaddingEntryは[1,2,3,4,5]を与えたなら[1,2,3,4,5,None,None,None]として扱ったので3を返す
        self.lenPaddingEntry = 2 ** (len(l) - 1).bit_length() - len(l) # 何エントリを補完したか

        self.dat = [self.unitDefault] * (self.lenTreeList * 2)
        # 値のロード
        for i in range(len(l)):
            if l[i] == self.targetChar:
                self.dat[self.lenTreeList - 1 + i] = [l[i], 1, 1, 1, 1, 0]
            else:
                self.dat[self.lenTreeList - 1 + i] = [l[i], 0, 0, 0, 0, 0]
        self.build()

    def funcSegmentValueById(self, nodeId):
        l = self.dat[nodeId * 2 + 1]
        r = self.dat[nodeId * 2 + 2]
        return self.funcSegmentValue(l, r, nodeId)

    # 書く計算をおこなう。
    # この際にはこの計算で境界とするl,r位置であるa,bをいれることで、右端と左端のパディングを行う
    def funcSegmentValue(self, lNode, rNode, parentNodeId):
        #print("funcSegmentValue parentNode={0}".format(parentNodeId))
        #print("L:")
        lchar, lcnt, lconsLeft, lconsRight, lconsLen, lNoneNum= lNode
        #print(lNode)
        #print("R:")
        rchar, rcnt, rconsLeft, rconsRight, rconsLen, rNoneNum = rNode
        #print(rNode)

        # ここは便宜上の名前変更(あまり深い意味はない)
        if lchar is None or rchar is None:
            nchar = None
        elif rchar is not None:
            nchar = rchar
        elif lchar is not None:
            nchar = lchar

        # l, rに含まれる文字の総量
        ncnt = lcnt + rcnt

        # 連結した後の右の長さは原則的に左と一致する
        nconsLeft = lconsLeft
        nconsRight = rconsRight

        """
        #print("searchdepth = {0}".format(self.depthTreeList - ((parentNodeId + 1).bit_length() - 1)))
        if lcnt == 2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())):
            #print("child!L!")
            nconsLeft += rconsLeft
        if rcnt == 2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())):
            #print("child!R!")
            nconsRight += lconsRight
        """

        # ルートの場合、右のノードを合算するときに右のノードの左端の連続文字列数が足りなくても
        # パディング分と会うなら、左のノードの右端の連続文字列数と合算する
        #print("magic = {0}".format(2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length()))))

        if lconsLeft == (2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())) - lNoneNum):
            #print(" parentnodeid {2} l root special cur={0} add={1}".format(nconsRight, rconsLeft, parentNodeId))
            nconsLeft += rconsLeft
        if rconsRight == (2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())) - rNoneNum):
            #print(" parentnodeid {2} r root special cur={0} add={1}".format(nconsRight, rconsLeft, parentNodeId))
            #print(" nconsRight{0} += lconsLeft{1}".format(nconsRight, lconsLeft))
            nconsRight += lconsRight

        #print("update n={0}, max({1},{2},{3},{4},{5}".format(parentNodeId, nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft))

        nconsLen = max(nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft)

        nNoneNum = lNoneNum + rNoneNum
        res = [nchar, ncnt, nconsLeft, nconsRight, nconsLen, nNoneNum]
        #print("Return{0}".format(res))
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
        """
        self.dat[nodeId] = a
        if a == self.targetChar:
            self.dat[self.lenTreeList - 1 + i] = [a, 1, 1, 1, 1, 0]
        else:
            self.dat[self.lenTreeList - 1 + i] = [a, 0, 0, 0, 0, 0]
        """
        #print("before")
        #print(self.dat[nodeId])
        self.dat[nodeId] = a
        if a == self.targetChar:
            self.dat[nodeId] = [a, 1, 1, 1, 1, 0]
        else:
            self.dat[nodeId] = [a, 0, 0, 0, 0, 0]
        #print("after")
        #print(self.dat[nodeId])


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
        Noneとなる条件: r <= a or b <= l
        """
        #print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))

        if (r <= a or b <= l):
            cannotAnswer = (r - l)
            #print(" > None") # これは答えられない数を返すべき
            return [None, 0, 0, 0, 0, cannotAnswer]
        if a <= l and r <= b:
            #print(" > have: {0} [node = {1}]".format(self.dat[nodeId], nodeId))
            #print(" >     : a={0} <= l={1} and r{2} <= b{3}".format(a,l,r,b))
            res =  self.dat[nodeId]
            return res

        #print("querySubcalc: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
        resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
        #print("querySubend: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        #print(" > L")
        #print("  node{0}: {1}".format(2 * nodeId + 1, resLeft))
        #print(" > R")
        #print("  node{0}: {1}".format(2 * nodeId + 2, resRight))
        #print(resRight)
        res = self.funcSegmentValue(resLeft, resRight, nodeId)
        #print(" > res")
        #print(res)
        return res

    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.lenTreeList)

    def debugGetSliceStr(self, a, b):
        """
        元の文字列リストの[a:b]を返す: str
        """
        return "".join(list(map(lambda x: x[0], self.dat[self.lenTreeList - 1 + a:self.lenTreeList - 1 + b])))


from pprint import pprint



def test1(a,b):
    pprint(st.query(a, b))
    pprint(st.debugGetSliceStr(a, b))


l = list("xaazaaa")
l = list("xaaaaa0A")
l = list("abaaabcaaaaxasaaa")
st = segmentTreeCharCount()
st.load(l, "a")
st.build()
#st.setValue(2, "x")
#st.setValue(4, "x")
#print("-----")
#pprint(st.dat)

print("----------------------------")
test1(0,9)
st.setValue(1, "a")
test1(0,9)
st.setValue(0, "x")
st.setValue(1, "x")
st.setValue(2, "x")
st.setValue(3, "x")
st.setValue(8, "x")
test1(0,9)


