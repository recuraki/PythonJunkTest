import sys
from io import StringIO
import unittest

def resolve():
    s = set()
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        t = ( min(a,b), max(a,b) )
        s.add(tuple(t))
    print(len(s))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """5
1 2
2 1
3 4
5 5
3 4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()