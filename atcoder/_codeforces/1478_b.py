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
        q,d = map(int, input().split())
        dat = list(map(int, input().split()))
        for x in dat:
            can = False
            for i in range(110):
                if x < d or x < 0:
                    break
                if str(x).count(str(d)) != 0:
                    can = True
                    break
                x -= d
            if can:
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
        input = """2
3 7
24 25 1000000000001
10 7
51 52 53 54 55 56 57 58 59 60"""
        output = """YES
NO
YES
YES
YES
NO
YES
YES
YES
YES
YES
YES
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()