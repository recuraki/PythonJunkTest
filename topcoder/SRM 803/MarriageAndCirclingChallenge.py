# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class MarriageAndCirclingChallenge:
    state = 0

    def rnd(self):
        self.state = (self.state * 1103515245 + 12345) % (1 << 31)
        return self.state % 100

    def solve(self, N, threshold, state):
        self.state = state
        e = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if self.rnd() < threshold:
                    e[i].append(j)
                else:
                    e[j].append(i)
        canReach = [set()] * (N+1)

        for i in range(N-1, -1, -1):
            for x in e[i]:
                if x < i:
                    canReach[i].add(x)
                else:
                    canReach[i] |= canReach[x]

        finalres = 0
        for start in range(N):
            dp = [[0] * 4 for _ in range(N)]
            dp[start][0] = 1
            for cnt in range(4):
                for i in range(start, N):
                    if dp[i][cnt] == 0:
                        continue
                    for next in e[i]:
                        if (next == start) and cnt == 3:
                            finalres += dp[i][cnt]
                        elif cnt < 3:
                            dp[next][cnt + 1] += dp[i][cnt]
        return finalres

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

def do_test(N, threshold, state, __expected):
    startTime = time.time()
    instance = MarriageAndCirclingChallenge()
    exception = None
    try:
        __result = instance.solve(N, threshold, state);
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
    sys.stdout.write("MarriageAndCirclingChallenge (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MarriageAndCirclingChallenge.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            threshold = int(f.readline().rstrip())
            state = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, threshold, state, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1617231842
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
