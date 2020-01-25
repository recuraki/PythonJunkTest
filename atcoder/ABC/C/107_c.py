import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat_x = list(map(int, input().split()))
    l = 0
    r = k - 1
    total = 0
    for i in range(1, k):
        # print("{0} - {1}".format(dat_x[i] , dat_x[i - 1] ))
        # print("abc: {0}".format(abs(dat_x[i] - dat_x[i - 1])))
        total += abs(dat_x[i] - dat_x[i - 1])

    total += min(abs(dat_x[l]), abs(dat_x[r]))

    m = total
    # print("m = {0}".format(m))

    #print("check: {0}, {1} = {2}".format(l, r, total))
    r += 1
    l += 1

    while r < n:
        #print("!!!!!!!!")
        #print(dat_x[l])
        #print(dat_x[l-1])
        total -= min(abs(dat_x[l-1]), abs(dat_x[r-1]))
        #print("check-0: {0}, {1} = {2}".format(l, r, total))
        total -= abs(dat_x[l] - dat_x[l - 1])
        #print("check-1: {0}, {1} = {2}".format(l, r, total))
        total += abs(dat_x[r] - dat_x[r - 1])
        #print("check-2: {0}, {1} = {2}".format(l, r, total))
        total += min(abs(dat_x[l]), abs(dat_x[r]))

        m = min(m, total)
        r += 1
        l += 1

    print(m)

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
        input = """5 3
-30 -10 10 20 50"""
        output = """40"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
10 20 30"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1
0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8 5
-9 -7 -4 -3 1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()