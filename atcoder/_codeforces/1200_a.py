
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    room = [0] * 10
    for i in range(len(s)):
        if s[i] == "L":
            for j in range(10):
                if room[j] == 0:
                    room[j] = 1
                    break
        elif s[i] == "R":
            for j in range(9,-1,-1):
                if room[j] == 0:
                    room[j] = 1
                    break
        else:
            room[int(s[i])] = 0
    res = map(str, room)
    res = list(res)
    print("".join(res))

class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """8
LLRL1RL1"""
        output = """1010000011"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_22")
        input = """9
L0L0LLRR9"""
        output = """1100000010"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()