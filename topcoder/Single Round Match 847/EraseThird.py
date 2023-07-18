# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class EraseThird:
    def erase(self, S):
        def f(s, q):
            import math
            for x in q:
                l = math.ceil(len(s) / 3)
                a = s[:l]
                b = s[l:-l]
                c = s[-l:]
                # print(">", a,b,c)
                if x == "1":
                    s = b + c
                if x == "2":
                    s = a + c
                if x == "3":
                    s = a + b
                # print("<", s)
            return (s)

        def g(s, q):
            import math
            pos = s.find(q)
            if pos == -1: return "NO"
            l = len(s)
            ans = []
            cnt = 0
            while (l > 1):
                cnt += 1
                if cnt == 10: break
                cut = math.ceil(l / 3)
                a = cut
                b = max(l - cut - cut, 0)
                c = cut
                # print(a,b,c, cut, pos, l, ans)
                # print("?", 0, pos, a, a, pos , a+b, a+c, pos , a+b+c)
                if 0 <= pos < a:  # inc a
                    ans.append(3)
                    l = a + b  # cut c
                    pos = pos
                elif a <= pos < a + b and b != 0:  # inc b
                    ans.append(3)
                    l = a + b  # cut c
                    pos = pos
                elif a + b <= pos < a + b + c:  # inc c
                    ans.append(1)  # cut a
                    l = b + c
                    pos -= a
                else:
                    assert False
            return "".join(list(map(str, ans)))

        s = "akira"
        list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans = []
        for ch in list_lower:
            x = g(S, ch)
            ans.append(x)

        return tuple(ans)

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

def do_test(S, __expected):
    startTime = time.time()
    instance = EraseThird()
    exception = None
    try:
        __result = instance.erase(S);
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
    sys.stdout.write("EraseThird (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("EraseThird.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            S = f.readline().rstrip()
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(f.readline().rstrip())
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(S, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1687483213
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
