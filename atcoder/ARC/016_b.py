import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    state = [0] * 9
    res = 0
    for _ in range(n):
        #print(state)
        s = input()
        res += s.count("x")
        for i in range(9):
            if state[i] == 0 and s[i] == "o":
                #print("nagaoshi")
                state[i] = 1
                res += 1
            elif state[i] == 1 and s[i] != "o":
                state[i] = 0
    print(res)

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
        input = """15
.........
.x.......
.........
...x.....
.........
.......o.
.......o.
.......o.
.........
..x.....o
........o
........o
....x...o
.x......o
........o"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
..o..x.o.
..o..x.o.
..x..o.o.
..o..o.o.
..o..x.o.
..o..x.o."""
        output = """9"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
.........
........."""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()