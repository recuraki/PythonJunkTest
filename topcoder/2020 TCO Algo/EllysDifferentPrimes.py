# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class EllysDifferentPrimes:
    def is_prime(q, k=50):
        q = abs(q)
        if q == 2: return True
        if q < 2 or q & 1 == 0: return False

        d = (q - 1) >> 1
        while d & 1 == 0:
            d >>= 1

        for i in xrange(k):
            a = random.randint(1, q - 1)
            t = d
            y = pow(a, t, q)
            while t != q - 1 and y != 1 and y != q - 1:
                y = pow(y, 2, q)
                t <<= 1
            if y != q - 1 and t & 1 == 0:
                return False
        return True


    def getClosest(self, N):
        canhigh = True
        if N > 987654321:
            N = 987654321
            canhigh = False
        a,b = None

        # high
        x = N
        while True:
            if N > 987654321:
                canhigh = False
                break
            used = [False] * 10
            s = list(str(x))
            isfail = False
            for i in range(len(s)):
                v = int(s[i])
                if used[v] is True:
                    s[i] += 1
                    if s[i] = 10:
                        s[i] = 0
                        s[i-1] += 1
                        isfail = True
                        break
            if isfail:
                x = int("".join(s))
                continue




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

def do_test(N, __expected):
    startTime = time.time()
    instance = EllysDifferentPrimes()
    exception = None
    try:
        __result = instance.getClosest(N);
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
    sys.stdout.write("EllysDifferentPrimes (900 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EllysDifferentPrimes.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1588073853
    PT, TT = (T / 60.0, 75.0)
    points = 900 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
