import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        from collections import defaultdict
        n = int(input())
        buf = []
        for _ in range(n):
            a, b = map(int, input().split())
            buf.append( (a, b) )
        s = input()

        dat = defaultdict(list)
        for i in range(n):
            x, y = buf[i]
            if s[i] == "R":
                dat[y].append( (x , 1) )
            else:
                dat[y].append( (x, -1) )
        #print(dat)
        for k in dat.keys(): # k = y
            dat[k].sort()
            isR = False
            for x, dir in dat[k]:
                if dir == -1: # go Left
                    if isR:
                        print("Yes")
                        return
                    continue
                # Right
                isR = True
        print("No")
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
        input = """3
2 3
1 1
4 1
RRL"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1 1
2 1
RR"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()