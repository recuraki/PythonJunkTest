# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class StepLeapSurviveTraps:
    def minDamage(self, n, j, seed, mod):

        from heapq import heappop, heappush, heapify
        from collections import defaultdict
        class exhanceHeapq():
            containDict = defaultdict(int)
            willdeleteDict = defaultdict(int)
            willdeletelen = 0
            def __init__(self, initlist=[]):
                self.q = initlist
                heapify(initlist, )
                for x in initlist: self.containDict[x] += 1

            def pop(self):
                while len(self.q) > 0:
                    candidate = heappop(self.q)
                    assert self.willdeleteDict[candidate] >= 0
                    self.containDict[candidate] -= 1
                    if self.willdeleteDict[candidate] > 0:
                        self.willdeletelen -= 1
                        self.willdeleteDict[candidate] -= 1
                    else:
                        return candidate
                assert False  # NOT REACH

            def push(self, x):
                heappush(self.q, x)
                self.containDict[x] += 1

            def len(self):
                return len(self.q) - self.willdeletelen

            def erase(self, x):
                assert self.containDict[x] > 0
                self.willdeletelen += 1  # will delete
                self.willdeleteDict[x] += 1
        INF = 2 ** 61
        t = [None] * (n+1)
        t[0] = 0
        state = seed
        k = 2 ** 31
        for i in range(1, n + 1):
            state = (state * 1103515245 + 12345) % k
            t[i] = 1 + (state % mod)
        #print(t)
        mn = collections.deque()
        mn.append( (0,0))
        dp = [0] + [INF]*n
        for i, t in enumerate(t[1:], 1):
            while mn[0][0] < i-j: mn.popleft()
            dp[i] = mn[0][1] + t
            while mn and mn[-1][-1] >= dp[i]: mn.pop()
            mn.append( (i, dp[i]))
        return dp[n]



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

def do_test(N, J, seed, M, __expected):
    startTime = time.time()
    instance = StepLeapSurviveTraps()
    exception = None
    try:
        __result = instance.minDamage(N, J, seed, M);
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
    sys.stdout.write("StepLeapSurviveTraps (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("StepLeapSurviveTraps.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            J = int(f.readline().rstrip())
            seed = int(f.readline().rstrip())
            M = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, J, seed, M, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1632963904
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
