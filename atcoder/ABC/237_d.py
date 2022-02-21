import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():





    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        from collections import deque
        n = int(input())
        s = input()
        ans = deque([n])
        #print(s)
        s = list(s)
        s.reverse()
        s = list(s)
        #print(s)
        cur = n
        for x in s:
            cur -= 1
            if x == "L":
                ans.append(cur)
            else:
                ans.appendleft(cur)

        print(" ".join(list(map(str, ans))))

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
LRRLR"""
        output = """1 2 4 5 3 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
LLLLLLL"""
        output = """7 6 5 4 3 2 1 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()