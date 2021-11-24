import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
        import math
        n, m, k = map(int, input().split())
        data = list(map(int, input().split()))
        for i in range(m):
            data[i] -= 1
        print(n, m, k)
        print(data)
        for i in range(n-1):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            print(u, v)

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
        input = """4 5 0
2 3 2 1 4
1 2
2 3
3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 10 10000
1 2 1 2 1 2 2 1 1 2
1 2
1 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 2 -1
1 10
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """126"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5 8 -1
1 4 1 4 2 1 3 5
1 2
4 1
3 1
1 5"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()