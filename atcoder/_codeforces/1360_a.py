
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
        a,b = map(int, input().split())
        a,b = min(a,b), max(a,b)
        x = a * 2
        x = b if x < b else x
        print(x**2)



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
        input = """8
3 2
4 2
1 1
3 1
4 7
1 3
7 4
100 100"""
        output = """16
16
4
9
64
9
64
40000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()