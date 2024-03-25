# -*- coding: utf-8 -*-

import math,string,itertools,fractions,heapq,collections,re,array,bisect


class Lasso:
    def lasso(self, R, C, R1, C1, R2, C2):
        vtime = collections.defaultdict(lambda : 10**9)
        q = collections.deque()
        # + 2する。なので、0 のとき、4までように+2する
        R += 4
        C += 4
        R1 += 2
        C1 += 2
        R2 += 2
        C2 += 2
        dr = [-2, -2, -1, -1, 1, 1, 2, 2]
        dc = [-1,  1, -2,  2,-2, 2,-1, 1]
        for r in (0, 1, R-1, R):
            for c in range(0, C):
                if (r,c) in vtime: continue
                vtime[(r, c)] = 0
                q.append( (r, c) )
        for c in (0, 1, C-1, C):
            for r in range(0, R):
                if (r,c) in vtime: continue
                vtime[(r, c)] = 0
                q.append( (r, c) )
        while(len(q) > 0):
            cr, cc = q.popleft()
            for di in range(len(dr)):
                nr = cr + dr[di]
                nc = cc + dc[di]
                if not (0 <= nr < R): continue
                if not (0 <= nc < C): continue
                if (nr,nc) in vtime: continue
                vtime[(nr, nc)] = vtime[(cr, cc)] + 1
                q.append( (nr, nc) )
        cnt = 0
        for r in range(R1, R2+1):
            for c in range(C1, C2 + 1):
                print(r, c, vtime[(r,c)])
                cnt += 1
        print(cnt)









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

def do_test(R, C, R1, C1, R2, C2, __expected):
    startTime = time.time()
    instance = Lasso()
    exception = None
    try:
        __result = instance.lasso(R, C, R1, C1, R2, C2);
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
    sys.stdout.write("Lasso (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Lasso.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            R = int(f.readline().rstrip())
            C = int(f.readline().rstrip())
            R1 = int(f.readline().rstrip())
            C1 = int(f.readline().rstrip())
            R2 = int(f.readline().rstrip())
            C2 = int(f.readline().rstrip())
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(R, C, R1, C1, R2, C2, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1687485273
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
