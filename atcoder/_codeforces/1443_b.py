import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]
    def do():
        a, b = map(int, input().split())
        s = input()
        if s.count("1") == 0:
            print(0)
            return
        s = s.strip("0") # 左右の0とる
        c = countstrs(s) # ["1", 3こ], ["0", 5こ]みたいなリスト作る
        c = filter(lambda x: x[0] == "0", c) # "0"の個数だけ抜く
        res = a # first bomb
        for char, cnt in c:
            if (cnt * b) < a:
                res += cnt * b
            else:
                res += a
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
        input = """2
1 1
01000010
5 1
01101110"""
        output = """2
6"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_3")
        input = """2
10 1
00000000
10 1
1111111111
"""
        output = """0
10"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()