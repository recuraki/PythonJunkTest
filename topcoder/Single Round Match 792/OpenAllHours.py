# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class OpenAllHours:
    def verify(self, N, openingTime, closingTime):
        check = [False] * (24*60)
        print(len(check))
        for i in range(N):
            so, sc = openingTime[i], closingTime[i]
            h, m = map(int, so.split(":"))
            to = h * 60 + m
            h, m = map(int, sc.split(":"))
            tc = h * 60 + m
            if to <=  tc: # 0100 - 0300
                for j in range(to, tc):
                    check[j] = True
            else:  # 0300 - 0100
                for j in range(to, 24*60):
                    check[j] = True
                for j in range(0, tc):
                    check[j] = True
        can = True
        for i in range(24*60):
            if check[i] is False:
                can = False
                break
        return ("correct" if can else "incorrect")






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

def do_test(N, openingTime, closingTime, __expected):
    startTime = time.time()
    instance = OpenAllHours()
    exception = None
    try:
        __result = instance.verify(N, openingTime, closingTime);
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
    sys.stdout.write("OpenAllHours (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("OpenAllHours.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            openingTime = []
            for i in range(0, int(f.readline())):
                openingTime.append(f.readline().rstrip())
            openingTime = tuple(openingTime)
            closingTime = []
            for i in range(0, int(f.readline())):
                closingTime.append(f.readline().rstrip())
            closingTime = tuple(closingTime)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, openingTime, closingTime, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1603450801
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
