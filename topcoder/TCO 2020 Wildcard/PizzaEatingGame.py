# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PizzaEatingGame:

    def eat(self, olives):
        cache = dict()

        def score(seg, turn):
            ls = len(seg)
            maxval = 0

            if turn == 0:
                if len(seg) == 0:
                    return 0
                if len(seg) == 1:
                    return seg[0]
                if len(seg) == 2:
                    return max(seg)
                s = map(str, seg)
                s = ",".join(s)
                if s in cache:
                    return cache[s]
                for i in range(ls):
                    maxval = max(maxval, seg[i] + score(seg[:i], 1) + score(seg[i + 1:], 1))
                cache[s] = maxval
                return maxval

            elif turn == 1:
                if len(seg) == 0:
                    return 0
                if len(seg) == 1:
                    return 0
                if len(seg) == 2:
                    return min(seg)
                return (sum(seg) - score(seg, 0))

        l = list(olives)
        return score(l, 0)

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

def do_test(olives, __expected):
    startTime = time.time()
    instance = PizzaEatingGame()
    exception = None
    try:
        __result = instance.eat(olives);
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
    sys.stdout.write("PizzaEatingGame (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PizzaEatingGame.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            olives = []
            for i in range(0, int(f.readline())):
                olives.append(int(f.readline().rstrip()))
            olives = tuple(olives)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(olives, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1602083102
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
