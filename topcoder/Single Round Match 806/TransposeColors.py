# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TransposeColors:
    def move(self, n):
        if n == 1:
            return ()
        maze = []
        collect = [[] for _ in range(n)]
        for i in range(n):
            l = [i] * n
            l = list(l)
            maze.append(l)
            for j in range(n):
                collect[j].append(i)

        def t(x):
            c = x % n
            r = x // n
            return r, c

        wantto = ""
        buffer = ""
        p = [-1, -1]

        def first(x):
            global buffer, wantto
            r, c = t(x)
            buffer = maze[r][c]

            maze[r][c] = -1
            p[0], p[1] = r, c
            dump()

        def dump():
            return
            #print("-------")
            for l in maze:
                print(l)

        def do(x):
            if x == n ** 2:
                last()
                return
            #print("!!!!!!!!", x)
            r, c = t(x)
            maze[p[0]][p[1]] = maze[r][c]
            maze[r][c] = -1
            p[0], p[1] = r, c
            dump()

        def last():
            global buffer
            # print("-------!!!")
            for l in maze:
                for i in range(len(l)):
                    if l[i] == -1:
                        l[i] = buffer
                # print(l)

        def search():
            for x in range(1, n * n):
                r, c = t(x)
                if maze[r][c] != collect[p[0]][p[1]]:  # ほしい色じゃない
                    continue
                if maze[r][c] == collect[r][c]:  # あるいはそれが正解だったら取っちゃダメ
                    continue
                return x

        def check():
            global buffer
            diff = 0
            for r in range(0, n):
                for c in range(0, n):
                    if collect[r][c] == maze[r][c]:
                        continue
                    diff += 1
                    if diff > 1:
                        return False
                    rr, cc = r, c
            if diff == 1 and buffer == collect[rr][cc]:
                return True
            return False

        res = []
        ########################
        first(n * n - 2)
        res.append(n * n - 2)

        while True:
            x = search()
            res.append(x)
            do(x)
            if check():
                break

        do(n * n)
        res.append(n * n)
        #########################
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

def do_test(N, __expected):
    startTime = time.time()
    instance = TransposeColors()
    exception = None
    try:
        __result = instance.move(N);
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
    sys.stdout.write("TransposeColors (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TransposeColors.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1622041503
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
