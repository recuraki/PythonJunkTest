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
        buf = [[-1] * 100 for _ in range(100)]
        for i in range(n):
            l = i + 1
            dat = [-1] * l
            buf[i][0] = 1
            buf[i][i] = 1
            for j in range(1, i):
                buf[i][j] = buf[i-1][j-1] + buf[i-1][j]

        for i in range(n):
            print(*buf[i][:i+1])




    # 1 time
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
        input = """3"""
        output = """1
1 1
1 2 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10"""
        output = """1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()