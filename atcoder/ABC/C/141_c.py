import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k, q = map(int, input().split())
    res = [k - q] * n
    for _ in range(q):
        c = int(input())
        res[c-1] += 1
    for i in range(n):
        if res[i] <= 0:
            print("No")
        else:
            print("Yes")
    #print(res)



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
        input = """6 3 4
3
1
3
2"""
        output = """No
No
Yes
No
No
No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5 4
3
1
3
2"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9"""
        output = """No
No
No
No
Yes
No
No
No
Yes
No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()