import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, x = map(int, input().split())
        dat = list(map(int, input().split()))

        minind = -1
        minkai = 10000000000
        for i in range(len(dat)):
            cur = dat[i]
            cnt = 0
            while cur % x == 0:
                cur //= x
                cnt += 1
            if minkai > cnt:
                minkai = cnt
                minind = i
        res = sum(dat) * (minkai + 1)
        for i in range(minind):
            res += dat[i]
        print(res)

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
        input = """2
1 2
12
4 2
4 6 8 2"""
        output = """36
44"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()