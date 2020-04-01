import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
from pprint import pprint
q = int(input())
for _ in range(q):
    n = int(input())
    target = []
    usedg = [0] * n # gen
    usedl = [0] * n # lady

    for i in range(n):
        l = []
        dat = list(map(int, input().split()))
        num = dat[0]
        for j in range(1, num + 1):
            dat[j] -= 1 # 0 origin
            if usedg[dat[j]] is 0:
                usedg[dat[j]] = 1
                usedl[i] = 1
                #print("marry", i, dat[j])
                break

    if sum(usedg) == n:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        a,b = -1,-1
        for i in range(n):
            if usedl[i] == 0:
                a = i + 1
            if usedg[i] == 0:
                b = i + 1
        print(a,b)

        #print(usedg)
        #print(usedl)

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
2 2 3
2 1 2
2 3 4
1 3
2
0
0
3
3 1 2 3
3 1 2 3
3 1 2 3
1
1 1
4
1 1
1 2
1 3
1 4"""
        output = """IMPROVE
4 4
IMPROVE
1 1
OPTIMAL
OPTIMAL
OPTIMAL"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()