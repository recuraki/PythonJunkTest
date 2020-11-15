# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TwoRobots:
    def move(self, plan):
        from copy import deepcopy
        from collections import deque
        h = len(plan)
        w = len(plan[0])
        maze = []
        for i in range(h):
            l = list(plan[i])
            maze.append(l)

        dh = [0, 1, 0, -1]
        dw = [-1,0, 1,  0]
        def solve(maze, s, g):
            sh, sw = s[0], s[1]
            gh, gw = g[0], g[1]
            q = deque([])
            l = [ [sh, sw] ]
            q.append([sh, sw, 0, l ])
            clear = False
            maze[sh][sw] = 0
            clearstep = -1
            while True:
                #print("cnt", q)
                if len(q) == 0:
                    print("!!!!!!!!!!!!!!!!!!")
                    return -1
                curh, curw, cnt, route = q.popleft()
                #print(route)
                for d in range(len(dh)):
                    nh, nw = curh + dh[d], curw + dw[d]
                    #print("next", nh, nw, 0, h-1)
                    if nh < 0 or h-1 < nh:
                        #print("ng1")
                        continue
                    if nw < 0 or w-1 < nw:
                        #print("ng2")
                        continue
                    #print("gogo")
                    if maze[nh][nw] == ".":
                        #print("can")
                        maze[nh][nw] = cnt + 1
                        newroute = deepcopy(route)
                        newroute.append([nh, nw])
                        q.appendleft([nh, nw, cnt + 1, newroute])
                    if nh == gh and nw == gw:
                        clear = True
                        clearstep = cnt + 1
                if clear:
                    break
            step =[]

            #print(maze)
            #print(newroute)
            #print(clearstep)
            return ([clearstep, newroute])

        def solvefree(maze, s):
            curh, curw = s[0], s[1]
            res = 0
            for d in range(len(dh)):
                nh, nw = curh + dh[d], curw + dw[d]
                #print("next", nh, nw, 0, h-1)
                if nh < 0 or h-1 < nh:
                    #print("ng1")
                    continue
                if nw < 0 or w-1 < nw:
                    #print("ng2")
                    continue
                #print("gogo")
                if maze[nh][nw] == ".":
                    res += 1
            return res

        sah = saw = gah = gaw = sbh = sbw = gbh = gbw = None
        for hh in range(h):
            for jj in range(w):
                if maze[hh][jj] == "A":
                    sah, saw = [hh, jj]
                if maze[hh][jj] == "a":
                    gah, gaw = [hh, jj]
                if maze[hh][jj] == "B":
                    sbh, sbw = [hh, jj]
                if maze[hh][jj] == "b":
                    gbh, gbw = [hh, jj]
        # turn a
        newmaze = deepcopy(maze)
        newmaze[sbh][sbw] = "."
        newmaze[gbh][gbw] = "."
        newmaze[sah][saw] = "."
        newmaze[gah][gaw] = "."
        stepa, routea = solve(newmaze, [sah, saw], [gah, gaw])
        print(stepa, routea)
        newmaze = deepcopy(maze)
        newmaze[sbh][sbw] = "."
        newmaze[gbh][gbw] = "."
        newmaze[sah][saw] = "."
        newmaze[gah][gaw] = "."
        stepb, routeb = solve(newmaze, [sbh, sbw], [gbh, gbw])
        if stepa > stepb:
            stepa, routea, stepb, routeb = stepb, routeb,stepa, routea

        print(stepb, routeb)
        if abs(stepa - stepb) % 2 == 1:
            return -1
        res = max(stepa, stepb)
        for i in range(min(stepa, stepb) + 1):
            if routea[i] == routeb[i]:
                if i == 1:
                    if solvefree(maze, [sah,saw]) != 1:
                        break
                    elif solvefree(maze, [sbh, sbw]) == 1:
                        return -1
                    else:
                        res += 2

        dh = dh[::-1]
        dw = dw[::-1]

        sah = saw = gah = gaw = sbh = sbw = gbh = gbw = None
        for hh in range(h):
            for jj in range(w):
                if maze[hh][jj] == "A":
                    sah, saw = [hh, jj]
                if maze[hh][jj] == "a":
                    gah, gaw = [hh, jj]
                if maze[hh][jj] == "B":
                    sbh, sbw = [hh, jj]
                if maze[hh][jj] == "b":
                    gbh, gbw = [hh, jj]
        # turn a
        newmaze = deepcopy(maze)
        newmaze[sbh][sbw] = "."
        newmaze[gbh][gbw] = "."
        newmaze[sah][saw] = "."
        newmaze[gah][gaw] = "."
        stepa, routea = solve(newmaze, [sah, saw], [gah, gaw])
        print(stepa, routea)
        newmaze = deepcopy(maze)
        newmaze[sbh][sbw] = "."
        newmaze[gbh][gbw] = "."
        newmaze[sah][saw] = "."
        newmaze[gah][gaw] = "."
        stepb, routeb = solve(newmaze, [sbh, sbw], [gbh, gbw])
        if stepa > stepb:
            stepa, routea, stepb, routeb = stepb, routeb, stepa, routea

        print(stepb, routeb)
        if abs(stepa - stepb) % 2 == 1:
            return -1
        for i in range(min(stepa, stepb) + 1):
            if routea[i] == routeb[i]:
                if i == 1:
                    if solvefree(maze, [sah, saw]) != 1:
                        break
                    elif solvefree(maze, [sbh, sbw]) == 1:
                        return -1
                    else:
                        res += 2


        return(res)




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
    instance = TwoRobots()
    exception = None
    try:
        __result = instance.move(plan);
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
    sys.stdout.write("TwoRobots (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TwoRobots.sample", "r") as f:
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

    T = time.time() - 1603452752
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
