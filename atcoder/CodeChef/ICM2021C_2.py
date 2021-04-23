import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    from copy import deepcopy
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = list(set(dat))
        buf.sort()
        m = dict()
        for i in range(len(buf)):
            m[buf[i]] = i
        newdat = []
        for x in dat:
            newdat.append(m[x])
        #print(newdat)

        if newdat.count(0) == n:
            print("YES")
            print(0)
            return

        movelast = False
        if newdat[-1] == 0:
            last0 = len(newdat)-1
            while newdat[last0 - 1] == 0:
                last0 -= 1
            newdat = [0] + newdat[:last0]
            movelast = True
            #print("!!!", newdat)

        n = len(newdat)
        #print("!!!>", n, newdat)
        ind = newdat.index(0)

        for i in range(n-1):
            if newdat[(ind+i) % n] > newdat[((ind+i+1)%n)]:
                print("NO")
                return
        if ind == 0 and movelast is False:
            print("YES")
            print(0)
            return
        print("YES")
        print(1)
    q = int(input())
    for _ in range(q):
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
        input = """2
2
1 2
3
2 1 3"""
        output = """YES
0
NO"""
        self.assertIO(input, output)

    def test_input_1c(self):
        print("test_input_1c")
        input = """2
2
10 20
3
20 10 30"""
        output = """YES
0
NO"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
3
3 1 2
5
13 14 15 11 12
4
22 22 11 11
1
100000"""
        output = """YES
1
YES
1
YES
1
YES
0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
6
1 2 3 4 5 1
6
1 1 1 1 1 1
6
1 1 2 1 1 1
6
2 1 1 1 1 1
2
1 2"""
        output = """YES
1
YES
0
YES
1
YES
1
YES
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()