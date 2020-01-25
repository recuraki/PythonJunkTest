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
                self.dat[self.lenTreeList - 1 + i] = (l[i], 1, 1, 1, 1)
            else:
                self.dat[self.lenTreeList - 1 + i] = (l[i], 0, 0, 0, 0)
        self.build()

    # char=入っているデータ, cnt, consLeft, consRight, consLen
    def build(self):
        for i in range(self.lenTreeList - 2, -1, -1):
            lchar, lcnt, lconsLeft, lconsRight, lconsLen = self.dat[i * 2  + 1]
            rchar, rcnt, rconsLeft, rconsRight, rconsLen = self.dat[i * 2 +  2]
            ncnt = lcnt + rcnt

            nconsLeft = lconsLeft
            print("searchdepth = {0}".format(self.depthTreeList - ( (i + 1).bit_length() - 1 )))
            if lcnt == 2 ** (self.depthTreeList - ( (i + 1).bit_length()  )):
                print("child!L!")
                nconsLeft += rconsLeft

            nconsRight = rconsRight
            if rcnt == 2 ** (self.depthTreeList - ( (i + 1).bit_length()  )):
                print("child!R!")
                nconsRight += lconsRight
            # 右端の場合、null
            if rchar == None:
                nconsRight += lconsLeft
            # ルートの場合、右のノードを合算するときに右のノードの左端の連続文字列数が足りなくても
            # パディング分と会うなら、左のノードの右端の連続文字列数と合算する
            if i == 0 and rconsLeft == 2 ** (self.depthTreeList - ( (i + 1).bit_length()  )) - self.lenPaddingEntry:
                nconsRight += lconsLeft

            nconsLen = max(nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft)
            # 重要：このコードはリストを生成しなおすので代入に直すこと！
            self.dat[i] = [lchar, ncnt, nconsLeft, nconsRight, nconsLen]

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

l = list("aaaaa")
st = segmentTreeCharCount()
st.load(l, "a")
st.build()
pprint(st.dat)