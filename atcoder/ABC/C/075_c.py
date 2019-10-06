import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,m = map(int, input().split())
    import collections
    ma = []
    for i in range(n + 1):
        ma.append(collections.deque([]))

    for i in range(m):
        a,b = map(int, input().split())
        ma[a].append(b)
        ma[b].append(a)
    from pprint import pprint
    pprint(ma)


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
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 5
1 2
2 3
3 4
4 5
5 6"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()