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
        if a == 1:
            print("YES")
        elif a == 2 and b == 2:
            print("YES")
        else:
            print("NO")


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
        input = """9
1 1
1 2
2 2
2 1
1 100
2 3
2 4
100000 100000
2 2"""
        output = """YES
YES
YES
YES
YES
NO
NO
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()