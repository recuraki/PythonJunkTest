# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class FixedNumberOfDigits:
    def sum(self, start, step, numberOfDigits):
        import math
        x = start
        nokori = numberOfDigits
        while True:
            #print("-----------")
            x = int(x)
            nokori = int(nokori)
            l = len(str(x))
            #print(x, nokori, l)
            diff = 10**(l) - x
            #print("d", diff, step, diff/step)
            count = math.ceil(diff / step) # nanko
            #print("c", count)
            if nokori > (l * count):
                if count == 0:
                    count = 1
                nokori -= (l*count)
                x += (step * count)
                continue
            # else
            #print("c", count)
            #print("count", count, nokori, l)
            ind = (nokori - 1) // l
            res = str(int (x + (ind * step)))

            #print(res, nokori, l)
            if nokori%l == 0:
                return int(res)
            else:
                return int(res[:nokori%l])

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

def do_test(start, step, numberOfDigits, __expected):
    startTime = time.time()
    instance = FixedNumberOfDigits()
    exception = None
    try:
        __result = instance.sum(start, step, numberOfDigits);
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
    sys.stdout.write("FixedNumberOfDigits (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("FixedNumberOfDigits.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            start = int(f.readline().rstrip())
            step = int(f.readline().rstrip())
            numberOfDigits = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(start, step, numberOfDigits, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1595088301
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
