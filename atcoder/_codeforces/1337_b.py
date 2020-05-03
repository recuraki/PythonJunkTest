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
        x, n, m = map(int, input().split())
        for _ in range(n):
            if x <= 10:
                break
            x = x // 2 + 10
            #print(x)
        x -= 10*m
        #print(x)
        #print("----")
        print("YES" if x <= 0 else "NO")





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
        input = """7
100 3 4
189 3 4
64 2 3
63 2 3
30 27 7
10 9 1
69117 21 2"""
        output = """YES
NO
NO
YES
YES
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()