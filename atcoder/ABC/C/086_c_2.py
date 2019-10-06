import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    t = 0
    res = True
    x, y = 0, 0
    for i in range(n):
        t2, x2, y2 = map(int, input().split())
        dt = t2 - t
        #print("cur {0} {1} {2}".format(t, x, y))
        #print("d {0} {1} {2}".format(dt, x2, y2))
        #print("ju {0} {1} {2} {3}".format(abs(x-x2) + abs(y-y2), dt, (abs(x-x2) + abs(y-y2) - dt) % 2, 1))

        if abs(x-x2) + abs(y-y2) > dt or (abs(x-x2) + abs(y-y2) - dt) % 2 == 1:
            res = False
        t, x, y = t2, x2, y2
    print("Yes" if res else "No")

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
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()