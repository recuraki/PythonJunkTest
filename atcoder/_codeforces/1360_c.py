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
        n = int(input())
        isdelete = False
        dat = list(map(int, input().split()))
        dat.sort()
        odd = []
        even = []
        prev = -100
        for i in range(n):
            if dat[i] % 2 == 0:
                even.append(dat[i])
            else:
                odd.append(dat[i])
            diff = dat[i] - prev
            if diff == 1:
                isdelete = True
            prev = dat[i]
        #print(even)
        #print(odd)
        #print(isdelete)
        if len(even) % 2 == 0 and len(odd) % 2 == 0:
            print("YES")
        elif len(even) % 2 == 1 and len(odd) % 2 == 0:
            print("NO")
        elif len(even) % 2 == 0 and len(odd) % 2 == 1:
            print("NO")
        else: # even odd
            if isdelete:
                print("YES")
            else:
                print("NO")



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
4
11 14 16 12
4
11 12 7 14
4
1 1 1 1
4
1 2 5 6
2
12 13
6
1 6 3 10 5 8
6
1 12 3 10 5 8"""
        output = """YES
YES
YES
YES
YES
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()