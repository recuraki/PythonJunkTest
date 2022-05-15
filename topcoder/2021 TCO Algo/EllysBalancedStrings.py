# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class EllysBalancedStrings:
    def getMin(self, s):
        vowels = {'A', 'E', 'I', 'O', 'U'}
        vowelslist = ['A', 'E', 'I', 'O', 'U']
        vowelsnum = []
        for x in vowelslist:
            vowelsnum.append(ord(x))

        numcons = 0
        numvow = 0
        datcons = []
        datvow = []
        n = len(s)
        for i in range(n):
            if s[i] in vowels:
                numvow += 1
                datvow.append(s[i])
            else:
                numcons += 1
                datcons.append(s[i])
        #print(numvow, numcons, datvow, datcons)
        if numvow == numcons:
            return 0
        if numcons < numvow:
            return (numvow - numcons) / 2
        dat = []
        # numcons < numvow
        for x in datcons:
            res = 1000
            for y in vowelsnum:
                res = min(res, abs(ord(x) - y))
            dat.append(res)
        dat.sort()
        #print("--", dat)
        res = 0
        for i in range((numcons - numvow) / 2):
            res += dat[i]
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

def do_test(S, __expected):
    startTime = time.time()
    instance = EllysBalancedStrings()
    exception = None
    try:
        __result = instance.getMin(S);
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
    sys.stdout.write("EllysBalancedStrings (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EllysBalancedStrings.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            S = f.readline().rstrip()
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(S, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1618675519
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
