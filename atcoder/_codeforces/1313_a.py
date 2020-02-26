import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        a, b,c = map(int, input().split())
        res = 0
        if a > 3:
            res +=1
            a -= 1
        if b > 3:
            res +=1
            a -= 1
        if c > 3:
            res +=1
            a -= 1
        if a > 0 and b > 0:
            res +=1
            a -= 1
            b -= 1
        if c > 0 and b > 0:
            res +=1
            c -= 1
            b -= 1
        if a > 0 and c > 0:
            res +=1
            a -= 1
            c -= 1
        if a > 0 and c > 0 and b > 0:
            res +=1
        print(res)



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
1 2 1
0 0 0
9 1 7
2 2 3
2 3 2
3 2 2
4 4 4"""
        output = """3
0
4
5
5
5
7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()