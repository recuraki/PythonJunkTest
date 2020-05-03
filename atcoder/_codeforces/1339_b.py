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
        import collections
        dat = list(map(int, input().split()))
        dat.sort()
        dat = collections.deque(dat)
        turn = True
        #print(dat)
        res = collections.deque([])
        while len(res) < n:
            if turn is True:
                turn = False
                x = dat.pop()
                res.appendleft(x)
            else:
                turn = True
                x = dat.popleft()
                res.appendleft(x)
        #print(res)
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
        input = """2
6
5 -2 4 8 6 5
4
8 1 4 2"""
        output = """5 5 4 6 8 -2
1 2 4 8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()