# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class RearrangeAndIncrement:
    def change(self, x, y):
        def f(x, y):
            dat = [x]
            while len(str(y)) > len(str(x)):
                if x % 10 == 1:
                    x += 9
                    dat.append(x)
                elif x % 10 == 0:
                    x += 9
                    dat.append(x)
                elif x % 10 == 9:
                    s = str(x)
                    x = int(s[-1] + s[:-1])
                    dat.append(x)
                else:
                    assert False
            # same keta
            keta = len(str(x))
            if x == y: return dat
            if (x + 11) >= y:
                can = min(13, y - x)
                x += can
                dat.append(x)
                return (dat)
            offset = False
            if y % 10 == 0:
                y -= 1
                offset = True
            first = True
            for i in range(keta - 2):
                target = int(str(y)[i])
                for _ in range(target):
                    x += 10
                    dat.append(x)
                x = list(str(x))
                x[i], x[-2] = x[-2], x[i]
                x = int("".join(x))
                dat.append(x)
                if first:
                    x = list(str(x))
                    x[-1], x[-2] = x[-2], x[-1]
                    x = int("".join(x))
                    dat.append(x)
                    first = False
            print(x, y)
            if offset:
                y += 1
            print(x, y)
            if (x + 11) >= y:
                can = min(13, y - x)
                x += can
                dat.append(x)
                return (dat)
            x = list(str(x))
            x[-1], x[-2] = x[-2], x[-1]
            x = int("".join(x))
            dat.append(x)
            while x < y:
                can = min(13, y - x)
                x += can
                dat.append(x)
            return (dat)

        def g(x):
            dat = [x]
            while x > 1 and x != 0:
                if x % 10 != 0:
                    x += 10 - x % 10
                    dat.append(x)
                x = list(str(x))
                x = [x[-1]] + x[:-1]
                x = int("".join(x))
                dat.append(x)
            if x == 0: dat.append(1)
            return dat

        ans = g(x)
        ans += f(1, y)
        return(tuple(ans))


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

def do_test(X, Y, __expected):
    startTime = time.time()
    instance = RearrangeAndIncrement()
    exception = None
    try:
        __result = instance.change(X, Y);
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
    sys.stdout.write("RearrangeAndIncrement (700 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("RearrangeAndIncrement.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            X = int(f.readline().rstrip())
            Y = int(f.readline().rstrip())
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(X, Y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1653996994
    PT, TT = (T / 60.0, 75.0)
    points = 700 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
