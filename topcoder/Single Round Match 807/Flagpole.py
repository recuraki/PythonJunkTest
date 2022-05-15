# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Flagpole:
    def build(self, dat, low, high):
        dat = list(dat)
        dat.sort(reverse=True)
        print(dat)
        def f(x):
            n = bin(x)[2:]
            n = n.zfill(len(dat))
            res = 0
            for i in range(len(dat)):
                if n[i] == "1":
                    res += dat[i]
            return res
        l = 0
        h = 2 ** len(dat) - 1

        # まず下を決める
        while l <= h:
            mid = (l + h) // 2
            if low < f(mid) :  # もじ、midより大きいなら
                h = mid - 1  # もっとしたが行ける
            else:  # midより小さい場合
                l = mid + 1  # もっと上
        if low < f(l):
            lownum = l
        elif low < f(h):
            lownum = h
        else:
            assert False

        # まず上を決める
        l = 0
        h = 2 ** len(dat) - 1
        while l <= h:
            mid = (l + h) // 2
            if high <= f(mid) :  # 大きすぎる場合、
                h = mid - 1  # もっとしたが行ける
            else:  # midより小さい場合
                l = mid + 1  # もっと上
        if f(h) <= high:
            highnum = h
        elif f(l) <= high:
            highnum = l
        else:
            assert False

        for i in range(2**len(dat)):
            print(i, f(i))
        print(lownum, highnum)
        print(dat, low, high)
        print(bin(lownum))
        print(bin(highnum))
        return (highnum - lownum + 1)



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

def do_test(segments, LO, HI, __expected):
    startTime = time.time()
    instance = Flagpole()
    exception = None
    try:
        __result = instance.build(segments, LO, HI);
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
    sys.stdout.write("Flagpole (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Flagpole.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            segments = []
            for i in range(0, int(f.readline())):
                segments.append(int(f.readline().rstrip()))
            segments = tuple(segments)
            LO = int(f.readline().rstrip())
            HI = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(segments, LO, HI, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1623238035
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
