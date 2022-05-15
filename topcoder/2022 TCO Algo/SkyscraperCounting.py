# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

# 組み合わせ
def nCr(n, r):
    import math
    # nCrのr>nは組み合わせが存在しないので0を返す
    # raiseすべきのこともあるかも
    if r > n:
        return 0
    return math.factorial(n) //  ( (math.factorial(n - r) * math.factorial(r)) )


def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans %= 10**9+7
    return ans

class SkyscraperCounting:
    def count(self, visibility):
        mod = 10**9 + 7
        visibility = visibility + "O"
        n = len(visibility)
        nextx = [0] * 101
        cnt = 0
        ind = 0
        for i in range(1, n):
            if visibility[i] == "X":
                cnt += 1
                continue
            nextx[ind] = cnt
            cnt = 0
            ind += 1
        nextx[ind] = cnt
        dp = [0] * (101)
        for i in range(nextx[0] + 1, 100):
            dp[i] = 1
        ocnt = visibility.count("O")
        for i in range(1, ocnt):
            print(dp)
            nd = [0] * (101)
            for j in range(1, 101):
                for prev in range(1, 101):
                    nxt = prev + j
                    if nxt > n: continue
                    nd[nxt] += dp[prev] * fac(nextx[i-1])
                    nd[nxt] %= mod
            dp = nd
        return (sum(dp[:n+1]) % mod)





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

def do_test(visibility, __expected):
    startTime = time.time()
    instance = SkyscraperCounting()
    exception = None
    try:
        __result = instance.count(visibility);
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
    sys.stdout.write("SkyscraperCounting (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SkyscraperCounting.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            visibility = f.readline().rstrip()
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(visibility, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1650127709
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
