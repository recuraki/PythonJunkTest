# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class DevuAndEqualizingLCM:
    def minimumOperationsNeeded(self, a, b):
        import math
        import fractions
        import decimal
        a = list(a)
        b = list(b)

        def lcm(x, y):
            return (x * y) // fractions.gcd(x, y)

        def lcmList(l):
            x = 1
            for i in range(len(l)):
                x = lcm(x, l[i])
            return x

        def factorization(n):
            arr = []
            temp = n
            for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
                if temp % i == 0:
                    cnt = 0
                    while temp % i == 0:
                        cnt += 1
                        temp //= i
                    arr.append([i, cnt])
            if temp != 1:
                arr.append([temp, 1])
            if arr == []:
                arr.append([n, 1])
            return arr

        # [2, 5, 5]
        def factorization_expand(n):
            l = factorization(n)
            dat = []
            for a, b in l:
                dat += [a] * b
            return dat

        from collections import defaultdict
        ps = defaultdict(int)
        for x in a:
            l = factorization(x)
            for p, num in l:


        for i in range(len(b)):
            b[i] = decimal.Decimal(b[i])
        numa = lcmList(a)
        print(numa)
        t = factorization_expand(numa)
        res = 0
        for i in range(len(b)):
            x = b[i]
            f = fractions.gcd(numa, x)
            if f == 1:
                b[i] = numa
                res += 1
        numb = lcmList(b)
        print(numb)
        return res



        return 0

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
    instance = DevuAndEqualizingLCM()
    exception = None
    try:
        __result = instance.minimumOperationsNeeded(A, B);
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
    sys.stdout.write("DevuAndEqualizingLCM (400 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DevuAndEqualizingLCM.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = []
            for i in range(0, int(f.readline())):
                A.append(int(f.readline().rstrip()))
            A = tuple(A)
            B = []
            for i in range(0, int(f.readline())):
                B.append(int(f.readline().rstrip()))
            B = tuple(B)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1632967064
    PT, TT = (T / 60.0, 75.0)
    points = 400 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
