# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class AddFlowers:
    def add(self, indat):
        from pprint import pprint
        ans = []
        for l in indat: ans.append(list(l))
        #print(ans)
        oh = len(indat)
        ow = len(indat[0])
        dh = [1, 0, 0, -1]
        dw = [0, 1, -1, 0]
        used = 0
        #print("--")
        #print(ans)
        #print("--")
        for h in range(oh):
            for w in range(ow):
                cnt = 0
                if ans[h][w] != "F": continue
                #print(">")
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    if ans[nh][nw] == "F":
                        #print("- ", nh, nw, ans[nh][nw])
                        cnt += 1

                #print(h, w, cnt)
                if cnt >= 2: continue
                #print("! need")
                used += 1
                can = False
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    if ans[nh][nw] == ".":
                        ans[nh][nw] = "F"
                        #print("fill", nh, nw)
                        can = True
                        cnt += 1
                        if cnt >= 2: break
                if can is False: assert False

        for h in range(oh-1, -1, -1):
            for w in range(ow-1, -1, -1):
                cnt = 0
                if ans[h][w] != "F": continue
                #print(">")
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    if ans[nh][nw] == "F":
                        #print("- ", nh, nw, ans[nh][nw])
                        cnt += 1

                #print(h, w, cnt)
                if cnt >= 2: continue
                #print("! need")
                used += 1
                can = False
                for di in range(len(dh)):
                    nh = h + dh[di]
                    nw = w + dw[di]
                    if not (0 <= nh < oh): continue
                    if not (0 <= nw < ow): continue
                    if ans[nh][nw] == ".":
                        ans[nh][nw] = "F"
                        #print("fill", nh, nw)
                        can = True
                        cnt += 1
                        if cnt >= 2: break
                if can is False: assert False


        #pprint(ans)
        #print(used)
        ans2 = []
        for l in ans:
            ans2.append("".join(l))
        #print()
        ans2 = tuple(ans2)
        #print("--")
        print()
        #for l in indat: print(l)
        #print("--")
        #for l in ans2: print(l)
        #print(used)
        return tuple(ans2)





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

def do_test(lawn, __expected):
    startTime = time.time()
    instance = AddFlowers()
    exception = None
    try:
        __result = instance.add(lawn);
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
    sys.stdout.write("AddFlowers (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("AddFlowers.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            lawn = []
            for i in range(0, int(f.readline())):
                lawn.append(f.readline().rstrip())
            lawn = tuple(lawn)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(f.readline().rstrip())
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(lawn, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1654081503
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
