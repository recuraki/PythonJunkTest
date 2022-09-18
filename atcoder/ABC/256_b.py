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
        ans = 0
        n = int(input())
        dat = list(map(int, input().split()))
        buf = [0] * 4
        for cnt in range(n):
            buf[0] = 1
            #print(buf)
            for i in range(3, -1, -1):
                if buf[i] == 0: continue
                nxt = i + dat[cnt]
                if nxt >= 4:
                    ans += 1
                else:
                    buf[nxt] = 1
                buf[i] = 0
            #print(">", buf)
        print(ans)


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
        input = """4
1 1 3 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
2 2 4 1 1 1 4 2 2 1"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()