# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SmallOccupiedAirplane:
    def seat(self, R, groups):
        nokori = [6] * R
        res = []
        visited = [[False] * 6 for _ in range(R)]
        #print(nokori)
        #print(visited)

        def f():
            for i in range(R):
                if visited[i][0] is False:
                    visited[i][0] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "A")
                    return
                if visited[i][5] is False:
                    visited[i][5] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "F")
                    return
            for i in range(R):
                if visited[i][2] is False:
                    visited[i][2] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "C")
                    return
                if visited[i][3] is False:
                    visited[i][3] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "D")
                    return
            for i in range(R):
                if visited[i][1] is False:
                    visited[i][1] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "B")
                    return
                if visited[i][4] is False:
                    visited[i][4] = True
                    nokori[i] -= 1
                    res.append(str(i+1) + "E")
                    return



        for pernum in groups:
            if pernum == 1:
                f()
                continue
            # Group
            did = False

            for i in range(R):
                if nokori[i] < pernum: continue
                # can!
                did = True
                seated = 0
                for j in range(6):
                    if seated == pernum: break
                    if visited[i][j] is False:
                        visited[i][j] = True
                        nokori[i] -= 1
                        res.append(str(i+1) + chr(ord("A") + j))
                        seated += 1
                break

            if did: continue

            for i in range(pernum):
                f()
        #print(res)
        return tuple(res)

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

def do_test(R, groups, __expected):
    startTime = time.time()
    instance = SmallOccupiedAirplane()
    exception = None
    try:
        __result = instance.seat(R, groups);
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
    sys.stdout.write("SmallOccupiedAirplane (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SmallOccupiedAirplane.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            R = int(f.readline().rstrip())
            groups = []
            for i in range(0, int(f.readline())):
                groups.append(int(f.readline().rstrip()))
            groups = tuple(groups)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(f.readline().rstrip())
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(R, groups, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1634311336
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
