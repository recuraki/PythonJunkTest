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
        res = []
        s = input()
        l = len(s)
        for i in range(l):
            c = int(s[i])
            if c == 0:
                continue
            res.append(s[i] + ("0" * (l-i-1)))
        print(len(res))
        print(" ".join(res))


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
5009
7
9876
10000
1"""
        output = """2
5000 9
1
7 
4
800 70 6 9000 
1
10000 
1
1 """
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()