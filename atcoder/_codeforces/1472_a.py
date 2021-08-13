import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        w, h, n = map(int, input().split())
        res = 1
        while w % 2 == 0:
            w //= 2
            res *= 2
        while h % 2 == 0:
            h //= 2
            res *= 2
        if res >= n:
            print("YES")
        else:
            print("NO")


    q = int(input())
    for _ in range(q):
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
        input = """5
2 2 3
3 3 2
5 10 2
11 13 1
1 4 4"""
        output = """YES
NO
YES
YES
YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()