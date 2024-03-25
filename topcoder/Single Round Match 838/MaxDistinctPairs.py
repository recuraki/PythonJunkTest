# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class MaxDistinctPairs:
    def maximize(self, N, partial):
        le = len(partial)
        dat = []
        for cur in list(partial):
            if cur == ".":
                dat.append(-1)
                continue
            dat.append(ord(cur) - ord("A"))
        #print(dat)
        INF = 100000
        dp = [[[INF, None] for _ in range(N)] for _ in range(le)]
        if partial == "": return ""
        # char 0
        if dat[0] == -1:
            for i in range(N): dp[0][i][0] = 0
        else:
            dp[0][dat[0]][0] = 0
        for ind in range(1, le):
            x = dat[ind]
            if x == -1:  # ANY
                for i in range(N):  # ANY ok
                    for p in range(N):  # prev
                        if i == p:
                            newval = dp[ind - 1][p][0] + 1
                        else:
                            newval = dp[ind - 1][p][0]
                        if dp[ind][i][0] > newval:  # update
                            dp[ind][i][0] = newval
                            dp[ind][i][1] = p
            else:  # One update
                i = x
                for p in range(N):  # prev
                    if i == p:
                        newval = dp[ind - 1][p][0] + 1
                    else:
                        newval = dp[ind - 1][p][0]
                    if dp[ind][i][0] > newval:  # update
                        dp[ind][i][0] = newval
                        dp[ind][i][1] = p
        ansbuf = []
        curind = -1
        curcost = INF
        pind = None
        #print("---")
        #print("---")
        last = dp[-1]
        for i in range(N):
            if curcost > last[i][0]:
                curcost = last[i][0]
                curind = i
        pind = dp[-1][curind][1]
        ansbuf = [curind, pind]

        dp.pop()
        for _ in range(le - 2):
            l = dp.pop()
            _, pind = l[pind]
            ansbuf.append(pind)
        #print(ansbuf)
        ansbuf.reverse()
        #print(ansbuf)
        ans = []
        for x in ansbuf:
            if x is None: continue
            ans.append(chr(ord("A") + x))

        #print(ans)
        ret = "".join(ans)
        #print(ret)
        return ret


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

def do_test(N, partial, __expected):
    startTime = time.time()
    instance = MaxDistinctPairs()
    exception = None
    try:
        __result = instance.maximize(N, partial);
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
    sys.stdout.write("MaxDistinctPairs (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MaxDistinctPairs.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            partial = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, partial, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1663686791
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
