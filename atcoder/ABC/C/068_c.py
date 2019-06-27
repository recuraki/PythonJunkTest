import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat_m = [[] for x in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        dat_m[a].append(b)
    c = False
    for i in dat_m[1]:
        if n in dat_m[i]:
            c = True
    print("POSSIBLE" if c else "IMPOSSIBLE")



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
        input = """3 2
1 2
2 3"""
        output = """POSSIBLE"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 2
2 3
3 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000 1
1 99999"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5 5
1 3
4 5
2 3
2 4
1 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()