# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

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


class YetAnotherGraphColoring:
    def minColors(self, n, a1, a2, x, y, z, m):
        n = 200000
        a = [0] * (n)
        ss = set()
        a[0] = a1
        a[1] = a2
        ss.add(a1)
        ss.add(a2)
        for i in range(2, n):
            a[i] = (x * a[i-1] + y * a[i-2] + z) % m
            ss.add(a[i])
        ss = list(ss)
        ss.sort()
        #print(ss)
        #print(a)
        zatsu = dict()
        for i in range(len(ss)):
            zatsu[ss[i]] = i
        #print(zatsu)

        st = segmentTreeSum()
        l = [0] * 200100
        st.load(l)

        buf = []
        for i in range(n-1, -1, -1):
            ind = zatsu[a[i]]
            st.addValue(ind, 1)
            val = st.query(0,ind)
            buf.append( (val, i) )
        return
        buf.sort(reverse=True)
        #print(buf)
        e = [set() for _ in range(200100)]
        q = []
        for k in range(min(3, n)):
            _, i = buf[k]
            q.append(i)
            for j in range(i+1, n):
                if a[i] > a[j]:
                    if j not in e[i]:
                        e[i].add(j)
                    if i not in e[j]:
                        e[j].add(i)

        color = [-1] * n
        visited = set()
        #print(e[:n])

        for curnode in q:
            #print(">", curnode, color[:100])
            visited.add(curnode)
            if color[curnode] == -1:
                color[curnode] = 0
            for nextnode in e[curnode]:
                if nextnode in visited:
                    continue
                #print("try>",nextnode)
                if color[nextnode] == -1:
                    if color[curnode] == 0:
                        color[nextnode] = 1
                    else:
                        color[nextnode] = 0
                elif color[nextnode] == 1:
                    color[curnode] = 2
            #print(">", curnode, color[:100])

        #print(color[:100])
        ma = max(color)
        return (ma + 1)

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(n, a1, a2, x, y, z, m, __expected):
    startTime = time.time()
    instance = YetAnotherGraphColoring()
    exception = None
    try:
        __result = instance.minColors(n, a1, a2, x, y, z, m);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("YetAnotherGraphColoring (400 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("YetAnotherGraphColoring.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            a1 = int(f.readline().rstrip())
            a2 = int(f.readline().rstrip())
            x = int(f.readline().rstrip())
            y = int(f.readline().rstrip())
            z = int(f.readline().rstrip())
            m = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, a1, a2, x, y, z, m, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1619176033
    PT, TT = (T / 60.0, 75.0)
    points = 400 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
