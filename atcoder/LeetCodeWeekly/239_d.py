from typing import List, Tuple
from pprint import pprint

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
        self.lenOriginalList = self.N # original nodes
        self.depthTreeList = (self.N - 1).bit_length() # Level of Tree
        self.lenTreeLeaf = 2 ** self.depthTreeList  # leaf of node, len 5 -> 2^3 = 8
        self.dat = [self.initValue] * (self.lenTreeLeaf * 2)
        self.lazy = [self.initValue] * (self.lenTreeLeaf * 2) # lazy propagete buffer

        # Load Function
        for i in range(len(l)):
            self.dat[self.lenTreeLeaf - 1 + i] = l[i]
        self.build()

    def build(self):
        for i in range(self.lenTreeLeaf - 2, -1, -1):
            self.dat[i] = self.func(self.dat[2 * i + 1], self.dat[2 * i + 2])
            #print("build: node", i, "child is ", self.dat[2 * i + 1], self.dat[2 * i + 2] ,"then I am ", self.dat[i])

    # just wrapper, get node value and op and put it
    def addValue(self, ind, value):
        nodeId = (self.lenTreeLeaf - 1) + ind
        self.dat[nodeId] += value
        self.setValue(ind, self.dat[nodeId])

    # set value to node, recalc parents NODEs
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
        #print(">>before", self.lazy, L, R)
        value = x
        while L < R:
            if R & 1:
                R -= 1
                #print(">>> updateR", R-1, value)
                self.lazy[R - 1] = self.func(self.lazy[R - 1], value)
                self.dat[R - 1] = self.func(self.dat[R - 1], value)
            if L & 1:
                #print(">>> updateL", L-1, value)
                self.lazy[L - 1] = self.func(self.lazy[L - 1], value)
                self.dat[L - 1] = self.func(self.dat[L - 1], value)
                L += 1
            L = L >> 1
            R = R >> 1
            value = self.funcRangePropagetToParent(value)
            #print(">>>END cur", L, R)
        #print(">>after", self.lazy)

        for node in plist:
            self.dat[node] = self.func(self.dat[2 * node + 1], self.dat[2 * node + 2])

    def propagete(self, plist):
        for nodeId in plist[::-1]:
            " this function will be call from top to down"
            #print("propagete", nodeId, "curlazyval =", self.lazy[nodeId])
            if self.lazy[nodeId] == self.initValue:
                continue
            if nodeId < (self.lenTreeLeaf - 1): # if this node has childs
                propageteValue = self.funcPropagateToChild(self.lazy[nodeId])
                #print(" > propagate to node")
                self.lazy[2 * nodeId + 1] = self.func(self.lazy[2 * nodeId + 1], propageteValue)
                self.lazy[2 * nodeId + 2] = self.func(self.lazy[2 * nodeId + 2], propageteValue)
                self.dat[2 * nodeId  + 1] = self.func(self.dat[2 * nodeId + 1], propageteValue)
                self.dat[2 * nodeId  + 2] = self.func(self.dat[2 * nodeId + 2], propageteValue)
            else:
                #print(" > do nothing")
                pass
            # Feedback to myself value
            #self.dat[nodeId] = self.func(self.dat[nodeId], self.lazy[nodeId])
            self.lazy[nodeId] = self.initValue

    def query(self, l, r):
        #print("query()", l, r)
        plist = self.nodelistFromLR(l, r)
        self.propagete(plist)

        L = self.lenTreeLeaf + l
        R = self.lenTreeLeaf + r

        view = []
        res = self.initValue
        while L < R:
            if R & 1:
                R -= 1
                #print(">>>checkR", R-1, "value", self.dat[R-1])
                res = self.func(res, self.dat[R-1])
            if L & 1:
                #print(">>>checkL", L-1, "value", self.dat[L-1])
                res = self.func(res, self.dat[L-1])
                L += 1
            L = L >> 1
            R = R >> 1
        return res


    def findNthValueSub(self, x, nodeId):
        """
        [2, 3, 5, 7] = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
        とマッピングされているセグメント木においてx番目に小さい値を得るための関数
        """
        if self.dat[nodeId] < x: # このノードが要求されているよりも小さい値しか持たないとき
            return (None, x - self.dat[nodeId])
        if nodeId >= self.lenTreeLeaf - 1: # nodeIfがノードのときは
            return (True, nodeId - (self.lenTreeLeaf - 1)) # そのindex番号を返す
        resLeft = self.findNthValueSub(x, 2 * nodeId + 1) # 左側の探索を行う
        if resLeft[0] != None: # もし、値が入っているならそれを返す
            return (True, resLeft[1])
        resRight = self.findNthValueSub(resLeft[1], 2 * nodeId + 2) #右側の探索を行う
        return resRight

    def findNthValue(self, x):
        return self.findNthValueSub(x, 0)[1]

class segmentTreeSum(segmentTree):
    def __init__(self):
        self.func = lambda x,y: x + y
        self.funcPropagateToChild = lambda parentValue: parentValue >> 1
        self.funcRangePropagetToParent = lambda currentValue: currentValue << 1
        self.initValue = 0

class segmentTreeMin(segmentTree):
    def __init__(self):
        self.func = lambda x,y: min(x, y)
        self.funcPropagateToChild = lambda parentValue: parentValue
        self.funcRangePropagetToParent = lambda currentValue: currentValue
        self.initValue = 2 * 10**9



class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        zatsu = set()
        for l, r in intervals:
            zatsu.add(r-l+1)
        zatsu = list(zatsu)
        zatsu.sort()
        print(zatsu)
        zatsudict = dict()
        zatsudictrev = dict()
        for i in range(len(zatsu)):
            zatsudict[zatsu[i]] = i
            zatsudictrev[i] = zatsu[i]
        zatsusize = len(zatsu)

        event = []
        for l, r in intervals:
            kukan = r-l+1
            event.append( (l, 0, zatsudict[kukan]) )
            event.append( (r, 2, zatsudict[kukan]) )
        for i in range(len(queries)):
            x = queries[i]
            event.append( (x, 1, i) )
        INF = 10**9
        l = [INF] * zatsusize
        cnt = [0] * zatsusize
        st = segmentTreeMin()
        st.load(l)
        event.sort()
        res = [None] * len(queries)
        for qtime, qtype, qval in event:
            if qtype == 0:
                cnt[qval] += 1
                st.setValue(qval, qval)
            elif qtype == 1:
                val = st.query(0, zatsusize)
                if val == INF:
                    res[qval] = -1
                else:
                    res[qval] = zatsudictrev[val]
                pass
            elif qtype == 2:
                cnt[qval] -= 1
                assert cnt[qval] >= 0
                if cnt[qval] == 0:
                    st.setValue(qval, INF)
            else:
                assert False
        return (res)




st = Solution()

print(st.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])== [3,3,1,4])
print(st.minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])==[2,-1,4,6])

