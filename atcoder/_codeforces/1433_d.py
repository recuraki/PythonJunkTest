import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    import collections
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        c = collections.Counter(dat)
        if len(c) == 1:
            print("NO")
            return
        f = dat[0]
        s = None
        sind = None
        for i in range(n):
            if dat[i] != f:
                s = dat[i]
                sind = i
                break
        print("YES")
        for i in range(1,n):
            if dat[i] == f:
                print(i+1, sind + 1)
            else:
                print(i+1, 1)
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
        input = """4
5
1 2 2 1 3
3
1 1 1
4
1 1000 101 1000
4
1 2 3 4"""
        output = """YES
1 3
3 5
5 4
1 2
NO
YES
1 2
2 3
3 4
YES
1 2
1 3
1 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()