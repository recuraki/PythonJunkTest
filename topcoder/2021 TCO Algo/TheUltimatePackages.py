# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TheUltimatePackages:
    def count(self, N, D, Xprefix, Yprefix, L, seed):
        X = [0] * D
        Y = [0] * D
        XL = len(Xprefix)
        for i in range(XL):
            X[i] = Xprefix[i]
            Y[i] = Yprefix[i]
        state = seed
        for i in range(XL, D):
            state = (state * 1103515245 + 12345) % (2**31)
            elen = 1 + (state % L)
            state = (state * 1103515245 + 12345) % (2**31)
            Y[i] = state % (N - elen)
            X[i] = Y[i] + elen
        print()
        print(X)
        print(Y)
        G = [set() for _ in range(N)]
        res = set()
        for i in range(D):
            x, y = X[i], Y[i]
            G[x].add(y)
            G[y].add(x)
        valMax = [-1] * N
        valMin = [10**9] * N
        for i in range(N):
            valMin[i] = min(valMin[i], i)
            print("i", i, valMin)
            for nextnode in G[i]:
                if nextnode < i:
                    continue # 戻らない
                valMin[nextnode] = min(valMin[nextnode], valMin[i])

        for i in range(N-1, -1, -1):
            valMax[i] = max(valMax[i], i)
            for nextnode in G[i]:
                if nextnode > i:
                    continue # 戻らない
                valMax[nextnode] = max(valMax[nextnode], valMax[i])


        print(valMin)
        print(valMax)




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

def do_test(N, D, Xprefix, Yprefix, L, seed, __expected):
    startTime = time.time()
    instance = TheUltimatePackages()
    exception = None
    try:
        __result = instance.count(N, D, Xprefix, Yprefix, L, seed);
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
    sys.stdout.write("TheUltimatePackages (600 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheUltimatePackages.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            D = int(f.readline().rstrip())
            Xprefix = []
            for i in range(0, int(f.readline())):
                Xprefix.append(int(f.readline().rstrip()))
            Xprefix = tuple(Xprefix)
            Yprefix = []
            for i in range(0, int(f.readline())):
                Yprefix.append(int(f.readline().rstrip()))
            Yprefix = tuple(Yprefix)
            L = int(f.readline().rstrip())
            seed = int(f.readline().rstrip())
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, D, Xprefix, Yprefix, L, seed, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1621700996
    PT, TT = (T / 60.0, 75.0)
    points = 600 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
