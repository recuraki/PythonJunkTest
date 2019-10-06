import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    t = int(input())
    x,y = 0,0
    a = 0
    for i in range(len(s)):
        if s[i] == "U":
            y += 1
        elif s[i] == "D":
            y -= 1
        elif s[i] == "L":
            x -= 1
        elif s[i] == "R":
            x += 1
        else:
            a = a + 1

    if t == 1:
        print(abs(x) + abs(y) + a)
    else:
        d = abs(x) + abs(y) - a
        if d < 0:
            if abs(d) % 2 == 1:
                print(1)
            else:
                print(0)
        else:
            print(d)

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
        input = """UL?
1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """UD?
1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """UUUU?DDR?LLLL
1"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()