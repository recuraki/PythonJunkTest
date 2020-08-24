import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q=int(input())
    for _ in range(q):
        n = int(input())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        if dat2.count(1) != 0 and dat2.count(0) != 0:
            print("Yes")
            continue
        can = True
        p = dat1[0]
        for i in range(n):
            if dat1[i] < p:
                can = False
                break
            p = dat1[i]
        print("Yes" if can else "No")






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
4
10 20 20 30
0 1 0 1
3
3 1 2
0 1 1
4
2 2 4 8
1 1 1 1
3
5 15 4
0 0 0
4
20 10 100 50
1 0 0 1"""
        output = """Yes
Yes
Yes
No
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()