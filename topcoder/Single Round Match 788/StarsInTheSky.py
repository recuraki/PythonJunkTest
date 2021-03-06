# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class StarsInTheSky:
    def countPictures(self, N, x, y):
        res = 0

        for pat in range(1, 2**N):
            x1 = y1 = 10** 9 + 1
            x2 = y2 = -1
            # calc size
            visit = [False] * N
            for i in range(N):
                if ((pat >> i) & 1) == 1:
                    x1 = min(x1, x[i])
                    y1 = min(y1, y[i])
                    x2 = max(x2, x[i])
                    y2 = max(y2, y[i])
                    visit[i] = True
            #print(pat, bin(pat), x1,y1, x2,y2)
            can = True
            for i in range(N):
                if visit[i] is True:
                    continue
                if x1 <= x[i] <= x2 and y1 <= y[i] <= y2:
                    can = False
                    break
            if can is True:
                res += 1
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

def do_test(N, X, Y, __expected):
    startTime = time.time()
    instance = StarsInTheSky()
    exception = None
    try:
        __result = instance.countPictures(N, X, Y);
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
    sys.stdout.write("StarsInTheSky (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("StarsInTheSky.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            X = []
            for i in range(0, int(f.readline())):
                X.append(int(f.readline().rstrip()))
            X = tuple(X)
            Y = []
            for i in range(0, int(f.readline())):
                Y.append(int(f.readline().rstrip()))
            Y = tuple(Y)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, X, Y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1595588975
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
