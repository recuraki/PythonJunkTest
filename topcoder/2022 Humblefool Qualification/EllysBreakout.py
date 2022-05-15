# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
from pprint import pprint
class EllysBreakout:
    def getCount(self, plan):
        from collections import deque
        oh = len(plan)
        ow = len(plan[0])
        maze = []
        maze.append(["."] * (ow+2))
        for x in plan:
            x = list(x)
            maze.append(["."] + x + ["."])
        maze.append(["."] * (ow+2))
        oh += 2
        ow += 2
        dh = [-1, 0, 1, 0]
        dw = [0, 1, 0, -1]
        INF = 2**30
        from collections import deque
        q = deque([])
        q.append( (0, 0) )
        cost = [[INF] * ow for _ in range(oh)]
        cost[0][0] = 0
        walked = 1
        curcost = -1
        while True:
            curcost += 1
            #if curcost > 300000: break
            walls = set()
            while len(q) > 0:
                h, w = q.popleft()
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    if cost[nh][nw] != INF: continue
                    ncost = curcost
                    if maze[nh][nw] == "#":
                        ncost += 1
                        cost[nh][nw] = ncost
                        walls.add( (nh, nw) )
                        walked += 1
                    else: #"road"
                        cost[nh][nw] = curcost
                        q.append( (nh, nw) )
                        walked += 1

            q = set()
            for h, w in list(walls):
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    q.add( (nh, nw) )
            q = list(q)
            q = deque(q)
            if walked >= oh * ow: break

        ma = -1
        for h in range(oh-2):
            for w in range(ow-2):
                if plan[h][w] == "#":
                    maze[h+1][w+1] = INF
                else:
                    ma = max(ma, cost[h+1][w+1])

        ans = 0
        for h in range(oh-2):
            for w in range(ow-2):
                if plan[h][w] == "#": continue
                if cost[h+1][w+1] == ma: ans += 1
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

def do_test(plan, __expected):
    startTime = time.time()
    instance = EllysBreakout()
    exception = None
    try:
        __result = instance.getCount(plan);
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
    sys.stdout.write("EllysBreakout (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EllysBreakout.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            plan = []
            for i in range(0, int(f.readline())):
                plan.append(f.readline().rstrip())
            plan = tuple(plan)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(plan, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1647524996
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
