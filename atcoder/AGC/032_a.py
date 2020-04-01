import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    f = True
    res = []
    while len(dat) > 0:
        t = -1
        for i in range(len(dat)):
            if i+1 == dat[i]:
                t = i
        if t == -1:
            f = False
            break
        res.append(dat[t])
        del dat[t]
    if f is False:
        print(-1)
    else:
        res.reverse()
        print("\n".join(list(map(str, res))))

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
        input = """3
1 2 1"""
        output = """1
1
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
2 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
1 1 1 2 2 1 2 3 2"""
        output = """1
2
2
3
1
2
2
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()