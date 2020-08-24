import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        l = input()
        goal = input()

        dat = []
        l = [1 if x == "1" else 0 for x in l]
        import math
        for i in range(math.ceil(len(l) // 2)):
            dat.append(l[i])
            if l[len(l) - 1 - i] == 0:
                dat.append(1)
            else:
                dat.append(0)
        if len(l) & 1 == 1:
            dat.append(l[len(l) // 2])
        #print(dat)

        res = []
        for i in range(n):
            tb = int(goal[n-1-i])
            if tb == dat[i]:
                res.append(1)
            res.append(n-i)

        if len(res) == 0:
            print(0)
        else:
            resstr = " ".join(list(map(str, res)))
            print("{0} {1}".format(len(res), resstr))


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
        input = """5
2
01
10
5
01011
11100
2
01
01
10
0110011011
1000110100
1
0
1"""
        output = """3 1 2 1
6 5 2 5 3 1 2
0
9 4 1 2 10 4 1 2 1 5
1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()