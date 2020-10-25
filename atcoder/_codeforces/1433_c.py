import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        ma = max(dat)
        res = -1
        for i in range(n):
            if dat[i] != ma:
                continue
            if i != 0:
                if ma > dat[i-1]:
                    res = i+1
                    break
            if i != (n-1):
                if ma > dat[i + 1]:
                    res = i+1
                    break
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
        input = """1
2
1 3
"""
        output = """None"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()