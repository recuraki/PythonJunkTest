import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n, k = map(int, input().split())
        s = input()
        if k == 0:
            print("YES")
            return
        samenum = 0
        for i in range(n//2):
            if s[i] == s[n-1-i]:
                samenum += 1
                continue
            else: # not same
                break
        if samenum == 0:
            print("NO")
            return
        centerstrnum = n - (2 * samenum)
        k -= samenum
        #print(k, samenum, centerstrnum, file=sys.stderr)
        if k < 0:
            print("YES")
            return
        elif k == 0 and centerstrnum != 0:
            print("YES")
            return
        else:
            print("NO")
            return


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
        input = """7
5 1
qwqwq
2 1
ab
3 1
ioi
4 2
icpc
22 0
dokidokiliteratureclub
19 8
imteamshanghaialice
6 3
aaaaaa"""
        output = """YES
NO
YES
NO
YES
NO
NO"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
3 1
vba
"""
        output = """
"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()