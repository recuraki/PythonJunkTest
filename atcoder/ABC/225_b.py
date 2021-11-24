import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        g = [[] for _ in range(n)]
        for _ in range(n-1):
            a, b = map(int, input().split())
            a-=1
            b-=1
            g[a].append(b)
            g[b].append(a)
        cnt = 0
        for i in range(len(g)):
            if len(g[i]) == (n-1): cnt += 1
        if cnt == 1:
            print("Yes")
            return
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
        input = """5
1 4
2 4
3 4
4 5"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
2 4
1 4
2 3"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
9 10
3 10
4 10
8 10
1 10
2 10
7 10
6 10
5 10"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()