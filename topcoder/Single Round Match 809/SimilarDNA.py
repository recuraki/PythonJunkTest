# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def lcs_length(x, y):
    m, n  = len(x), len(y)
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'A'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "B"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "C"
    return c, b

# アルゴリズムイントロダクション 15.4 LCS
# bを基にもともとのinput xから共通部分を抜き出す。
def lcs_decode(b, X, i, j):
    import collections
    res = collections.deque([])
    while True:
        #print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
        if i == 0 or j == 0:
            break
        if b[i][j] == 'A':
            res.appendleft(X[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == "B":
            i -= 1
            continue
        else:
            j -= 1
            continue
    return res

# 適当に実装したけどあってるはず
# lcsした結果から「一致しなかった部分」を取得する
def lcs_decode_negative(b, X, i, j):
    import collections
    res = collections.deque([])
    while True:
        #print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
        if i == 0 or j == 0:
            break
        if b[i][j] == 'A':
            i -= 1
            j -= 1
        elif b[i][j] == "B":
            res.appendleft(X[i-1])
            i -= 1
            continue
        else:
            j -= 1
            continue
    if i != 0:
        for i in range(1,i+1):
            res.appendleft(X[i-1])
    return res

def lcs_print_recurcive(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 'A':
        lcs_decode(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] == "B":
        lcs_decode(b, X, i - 1, j)
    else:
        lcs_decode(b, X, i, j - 1)


class SimilarDNA:
    def areSimilar(self, a, b):
        if len(b) > len(a):
            a, b = b, a
        cc, bb = lcs_length(a, b)
        same = lcs_decode(bb, a, len(a), len(b))
        samelen = len(same)
        #print(cc)
        #print("len ", samelen)
        if (len(a) - samelen) <= 2:
            return "similar"
        else:
            return "distinct"

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

def do_test(A, B, __expected):
    startTime = time.time()
    instance = SimilarDNA()
    exception = None
    try:
        __result = instance.areSimilar(A, B);
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
    sys.stdout.write("SimilarDNA (400 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SimilarDNA.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = f.readline().rstrip()
            B = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1626174876
    PT, TT = (T / 60.0, 75.0)
    points = 400 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
