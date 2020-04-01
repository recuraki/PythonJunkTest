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
        dat = list(map(int, input().split()))
        s = sum(dat)
        oddnum = 0
        for i in range(len(dat)):
            if dat[i] % 2 == 1:
                oddnum += 1

        res = []

        if oddnum == 0:
            print(n)
            res = []
            for i in range(n):
                res.append(i + 1)
            print(" ".join(list(map(str, res))))
        else:
            if n == 1:
                print(-1)
            else:
                a = False
                for i in range(n):
                    if dat[i] % 2 == 1 and a is False and s % 2 == 1:
                        a = True
                        continue
                    else:
                        res.append(i + 1)
                print(len(res))
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
        input = """4
3
1 4 3
1
15
2
3 5
3
2 4 6"""
        output = """1
2
-1
2
1 2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()