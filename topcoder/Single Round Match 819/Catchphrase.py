# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Catchphrase:
    def reconstruct(self, Ascore, Bscore):
        ans = -1
        for ok1a in range(10):
            for ok1b in range(10):
                if (ok1a + ok1b) > 9: break
                for ok2a in range(10):
                    for ok2b in range(10):
                        if (ok2a + ok2b) > 9: break
                        for bounus1 in range(2):
                            for bounus2 in range(2):
                                predictA = 100 * ok1a + 200 * ok2a
                                predictB = 100 * ok2a + 200 * ok2b
                                if bounus1 == 0:
                                    predictA += 500
                                else:
                                    predictB += 500
                                if bounus2 == 0:
                                    predictA += 1000
                                else:
                                    predictB += 1000
                                nokoriA = Ascore - predictA
                                nokoriB = Bscore - predictB
                                if nokoriA < 0: continue
                                if nokoriB < 0: continue
                                if nokoriA % 500 != 0: continue
                                if nokoriB % 500 != 0: continue
                                tmp = ok1a + ok2a + (nokoriA // 500)
                                if bounus1 == 0: tmp += 1
                                if bounus2 == 0: tmp += 1
                                ans = max(ans, tmp)
        return ans


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

def do_test(Ascore, Bscore, __expected):
    startTime = time.time()
    instance = Catchphrase()
    exception = None
    try:
        __result = instance.reconstruct(Ascore, Bscore);
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
    sys.stdout.write("Catchphrase (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Catchphrase.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            Ascore = int(f.readline().rstrip())
            Bscore = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(Ascore, Bscore, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1638552018
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
