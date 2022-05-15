# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class cumSum1D(object):
    sdat = []
    def init(self):
        pass
    def load(self, l):
        import itertools
        self.sdat = [0] * (len(l) + 1)
        for i in range(len(l)):
            self.sdat[i+1] = self.sdat[i] + l[i]
    def query(self, l, r):
        """
        query [l, r)
        """
        # assert l < r
        return self.sdat[r] - self.sdat[l]

from collections import defaultdict
class pairmng(object):
    def __init__(self):
        self.cntR = defaultdict(int)
        self.cntL = defaultdict(int)
        self.paircnt = 0
    def addinit(self, x):
        self.cntR[x] += 1
    def query(self):
        return self.paircnt
    def proc(self, x):
        self.paircnt -= min(self.cntR[x], self.cntL[x])
        assert self.paircnt >= 0
        self.cntL[x] += 1
        self.cntR[x] -= 1
        self.paircnt += min(self.cntR[x], self.cntL[x])




class MedianSegments:
    def count(self, n, k, aprefix, m):
        l = len(aprefix)
        dat = [None] * n
        for i in range(l):
            dat[i] = aprefix[i]
        state = aprefix[l-1]
        for i in range(l, n):
            state = (state * 1103515245 + 12345) % (2 ** 31)
            dat[i] = state % m
        target = dat[k]
        for i in range(n):
            if dat[i] == target: dat[i] = 0
            elif dat[i] > target: dat[i] = 1
            elif dat[i] < target: dat[i] = -1
            else: assert False
        cum = cumSum1D()
        cum.load(dat)
        even = pairmng()
        odd = pairmng()
        for i in range(n):
            if i % 2 == 0: even.addinit(cum.sdat[i+1])
            else: odd.addinit(cum.sdat[i+1])
        print()
        print(dat)
        print(cum.sdat)
        print(even.cntR)
        print(odd.cntR)
        ans = 0
        for i in range(n):
            print(i)
            if dat[i] == 0:
                ans += even.query() + odd.query()
                print(even.query(), odd.query())
                print(even.cntR)
                print(even.cntL)
                print(odd.cntR)
                print(odd.cntL)
                continue
            if i % 2 == 0: even.proc(cum.sdat[i+1] )
            else: odd.proc(cum.sdat[i+1])
            continue

        print(cum.sdat)
        print(dat)
        return ans


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

def do_test(N, K, Aprefix, M, __expected):
    startTime = time.time()
    instance = MedianSegments()
    exception = None
    try:
        __result = instance.count(N, K, Aprefix, M);
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
    sys.stdout.write("MedianSegments (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MedianSegments.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            K = int(f.readline().rstrip())
            Aprefix = []
            for i in range(0, int(f.readline())):
                Aprefix.append(int(f.readline().rstrip()))
            Aprefix = tuple(Aprefix)
            M = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, K, Aprefix, M, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1636129783
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
