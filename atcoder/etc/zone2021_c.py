import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    def main():
        t = deque([])
        s = input()
        isflap = False
        # 積むところ
        for x in s:
            if x == "R":
                isflap = not isflap
            elif isflap is False:
                t.append(x)
            else:
                t.appendleft(x)
        # 同じ字があるなら消す
        t = list(t)
        if isflap:
            t = t[::-1]
        res = list()
        for x in t:
            if len(res) == 0:
                res += x
            elif res[-1] == x:
                res.pop()
            else:
                res.append(x)
        print("".join(res))
    main()


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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()