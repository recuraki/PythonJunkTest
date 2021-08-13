import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    from collections import defaultdict
    def do():

        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        d = defaultdict(int)
        color = 0
        res = -1
        # 準備
        for i in range(k):
            x = dat[i]
            if d[x] == 0:
                color += 1
            d[x] += 1
        res = max(res, color)

        for i in range(n-k):
            # out
            x = dat[i]
            d[x] -= 1
            if d[x] == 0:
                color -= 1

            # in
            x = dat[k + i]
            if d[x] == 0:
                color += 1
            d[x] += 1

            res = max(res, color)

        print(res)

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
        input = """7 3
1 2 1 2 3 3 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5
4 4 4 4 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 6
304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()