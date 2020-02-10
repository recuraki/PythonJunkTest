import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        dat=list(map(int, input().split()))
        ocount = 0
        ecount = 0
        for i in range(len(dat)):
            if dat[i] % 2 ==0:
                ecount += 1
            else:
                ocount += 1
        if ocount == 0:
            print("NO")
        elif ocount % 2 == 0  and ecount == 0:
            print("NO")
        else:
            print("YES")




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
2
2 3
4
2 2 8 8
3
3 3 3
4
5 5 5 5
4
1 1 1 1"""
        output = """YES
NO
YES
NO
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()