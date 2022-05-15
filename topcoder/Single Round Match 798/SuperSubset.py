# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SuperSubset:

    def solve(self, dat, y):
        m = 10**9 + 7
        def nCr(n, r):
            import math
            # nCrのr>nは組み合わせが存在しないので0を返す
            # raiseすべきのこともあるかも
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

        ll = len(dat)

        import collections
        d = [collections.defaultdict(int) for _ in range(10010)]
        d[0][0] = 1
        for x in dat:
            for i in range(10000, -1, -1):
                if (i + x) > y:
                    continue
                for key in d[i]:
                    d[i+x][key+1] += d[i][key]

        res = 0
        orid = d[y]
        for key in d[y]: # key is kumi
            res += d[y][key] # 3 own
        # shita
        for i in range(y-1, 0, -1):
            for key in d[y]:
                if (i - key) >= 0:
                    res += d[y][key] * nCr(i, key)
                    res %= m
        # ue
        for i in range(y+1, ll+1):
            for key in d[y]:
                res += nCr(i, key)
                res %= m
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

def do_test(A, Y, __expected):
    startTime = time.time()
    instance = SuperSubset()
    exception = None
    try:
        __result = instance.solve(A, Y);
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
    sys.stdout.write("SuperSubset (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SuperSubset.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = []
            for i in range(0, int(f.readline())):
                A.append(int(f.readline().rstrip()))
            A = tuple(A)
            Y = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, Y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1611422906
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
