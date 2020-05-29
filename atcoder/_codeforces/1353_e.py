import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    for _ in range(q):
        print("---")
        n, k = map(int, input().split())
        s = input()
        res1 = [0] * k
        res2 = [0] * k
        res3 = [0] * k
        onnum = s.count("1")
        offnum = s.count("0")
        for i in range(n):
            if s[i] == "1":
                res1[i%k] += 1
            else:
                res2[i % k] += 1
        for j in range(k):
            res3[j] = n // k + (1 if n%k > j else 0)
        final = 99999999999999999
        for i in range(k):
            x = 0
            x += onnum - res1[i]
            x += res3[i] - res1[i]
            final = min(final, x)
        print(res1)
        print(res2)
        print(res3)
        print(final)




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
        input = """6
9 2
010001010
9 3
111100000
7 4
1111111
10 3
1001110101
1 1
1
1 1
0"""
        output = """1
2
5
4
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()