# -*- coding: utf-8 -*-
from __future__ import division
from fractions import Fraction
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SingleOrDouble:
    def probAlice(self, N, D, A, B):
        dp = [[0] * 101 for _ in range(N)]
        for i in range(1, D+1):
            dp[0][i] = 1/D
        for kai in range(1, N):
            for i in range(1, D+1):
                for prev in range(1, 101):
                    cur = i + prev
                    if cur > 100: continue
                    dp[kai][cur] += dp[kai-1][prev] / D
        pa = dp[-1][A]
        pb = dp[-1][B]
        pc = 1 - pa - pb
        dat = [pa, pb, 0, pc]
        for _ in range(100000):
            nd = [0, 0, 0, 0]
            nd[0] = dat[0]
            nd[0] += dat[1] * pa
            nd[0] += dat[3] * pa
            nd[1] = dat[3] * pb
            nd[2] = dat[2]
            nd[2] += dat[1] * pb
            nd[3] = dat[1] * pc
            nd[3] += dat[3] * pc
            dat = nd
        #print(dat)
        return(dat[0])

class SingleOrDouble2:
    def probAlice(self, N, D, A, B):
        dp = [[Fraction(0, 1)] * 101 for _ in range(N)]
        for i in range(1, D+1):
            dp[0][i] = Fraction(1, D)
        for kai in range(1, N):
            for i in range(1, D+1):
                for prev in range(1, 101):
                    cur = i + prev
                    if cur > 100: continue
                    dp[kai][cur] += dp[kai-1][prev] * Fraction(1, D)
        pa = dp[-1][A]
        pb = dp[-1][B]
        pc = 1 - pa - pb
        dat = [pa, pb, 0, pc]
        for _ in range(300):
            nd = [0, 0, 0, 0]
            nd[0] = dat[0]
            nd[0] += dat[1] * pa
            nd[0] += dat[3] * pa
            nd[1] = dat[3] * pb
            nd[2] = dat[2]
            nd[2] += dat[1] * pb
            nd[3] = dat[1] * pc
            nd[3] += dat[3] * pc
            dat = nd
        print(dat)
        print(float(dat[0]))




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

def do_test(N, D, A, B, __expected):
    startTime = time.time()
    instance = SingleOrDouble()
    exception = None
    try:
        __result = instance.probAlice(N, D, A, B);
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
    sys.stdout.write("SingleOrDouble (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SingleOrDouble.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            D = int(f.readline().rstrip())
            A = int(f.readline().rstrip())
            B = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, D, A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1650125441
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
