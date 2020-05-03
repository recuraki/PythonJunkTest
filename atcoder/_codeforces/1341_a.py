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
        n, a,b,c,d = map(int, input().split())
        weightL = (a-b) * n
        weightR = (a+b) * n
        totalL = (c-d)
        totalR = (c+d)
        #print(weightL, weightR,totalL,totalR)
        if totalL <= weightL <= totalR or totalL <= weightR <= totalR or (weightL <= totalL and totalR <= weightR):
            print("Yes")
        else:
            print("No")



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
7 20 3 101 18
11 11 10 234 2
8 9 7 250 122
19 41 21 321 10
3 10 8 6 1"""
        output = """Yes
No
Yes
No
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()