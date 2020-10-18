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
        q = int(input())
        for _ in range(q):
            from collections import deque
            n = int(input())
            s = input()
            c = countstrs(s)
            c = map(lambda x: x[1], c)
            c = list(c)
            c = deque(c)
            #print(c)
            over2 = []
            for i in range(len(c)):
                x = c[i]
                if x == 1:
                    continue
                over2.append([i, x]) # i個目は 2以上の 数字をもつ
            over2 = deque(over2)
            res = 0
            l = 0
            endl = len(c)
            while l < endl:
                res += 1
                used2 = False
                if len(over2) > 0:
                    ind, x = over2.popleft()
                    if ind == l: # 今のますに複数あるなら そのまま使う
                        used2 = True
                    else: # そうでないなら次のを１つかりる
                        used2 = True
                        x -= 1
                        if x > 1:
                            over2.appendleft([ind, x])
                if used2 is False:
                    l += 1
                l += 1
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
        input = """5
6
111010
1
0
1
1
2
11
6
101010"""
        output = """3
1
1
1
3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
11
11001101011"""
        output = """6"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()