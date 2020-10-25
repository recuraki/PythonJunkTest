import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import collections
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        q = collections.deque(dat)
        while True:
            if len(q) == 0:
                break
            x = q.popleft()
            if x == 0:
                continue
            q.appendleft(x)
            break
        while True:
            if len(q) == 0:
                break
            x = q.pop()
            if x == 0:
                continue
            q.append(x)
            break
        print(list(q).count(0))


    q = int(input())
    for _ in range(q):
        do()
    # do()



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
7
0 0 1 0 1 0 1
3
1 0 0
5
1 1 0 0 1
6
1 0 0 0 0 1
5
1 1 0 1 1
5
0 0 0 0 1"""
        output = """2
0
2
4
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()