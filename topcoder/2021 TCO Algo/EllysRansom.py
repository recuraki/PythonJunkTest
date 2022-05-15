# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

from collections import deque

class DinicRecurcive(object):
    INF = 2 ** 60

    def __init__(self, n):
        """
        n: num of vertex
        """
        self.e = [[] for _ in range(n)]
        self.dist = [-1] * n
        self.iter = [-1] * n
        self.n = n

    def makeEdge(self, s, t, cap):
        l = [t, cap, None]  # edge
        lrev = [s, 0, l]  # reverse edge
        l[2] = lrev
        self.e[s].append(l)
        self.e[t].append(lrev)

    def bfs(self, s):
        self.dist[s] = 0  # init start point
        q = deque([])
        q.appendleft(s)
        while len(q) > 0:
            curNode = q.popleft()
            # print("curNode", curNode)
            for nextNode, edgeCap, revEdge in self.e[curNode]:
                # print("edgeCap", nextNode, edgeCap)
                if edgeCap > 0 and self.dist[nextNode] == -1:
                    self.dist[nextNode] = self.dist[curNode] + 1
                    q.appendleft(nextNode)
    def solve(self, s, g):
        """Max-Flow! """
        flow = 0
        while True:
            self.dist = [-1] * self.n
            self.bfs(s)
            if self.dist[g] == -1:
                return flow
            self.iter = [-1] * self.n
            while True:
                res = self.dfs(s, g, self.INF)
                if res <= 0: # cannot more flow Then End
                    break
                flow += res

    def dfs(self, curNode, g, flow):
        if curNode == g:
            return flow

        for i in range(self.iter[curNode], len(self.e[curNode])):

            self.iter[curNode] += 1

            l = self.e[curNode][i]  # node, cap, revpath

            # go only forward, don't back to parent
            if l[1] > 0 and self.dist[curNode] < self.dist[l[0]]:
                f = self.dfs(l[0], g, min(flow, l[1]))
                if f > 0:
                    l[1] -= f
                    l[2][1] += f
                    return f
        return 0
class EllysRansom:

    def getRansom(self, A, B, T):
        mf = DinicRecurcive(2 + 1000 + 26 + 100)
        s = 1100
        t = 1101
        # 0-999 are cards
        # 1000 - 1025 are Alpha
        for i in range(len(A)):
            x = ord(A[i]) - ord("A")
            mf.makeEdge(i, 1000 + x, 1)
            x = ord(B[i]) - ord("A")
            mf.makeEdge(i, 1000 + x, 1)
            mf.makeEdge(s, i, 1)
        for i in range(26):
            x = T.count(chr(ord("A") + i))
            mf.makeEdge(1000+i, t, x)
        flow = mf.solve(s, t)
        if flow != len(T):
            return 	"NO SOLUTION"
        print(flow)
        s = ""
        for i in range(len(A)):
            ok = False
            for dst, use, _ in mf.e[i]:
                if dst == s or dst == t:
                    continue
                if use == 0:
                    if 1000 <= dst <= 1025:
                        s += chr(ord("A") + dst - 1000)
                        ok = True
                        break
            if ok is False:
                s += "_"
        return s



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

def do_test(A, B, T, __expected):
    startTime = time.time()
    instance = EllysRansom()
    exception = None
    try:
        __result = instance.getRansom(A, B, T);
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
    sys.stdout.write("EllysRansom (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EllysRansom.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = f.readline().rstrip()
            B = f.readline().rstrip()
            T = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, T, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1618678166
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
