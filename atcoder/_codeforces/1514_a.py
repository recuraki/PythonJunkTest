import math
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    def do():
        sqs = set()
        for i in range(200):
            sqs.add(i*i)

        n = int(input())
        dat = list(map(int, input().split()))
        buf = []
        for x in dat:
            buf.append(x in sqs)
        for x in buf:
            if x is False:
                print("YES")
                return
        print("NO")
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
3
1 5 4
2
100 10000"""
        output = """YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()