import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        n = int(input())
        l = len(str(n))
        res = 0
        for i in range(1, l + 1):
            for j in range(1, 10):
                k = int(str(j) * i)
                if k <= n:
                    res += 1

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
        input = """6
1
2
3
4
5
100"""
        output = """1
2
3
4
5
18"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()