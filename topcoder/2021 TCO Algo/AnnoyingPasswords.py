# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class AnnoyingPasswords:
    def count(self, u, l, d):
        from pprint import pprint
        def nCr(n, r):
            import math
            # nCrのr>nは組み合わせが存在しないので0を返す
            # raiseすべきのこともあるかも
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
        m = 10**9 + 7
        dp = [[[[0] * 3 for _ in range(10)] for _ in range(26)] for _ in range(26)]
        def f(a, b, c):
            if a > u: return 0,0,0
            if b > l: return 0,0,0
            if c > d: return 0,0,0
            if a == u and b == l and c == d:
                return u, l, d
            aa, bb, cc = f(a+1, b, c)


        print(f(0, 0, 0))



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

def do_test(U, L, D, __expected):
    startTime = time.time()
    instance = AnnoyingPasswords()
    exception = None
    try:
        __result = instance.count(U, L, D);
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
    sys.stdout.write("AnnoyingPasswords (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("AnnoyingPasswords.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            U = int(f.readline().rstrip())
            L = int(f.readline().rstrip())
            D = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(U, L, D, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1625742310
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
