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

        if n % 2 == 0:
            res = []
            buf = [1] * ((n-2) // 2)
            buf.extend([0])
            buf.extend([-1] * ((n-2) // 2))
            for i in range(n - 1):
                res.extend(buf[:(n - 1) - i])
            print(" ".join(list(map(str, res))))
            return
        # odd
        res = []
        buf = [1] * (n//2)
        buf.extend([-1] * (n//2))
        #print(buf)
        for i in range(n-1):
            res.extend(buf[:(n-1) - i])
        print(" ".join(list(map(str, res))))

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
3
4
5
6"""
        output = """0
1 -1 1
1 0 -1 1 0 1
1 1 -1 -1 1 1 -1 1 1 1
1 1 0 -1 -1 1 1 0 -1 1 1 0 1 1 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()