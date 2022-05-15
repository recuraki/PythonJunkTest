# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ThreeDChessRooks:
    def count(self, C, R, XP, YP, ZP, seed):
        X = [-1] * R
        Y = [-1] * R
        Z = [-1] * R
        L = len(XP)
        for i in range(L):
            print(i)
            X[i] = XP[i]
            Y[i] = YP[i]
            Z[i] = ZP[i]
        state = seed
        print()
        print(X)
        print(Y)
        print(Z)
        for i in range(L, R):
            print(i)
            state = (state * 1103515245 + 12345) % 2**31
            X[i] = state % C
            state = (state * 1103515245 + 12345) % 2**31
            Y[i] = state % C
            state = (state * 1103515245 + 12345) % 2**31
            Z[i] = state % C
        print()
        print(X)
        print(Y)
        print(Z)
        from collections import defaultdict
        hashX = defaultdict(int)
        hashY = defaultdict(int)
        hashZ = defaultdict(int)
        hashO = defaultdict(int)

        # 組み合わせ
        def nCr(n, r):
            import math
            # nCrのr>nは組み合わせが存在しないので0を返す
            # raiseすべきのこともあるかも
            if r > n:
                return 0
            return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))

        for i in range(R):
            hash = X[i] << 64 + Y[i] << 32 + Z[i] << 0
            hashO[hash] += 1
            hash = Y[i] << 32 + Z[i] << 0
            hashX[hash] += 1
            hash = X[i] << 32 + Z[i] << 0
            hashY[hash] += 1
            hash = Y[i] << 32 + X[i] << 0
            hashZ[hash] += 1

        res = 0
        for k in hashO.keys():
            res -= nCr(hashO[k], 2)
        for k in hashX.keys():
            res += nCr(R - hashX[k], 2)
        for k in hashY.keys():
            res += nCr(R - hashY[k], 2)
        for k in hashZ.keys():
            res += nCr(R - hashZ[k], 2)
        return (res)


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

def do_test(C, R, XP, YP, ZP, seed, __expected):
    startTime = time.time()
    instance = ThreeDChessRooks()
    exception = None
    try:
        __result = instance.count(C, R, XP, YP, ZP, seed);
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
    sys.stdout.write("ThreeDChessRooks (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ThreeDChessRooks.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            C = int(f.readline().rstrip())
            R = int(f.readline().rstrip())
            XP = []
            for i in range(0, int(f.readline())):
                XP.append(int(f.readline().rstrip()))
            XP = tuple(XP)
            YP = []
            for i in range(0, int(f.readline())):
                YP.append(int(f.readline().rstrip()))
            YP = tuple(YP)
            ZP = []
            for i in range(0, int(f.readline())):
                ZP.append(int(f.readline().rstrip()))
            ZP = tuple(ZP)
            seed = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(C, R, XP, YP, ZP, seed, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1620492921
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
