# https://tjkendev.github.io/procon-library/python/range_query/rsq_ruq_segment_tree_lp.html
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

    # just wrapper
    def addValue(self, ind, value):
        nodeId = (self.lenTreeLeaf - 1) + ind
        self.dat[nodeId] += value
        self.setValue(ind, self.dat[nodeId])

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

import sys

def DSL_2_E():
    n, q = map(int,input().split())
    st = segmentTreeSum()
    l = [0] * n
    st.load(l)
    for _ in range(q):
        dat = map(int, input().split())
        dat = list(dat)
        if dat[0] == 0:
            l, r = dat[1]-1, dat[2]-1 + 1
            x = dat[3]
            st.rangeAdd(l, r, x)
            #print(st.dat)
        elif dat[0] == 1:
            i = dat[1]-1
            print(st.query(i, i+1))

def DSL_2_G():
    import sys
    input = sys.stdin.readline
    readline = sys.stdin.readline
    write = sys.stdout.write
    n, q = map(int,input().split())
    st = segmentTreeSum()
    l = [0] * n
    st.load(l)
    ans = []
    for _ in range(q):
        dat = map(int, input().split())
        dat = list(dat)
        if dat[0] == 0:
            l, r = dat[1], dat[2]+1
            l-=1
            r-=1
            x = dat[3]
            st.rangeAdd(l, r, x)
            #print(st.dat)
            #print(st.lazy[:st.lenTreeLeaf-1])
        elif dat[0] == 1:
            l, r = dat[1], dat[2]+1
            l-=1
            r-=1
            ans.append(str(st.query(l, r)))
            #print(st.dat)
            #print(st.lazy[:st.lenTreeLeaf-1])
    write("\n".join(ans))
    write("\n")

def RSA_test():
    l = [1, 0, 2, 3, 4, 0, 1]
    st = segmentTreeSum()
    st.load(l)
    st.build()
    print(st.dat)
    for i in range(0, len(l) + 1):
        print(" query[0, {0}) = {1}".format(i, st.query(0, i)))
    st.rangeAdd(3, 7, 100)
    st.rangeAdd(3, 6, 1000)
    print(st.dat)
    print(st.lazy)
    print(st.dat[:st.lenTreeLeaf - 1])
    print(st.dat[st.lenTreeLeaf - 1:])
    for i in range(0, len(l) + 1):
        print(" query[0, {0}) = {1}".format(i, st.query(0, i)))

    print(st.query(0, 8))

    print(st.dat)
    print(st.lazy)
    print(st.dat[:st.lenTreeLeaf - 1])
    print(st.dat[st.lenTreeLeaf - 1:])
    print("lenTreeList", st.lenTreeLeaf)

def RMQ_RMA():
    l = [200, 100, 1000, 0, 300]
    st = segmentTreeMin()
    st.load(l)
    print(st.dat)
    st.build()
    for i in range(0, len(l) + 1):
        print(" query[0, {0}) = {1}".format(i, st.query(0, i)))
    st.rangeAdd(1, 3+1, 10000)
    for i in range(0, len(l) + 1):
        print(" query[0, {0}) = {1}".format(i, st.query(0, i)))
    print(st.dat)

#DSL_2_E()
DSL_2_G()
#sys.exit()
#RSA_test()
#RMQ_RMA()


