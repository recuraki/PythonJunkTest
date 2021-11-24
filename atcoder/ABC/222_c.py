import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def do():
        import math
        n, m = map(int, input().split())
        hands = []

        def f(x, y):
            #print(x, y)
            if x == 'G':
                if y == 'G':
                    return 0
                if y == 'C':
                    return 1
                if y == 'P':
                    return -1
            if x == 'C':
                if y == 'G':
                    return -1
                if y == 'C':
                    return 0
                if y == 'P':
                    return 1
            if x == 'P':
                if y == 'G':
                    return 1
                if y == 'C':
                    return -1
                if y == 'P':
                    return 0
            #print("!!!")
            return

        for i in range(2 * n):
            s = input()
            hands.append(list(s))
        #print(hands)
        # win, number(0-orig]
        dat = []
        for i in range(2 * n):
            dat.append([0, i + 1])
        # print(dat)
        for turn in range(m):
            dat.sort(key=lambda x: (-x[0], x[1]))
            #print("truen", turn, dat)
            for i in range(n):
                xperson = dat[2 * i][1] - 1
                yperson = dat[2 * i + 1][1] - 1
                # print("!!", xperson, yperson, turn)
                # print(dat[xperson], dat[yperson])
                xhand = hands[xperson][turn]
                yhand = hands[yperson][turn]
                bat = f(xhand, yhand)
                #print("bat", xperson + 1, yperson + 1, bat)
                if bat == 1:
                    dat[2 * i][0] += 1
                elif bat == 0:
                    pass
                elif bat == -1:
                    dat[2 * i + 1][0] += 1
                #print("after", dat)
        dat.sort(key=lambda x: (-x[0], x[1]))
        for i in range(2 * n):
            print(dat[i][1])

    do()


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
        input = """2 3
GCP
PPP
CCC
PPC"""
        output = """3
1
2
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2
GC
PG
CG
PP"""
        output = """1
2
3
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()