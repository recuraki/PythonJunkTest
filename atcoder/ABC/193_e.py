import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    def do():
        x, y, p, q = map(int, input().split())
        a = x
        untila = x + y
        diffa = 2 * x + y

        firstb = p
        diffb = x + y
        for i in range(3):



    q = int(input())
    for _ in range(q):
        do()
        sys.exit(0)
    # do()

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
5 2 7 6
1 1 3 1
999999999 1 1000000000 1"""
        output = """20
infinity
1000000000999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()