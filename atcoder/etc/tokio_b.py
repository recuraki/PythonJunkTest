import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, speedA = map(int, input().split())
    b, speedB = map(int, input().split())
    t = int(input())
    def do():
        if speedB >= speedA:
            print("NO")
            return 0

        d = abs(a - b)
        x = speedA - speedB
        #if d % x != 0:
        #    print("NO")
        #    return 0

        reachTime = d / x
        if reachTime <= t:
            print("YES")
            return 0
        else:
            print("NO")
            return 0
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
        input = """1 2
3 1
3"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2
3 2
3"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 2
3 3
3"""
        output = """NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()