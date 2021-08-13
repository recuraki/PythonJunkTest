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
        n, m = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = []
        e = [[] for _ in range(n)]
        for i in range(m):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            buf.append([x, y])
            e[x].append(y)
        finalRes = -99999999999999999
        resMin = [None] * n
        for i in range(n):
            if resMin[i] is not None:
                finalRes = max(finalRes, dat[i] - resMin[i] )
            resMin[i] = min(resMin[i], dat[i]) if resMin[i] is not None else dat[i]
            for nextNode in e[i]:
                if resMin[nextNode] is not None:
                    resMin[nextNode] = min(resMin[nextNode], resMin[i])
                else:
                    resMin[nextNode] = resMin[i]
        print(finalRes)
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
        input = """4 3
2 3 1 5
2 4
1 2
1 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5
13 8 3 15 18
2 4
1 2
4 5
2 3
1 3"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 1
1 100 1
2 3"""
        output = """-99"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()