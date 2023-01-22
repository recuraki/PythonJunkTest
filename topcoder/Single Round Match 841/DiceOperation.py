# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


class DiceOperation:
    def solve(self, dice):
        def calc1(x):
            dat = [0] * 64
            buf = [0] * 64
            for i in range(64):
                val = x + 1
                turn = 2 ** i
                turn *= 2
                c = (val // turn) * (2 ** i)
                amari = (val % turn) - (2 ** i)
                if amari >= 0: c += amari
                buf[i] = c
            return (buf)


        from fractions import Fraction
        dp = [[0] * 2 for _ in range(64)]
        for i in range(64):
            # init all = int
            dp[i][0] = 1
            dp[i][1] = 0

        all = 0
        for ind in range(len(dice)): # x = me
            newdp = [[0] * 2 for _ in range(64)]
            x = dice[ind]
            all += x
            cnt1 = calc1(x)
            cnt0 = []
            for a in cnt1: cnt0.append(x - a)
            #print(x, cnt1)
            #print(x, cnt0)
            for i in range(64):
                p0 = Fraction(cnt0[i], x)
                p1 = Fraction(cnt1[i], x)
                newdp[i][0] += dp[i][0] * p0
                newdp[i][0] += dp[i][1] * p1
                newdp[i][1] += dp[i][0] * p1
                newdp[i][1] += dp[i][1] * p0
            dp = newdp
        ans = 0
        #print(dp)
        for i in range(64):
            ans += dp[i][1] * (2**i)
            #print("i", i, dp[i][0], dp[i][1], float(dp[i][1] * (2**i)))
        return (float(ans))

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

def do_test(dice, __expected):
    startTime = time.time()
    instance = DiceOperation()
    exception = None
    try:
        __result = instance.solve(dice);
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
    sys.stdout.write("DiceOperation (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DiceOperation.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            dice = []
            for i in range(0, int(f.readline())):
                dice.append(int(f.readline().rstrip()))
            dice = tuple(dice)
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(dice, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1667909102
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
