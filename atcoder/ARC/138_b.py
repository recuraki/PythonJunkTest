import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        from collections import deque
        def judge(dat, mode=False):
            dat = deque(dat)
            for _ in range(len(dat)):
                if mode is False:  # NOT FLAP
                    if dat[-1] == 0:  # op B
                        dat.pop()
                    elif dat[0] == 0:  # op A
                        mode = not mode
                        dat.popleft()
                    else:
                        return False
                else:  # FLAP MODE
                    if dat[-1] == 1:  # op B
                        dat.pop()
                    elif dat[0] == 1:  # op A
                        mode = not mode
                        dat.popleft()
                    else:
                        return False
            return True
        if judge(dat):
            print("Yes")
        else:
            print("No")


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
        input = """4
0 1 1 0"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 0 0 0"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
0 0 0 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()