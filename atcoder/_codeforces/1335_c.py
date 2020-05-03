import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import collections
    q = int(input())
    for _ in range(q):
        s = int(input())
        dat = list(map(int, input().split()))
        c = collections.Counter(dat)
        mc = c.most_common(1)[0][0]
        typenum = len(c) - 1
        #print(c)
        #print("mc", mc)
        mcnum = c[mc]
        #print(typenum)
        res = min(mcnum, typenum)
        if mcnum >= typenum + 2:
            res += 1
        #print("RES")
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
7
4 2 4 1 4 3 4
5
2 1 5 4 3
1
1
4
1 1 1 3
6
1 2 3 4 4 4
7
1 2 3 4 4 4 4
8
1 2 3 4 4 4 4 4"""
        output = """3
1
0
2
3
3
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()