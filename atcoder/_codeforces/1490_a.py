
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
        n = int(input())
        dat = list(map(int, input().split()))
        res = 0
        for i in range(n - 1):
            a, b = dat[i], dat[i+1]
            a, b = min(a, b), max(a, b)
            #print(">", a, b)
            while 2*a < b:
                #print("!")
                res += 1
                a *= 2
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
2 9"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()