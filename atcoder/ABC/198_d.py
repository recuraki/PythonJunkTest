import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys

    N = 128
    s = "0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ"
    word = [['' for i in range(N)] for j in range(128)]
    digit = [0 for i in range(len(s))]
    l = [0 for i in range(len(s))]
    ok = [False for i in range(10)]
    ll = [0, 0]
    carry = 0
    solution = 0
    issolve = [False]

    def found():
        solution = 1
        issolve[0] = True
        for i in range(imax):
            for j in range(jmax):
                k = jmax - 1 - j
                c = word[i][k]
                if (c == ''):
                    pass
                    print(" ", end="")
                else:
                    print("%d" % digit[s.index(c)], end='')
            print("")
        sys.exit(0)

    def tr(sum):
        w = word[ll[0]][ll[1]]
        c = 0 if w == '' else s.index(w)
        if (ll[0] < imax - 1):
            ll[0] += 1
            d = digit[c]
            if (d < 0):
                d = l[c]
                while (d <= 9):
                    if (ok[d]):
                        digit[c] = d
                        ok[d] = False
                        tr(sum + d)
                        ok[d] = True
                    d += 1
                digit[c] = -1
            else:
                tr(sum + d)
            ll[0] -= 1
        else:
            ll[1] += 1
            ll[0] = 0
            carry, d = divmod(sum, 10)
            if (digit[c] == d):
                if (ll[1] < jmax):
                    tr(carry)
                elif (carry == 0):
                    found()
                    return True
            else:
                if (digit[c] < 0 and ok[d] and d >= l[c]):
                    digit[c] = d
                    ok[d] = False
                    if (ll[1] < jmax):
                        tr(carry)
                    elif (carry == 0):
                        found()
                        return True
                    digit[c] = -1
                    ok[d] = True
            ll[1] -= 1
            ll[0] = imax - 1
            return False

    sss = input().upper().strip()
    ttt = input().upper().strip()
    qqq = input().upper().strip()

    argv = [sss, ttt, qqq]
    imax = 3
    jmax = max(map(len, argv))

    for i in range(imax):
        argv[i] = argv[i].upper()
        l[s.index(argv[i][0])] = 1
        a = argv[i][-1::-1]
        for j in range(len(a)):
            word[i][j] = a[j]
            c = word[i][j]
            if (c.isalpha()):
                digit[s.index(c)] = -1
            elif (c.isdigit()):
                digit[s.index(c)] = int(c)
            else:
                print("Invalid parameter.")
                exit(1)

    for i in range(10):
        ok[i] = True
    tr(0)
    if issolve[0] is False:
        print("UNSOLVABLE")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """a
b
c"""
        output = """1
2
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """x
x
y"""
        output = """1
1
2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """p
q
p"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """abcd
efgh
ijkl"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()