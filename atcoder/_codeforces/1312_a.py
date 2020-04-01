import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    t = int(input())
    for _ in range(t):
        f = False
        n, m = map(int, input().split())
        #print(n,m)
        if n == 5 or n == 3 or n == 4:
            pass
        else:
            for i in range(2, 100):
                if m * i == n:
                    f = True
                    break



        print("NO" if f is False else "YES")




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
12 6
12 7
12 8
4 2
5 2
9 4
9 3
20 5
6 3"""
        output = """YES
NO
NO
NO
NO
NO
YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()