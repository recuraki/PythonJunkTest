import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        errorEvenNum = 0
        errorOddNum = 0
        for i in range(n):
            if i % 2 == 0:
                if dat[i] % 2 == 1:
                    errorEvenNum += 1
            else: # i=odd
                if dat[i] % 2 == 0:
                    errorOddNum += 1

        if n == 1:
            if dat[0] % 2 == 0:
                print(0)
            else:
                print(-1)
        else:
            if n % 2 == 0:
                if errorEvenNum == errorOddNum:
                    print(errorOddNum)
                else:
                    print(-1)
            else:
                if errorEvenNum == errorOddNum:
                    print(errorOddNum)
                else:
                    print(-1)






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
        input = """4
4
3 2 7 6
3
3 2 6
1
7
7
4 9 2 1 18 3 0"""
        output = """2
1
-1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()