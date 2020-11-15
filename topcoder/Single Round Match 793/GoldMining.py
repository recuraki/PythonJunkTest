# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class GoldMining:
    def maxProfit(self, goldInGround, miningTime, hiringCost):
        import collections
        q = collections.deque([])
        q.append([goldInGround, miningTime, 0, 1])
        person = 1
        res = -1
        cur = 0
        import math
        while len(q) > 0:
            print(q)
            gremine, mtime, cur, p = q.popleft()
            if gremine < 0 or mtime < 0:
                break
            cangetnow = min(p * mtime, gremine)
            print("!!", cur + cangetnow)
            if cangetnow > hiringCost:
                hireneedtime = math.ceil(hiringCost / p)
                print("--", hireneedtime,hiringCost / p)
                hirereminegold = cur + ((p * hireneedtime) - hiringCost)
                goldremine = gremine - (p * hireneedtime)
                hirereminetime = mtime - hireneedtime
                if not(hirereminetime < 0 or goldremine < 0 or hirereminegold < 0):
                    q.append([goldremine, hirereminetime, hirereminegold, p + 1 ])

            res = max(res, cur + cangetnow)
        print(res)
        return int(res)


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

def do_test(goldInGround, miningTime, hiringCost, __expected):
    startTime = time.time()
    instance = GoldMining()
    exception = None
    try:
        __result = instance.maxProfit(goldInGround, miningTime, hiringCost);
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
    sys.stdout.write("GoldMining (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("GoldMining.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            goldInGround = int(f.readline().rstrip())
            miningTime = int(f.readline().rstrip())
            hiringCost = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(goldInGround, miningTime, hiringCost, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1604544735
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
