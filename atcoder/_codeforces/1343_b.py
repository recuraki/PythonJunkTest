import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        if n == 2:
            print("NO")
        elif (n//2) % 2 == 1:
            print("NO")
        else:
            res = []
            for i in range(n//2):
                res.append(2*(i+1) )
            t = sum(res)
            for i in range(n//2 - 1):
                res.append(i * 2 + 1)
                t -= (i * 2 + 1)
            res.append(t)
            print("YES")
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
        input = """5
2
4
6
8
10"""
        output = """NO
YES
2 4 1 5
NO
YES
2 4 6 8 1 3 5 11
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()