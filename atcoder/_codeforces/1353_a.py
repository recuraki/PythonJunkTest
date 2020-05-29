import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n,m  = map(int, input().split())
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(m*2)





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
1 5
2 5
3 5
4 5
5 5"""
        output = """0
5
10
1
1"""
        self.assertIO(input, output)

unittest.main()