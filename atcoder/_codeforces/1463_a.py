import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        a,b,c = map(int, input().split())
        t = a+ b+ c
        x = t // 9
        if t % 9 == 0 and min(a, b, c)  > x:
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
3 3 12
1 1 1
10 1 7"""
        output = """YES
NO
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()