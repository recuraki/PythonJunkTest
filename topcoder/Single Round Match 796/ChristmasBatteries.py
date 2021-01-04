# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ChristmasBatteries:
    def mostFun(self, b, n, x, y, z, m):
        dat = [0] * n
        initialValue = 0
        for i in range(n):
            dat[i] = ((((x*i) % m *i) % m) + y * i + z)%m
        print(dat)
        buf = [[] for _ in range(5)]
        for i in range(n):
            x = i % 5
            if x == 0:
                initialValue += dat[i]
                continue
            buf[x].append(dat[i])
        tmp = [0] * 10
        for i in range(5):
            buf[i].sort()
        for i in range(min(len(buf[1]), 4)):
            tmp[0 + i] = buf[1][i]
        for i in range(min(len(buf[2]), 3)):
            tmp[4 + i] = buf[2][i]
        for i in range(min(len(buf[3]), 2)):
            tmp[7 + i] = buf[3][i]
        for i in range(min(len(buf[4]), 1)):
            tmp[9 + i] = buf[4][i]
        cost = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        res = 0
        for pat in range(0, 2**10):
            costtmp = 0
            restmp = 0
            for i in range(10):
                if (pat >> i & 1) == 1:
                    costtmp += cost[i]
                    restmp += tmp[i]
            if costtmp <= b:
                res = max(res, restmp)

        return res+initialValue

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

def do_test(B, N, X, Y, Z, M, __expected):
    startTime = time.time()
    instance = ChristmasBatteries()
    exception = None
    try:
        __result = instance.mostFun(B, N, X, Y, Z, M);
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
    sys.stdout.write("ChristmasBatteries (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ChristmasBatteries.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            B = int(f.readline().rstrip())
            N = int(f.readline().rstrip())
            X = int(f.readline().rstrip())
            Y = int(f.readline().rstrip())
            Z = int(f.readline().rstrip())
            M = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(B, N, X, Y, Z, M, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1608727988
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
