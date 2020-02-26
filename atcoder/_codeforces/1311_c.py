import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    from copy import deepcopy
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        s = input()
        datp = list(map(int, input().split()))
        kmap = [0] * 26
        totalkey = []
        for i in range(n):
            # a=0, b=1
            c = ord(s[i]) - ord('a')
            kmap[c] += 1
            totalkey.append(deepcopy(kmap))
        #pprint(totalkey)
        res = [0] * 26
        for i in range(m):
            #print("i", i)
            for k in range(26):
                res[k] += totalkey[datp[i] - 1][k]
        for k in range(26):
            res[k] += totalkey[-1][k]
        #print("res")
        #print(res)
        print(" ".join(list(map(str, res))))




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
        input = """3
4 2
abca
1 3
10 5
codeforces
2 8 3 2 9
26 10
qwertyuioplkjhgfdsazxcvbnm
20 10 1 2 3 5 10 5 9 4"""
        output = """4 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 9 4 5 3 0 0 0 0 0 0 0 0 9 0 0 3 1 0 0 0 0 0 0 0
2 1 1 2 9 2 2 2 5 2 2 2 1 1 5 4 11 8 2 7 5 1 10 1 5 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()