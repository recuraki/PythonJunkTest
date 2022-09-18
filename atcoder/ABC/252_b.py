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
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        selected = set()
        maval = max(a)
        for i in range(n):
            if a[i] == maval: selected.add(i+1)
        ans = False
        for k in b:
            if k in selected: ans = True
        if ans:
            print("Yes")
        else:
            print("No")


    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()



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
        input = """5 3
6 8 10 7 10
2 3 4"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2
100 100 100 1 1
5 4"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 1
100 1
2"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()