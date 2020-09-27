# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SquareCityWalking:
    def largestGCD(self, n, a):
        from fractions import gcd
        dat = []
        maze = []
        for i in range(n):
            l = []
            for j in range(n):
                l.append([])
            dat.append(l)
            l = [None] * n
            maze.append(l)
        for i in range(n):
            for j in range(n):
                maze[i][j] = a[n*i + j]
        #print(dat)
        #print(maze)
        dx = [1, 0]
        dy = [0, 1]

        dat[0][0] = [a[0]]
        for i in range(n): # y
            for j in range(n): # x
                #print("j, i", j, i)
                #print("dat", dat)
                for d in range(len(dx)):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if ny >= n or nx >= n: # over
                        #print(">cannot", nx, ny)
                        continue
                    #print(" > ny,nx", ny, nx)
                    for curval in dat[i][j]:
                        v = gcd(curval, maze[ny][nx])
                        #print("  > v, curval,  mazenum ", v, curval,  maze[ny][nx])
                        if v not in dat[ny][nx]:
                            dat[ny][nx].append(v)
                            #print("  > insert to ", ny, nx)
        #print(maze)
        #print(dat)
        return max(dat[n-1][n-1])






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

def do_test(N, A, __expected):
    startTime = time.time()
    instance = SquareCityWalking()
    exception = None
    try:
        __result = instance.largestGCD(N, A);
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
    sys.stdout.write("SquareCityWalking (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SquareCityWalking.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            A = []
            for i in range(0, int(f.readline())):
                A.append(int(f.readline().rstrip()))
            A = tuple(A)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, A, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1595589933
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
