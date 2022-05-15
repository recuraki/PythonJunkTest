from typing import List, Tuple
from pprint import pprint

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

    def funcSegmentValue(self, lNode, rNode, parentNodeId):
        lchar, lcnt, lconsLeft, lconsRight, lconsLen, lNoneNum = lNode
        rchar, rcnt, rconsLeft, rconsRight, rconsLen, rNoneNum = rNode

        if lchar is None or rchar is None:
            nchar = None
        elif rchar is not None:
            nchar = rchar
        elif lchar is not None:
            nchar = lchar
        ncnt = lcnt + rcnt
        nconsLeft = lconsLeft
        nconsRight = rconsRight
        if lconsLeft == (2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())) - lNoneNum):
            nconsLeft += rconsLeft
        if rconsRight == (2 ** (self.depthTreeList - ((parentNodeId + 1).bit_length())) - rNoneNum):
            nconsRight += lconsRight
        nconsLen = max(nconsLeft, nconsRight, lconsLen, rconsLen, lconsRight + rconsLeft)
        nNoneNum = lNoneNum + rNoneNum
        res = (nchar, ncnt, nconsLeft, nconsRight, nconsLen, nNoneNum)
        return res

    def build(self):
        for nodeId in range(self.lenTreeList - 2, -1, -1):
            # 重要：このコードはリストを生成しなおすので代入に直すこと！
            x = self.funcSegmentValueById(nodeId)
            self.dat[nodeId][0] = x[0]
            self.dat[nodeId][1] = x[1]
            self.dat[nodeId][2] = x[2]
            self.dat[nodeId][3] = x[3]
            self.dat[nodeId][4] = x[4]
            self.dat[nodeId][5] = x[5]

    def setValue(self, i, a):
        nodeId = (self.lenTreeList - 1) + i
        if a == self.targetChar:
            self.dat[nodeId][0] = a
            self.dat[nodeId][1] = 1
            self.dat[nodeId][2] = 1
            self.dat[nodeId][3] = 1
            self.dat[nodeId][4] = 1
            self.dat[nodeId][5] = 0
        else:
            self.dat[nodeId][0] = a
            self.dat[nodeId][1] = 0
            self.dat[nodeId][2] = 0
            self.dat[nodeId][3] = 0
            self.dat[nodeId][4] = 0
            self.dat[nodeId][5] = 0

        while nodeId != 0:
            nodeId = (nodeId - 1) // 2
            x = self.funcSegmentValueById(nodeId)
            self.dat[nodeId][0] = x[0]
            self.dat[nodeId][1] = x[1]
            self.dat[nodeId][2] = x[2]
            self.dat[nodeId][3] = x[3]
            self.dat[nodeId][4] = x[4]
            self.dat[nodeId][5] = x[5]

    def querySub(self, a, b, nodeId, l, r):
        if (r <= a or b <= l):
            cannotAnswer = (r - l)
            return [None, 0, 0, 0, 0, cannotAnswer]
        if a <= l and r <= b:
            res = self.dat[nodeId]
            return res

        resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
        resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
        res = self.funcSegmentValue(resLeft, resRight, nodeId)
        return res

    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.lenTreeList)



class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        trees = []
        for i in range(26):
            st = segmentTreeCharCount()
            st.load(list(s), chr(ord("a") + i))
            trees.append(st)
        res = []
        for k in range(len(queryCharacters)):
            ind = queryIndices[k]
            ch = queryCharacters[k]
            ans = -1
            for i in range(26):
                trees[i].setValue(ind, ch)
                ans = max(ans , trees[i].query(0, len(s))[4])
            res.append(ans)
        return(res)



st = Solution()

print(st.longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3])==[3,3,4])
print(st.longestRepeating(s = "abyzz", queryCharacters = "aa", queryIndices = [2,1])==[2,3])

