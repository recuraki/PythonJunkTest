# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class FilmSort:
    def sort(self, reels):
        reels = list(reels)
        res = []
        rind = len(reels) - 1
        for i in range(1, len(reels) - 1):
            print(i, reels, res)
            if reels[0] != 0:
                print("zero")
                ind = reels.index(0)
                res.append(0)
                reels[ind], reels[0] = -reels[0], 0
            print(i, reels, res)
            if reels[i] == i:
                print("ok")
                continue
            if reels[i] == -i:
                print(i)
                print()r
                continue
            if -i in reels:
                print("inv")
                ind = reels.index(-i)
                res.append(ind)
                reels[ind], reels[i] = -reels[i], i
                continue
            # i in reels
            print("plus")
            ind = reels.index(i)
            res.append(ind)
            res.append(i)
            res.append(0)
            reels[ind], reels[i] = -reels[i], i

        if reels[0] == -rind:
            res.append(0)
            ind = reels.index(0)
            reels[0], reels[ind] = 0, -reels[0]




        print(res)
        can = True
        for i in range(len(reels)):
            if i != reels[i]:
                can = False
        if can:
            return tuple(res)
        else:
            return tuple([-1])

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

def do_test(reels, __expected):
    startTime = time.time()
    instance = FilmSort()
    exception = None
    try:
        __result = instance.sort(reels);
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
    sys.stdout.write("FilmSort (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("FilmSort.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            reels = []
            for i in range(0, int(f.readline())):
                reels.append(int(f.readline().rstrip()))
            reels = tuple(reels)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(reels, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1602074004
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
