import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    # input = sys.stdin.readline

    from pprint import pprint
    def do():
        oa, ob = map(int, input().split())
        a = oa
        b = ob
        if a % b == 0:
            print("NO")
            return
        x = a * b
        y = a
        z = a * (b+1)
        if x % oa == 0 and x % ob == 0 and y % oa == 0 and y % ob != 0 and z % oa == 0 and z % ob != 0 and x + y == z:
            print("YES")
            print(x, y, z)
            return
        print("NO")
        return

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
        input = """5
5 3
13 2
7 11
8 2
7 1"""
        output = """YES
10 50 60
YES
169 39 208
YES
28 154 182
NO
NO"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
10001 2"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()