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
        n, d = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort()
        a = dat[0]
        b = dat[1]
        if a > d or b > d:
            print("NO")
            return
        if dat[-1] <= d:
            print("YES")
            return
        if a+b <= d:
            print("YES")
            return
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
        input = """3
5 3
2 3 2 5 4
3 4
2 4 4
5 4
2 1 5 3 6"""
        output = """NO
YES
YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()