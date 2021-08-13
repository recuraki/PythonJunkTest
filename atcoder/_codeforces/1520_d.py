import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        def sigma1(n):
            return n * (n + 1) // 2
        n = int(input())
        dat = list(map(int, input().split()))
        table = [0] * (n + 1 + n)
        offset = n # zeroのindex
        for i in range(n):
            diff = dat[i] - (i + 1)
            table[offset + diff] += 1
        res = 0
        for x in table:
            res += sigma1(x-1)
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
        input = """4
6
3 5 1 4 6 6
3
1 2 3
4
1 3 3 4
6
1 6 3 4 5 6"""
        output = """1
3
3
10"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()