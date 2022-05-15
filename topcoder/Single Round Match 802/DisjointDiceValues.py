# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class DisjointDiceValues:
    def getProbability(self, a,b):
        # 組み合わせ
        def nCr(n, r):
            import math
            # nCrのr>nは組み合わせが存在しないので0を返す
            # raiseすべきのこともあるかも
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))
        def do(n, r):  # n回降ってr種類出る数
            res = (1.0 / 6.0 ** (n*1.0)) * nCr(6.0, r)
            tmp = 0
            for i in range(r + 1):
                tmp += ((-1) ** (r - i)) * float(nCr(r, i)) * float((i ** n))
            return res * tmp
        res = 0
        res += (do(a, 6)) * (1 - (0 / 6.0) ** b)
        res += (do(a, 5)) * (1 - (1 / 6.0) ** b)
        res += (do(a, 4)) * (1 - (2 / 6.0) ** b)
        res += (do(a, 3)) * (1 - (3 / 6.0) ** b)
        res += (do(a, 2)) * (1 - (4 / 6.0) ** b)
        res += (do(a, 1)) * (1 - (5 / 6.0) ** b)
        res += (do(a, 0)) * (1 - (6 / 6.0) ** b)

        print(res)
        return(res)


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

def do_test(A, B, __expected):
    startTime = time.time()
    instance = DisjointDiceValues()
    exception = None
    try:
        __result = instance.getProbability(A, B);
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
    sys.stdout.write("DisjointDiceValues (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DisjointDiceValues.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = int(f.readline().rstrip())
            B = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1616151902
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
