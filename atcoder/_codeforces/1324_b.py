import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    qq = int(input())
    for _ in range(qq):
        n = int(input())
        dat = list(map(int, input().split()))
        f = False
        d = dict()
        for i in range(n):
            #print(d)
            if dat[i] in d:
                if i - d[dat[i]] != 1:
                    f = True
            else:
                d[dat[i]] = i


        print("YES" if f else "NO")



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
3
1 2 1
5
1 2 2 3 2
3
1 1 2
4
1 2 2 1
10
1 1 2 2 3 3 4 4 5 5"""
        output = """YES
YES
NO
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()