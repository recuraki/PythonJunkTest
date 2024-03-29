# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

from __future__ import division

class LunchLine:
    def simulate(self, n, m, a,b,c,d,e):

        k = [None] * m
        if m > 0: k[0] = a
        if m > 1: k[1] = b
        for i in range(2, m):
            k[i] = (c * k[i - 1] + d * k[i - 2] + e) % n
        #if len(k ) > 100:
        #    return
        #print(k)
        number = [i for i in range(n)]
        #print("n", len(number))
        #print("num", number[:10])
        #print("k ", k[:100])
        jun = n + 5000000
        for x in k:
            #print(x, jun)
            number[x] = jun
            jun += 1
        #print("num", number[:10])
        buf = []
        for i in range(n):
            buf.append( (number[i], i) )
        buf.sort()
        #print(buf[:10])
        dat = []
        res = 0
        for i in range(len(buf)):
            dat.append(buf[i][1])
            res += i * buf[i][1]

        #print(dat)
        return res


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

def do_test(N, M, A, B, C, D, E, __expected):
    startTime = time.time()
    instance = LunchLine()
    exception = None
    try:
        __result = instance.simulate(N, M, A, B, C, D, E);
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
    sys.stdout.write("LunchLine (900 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LunchLine.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            M = int(f.readline().rstrip())
            A = int(f.readline().rstrip())
            B = int(f.readline().rstrip())
            C = int(f.readline().rstrip())
            D = int(f.readline().rstrip())
            E = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, M, A, B, C, D, E, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1626175505
    PT, TT = (T / 60.0, 75.0)
    points = 900 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
