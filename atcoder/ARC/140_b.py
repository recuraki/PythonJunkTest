import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    # import pypyjit
    # pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    from collections import deque
    def do():
        n = int(input())
        s = input()
        buf = []
        for i in range(n):
            if s[i] != "R": continue
            # Rの場合左右のA, Cを確認
            cnt = 0
            offset = 1
            while 0 <= i - offset and i + offset < n:
                if s[i - offset] == "A" and s[i + offset] == "C":
                    cnt += 1
                else:
                    break
                offset += 1
            if cnt != 0:
                buf.append(cnt)
        # print(s, buf)
        from collections import deque
        buf.sort()
        q = deque(buf)
        # print(q)
        ans = 0
        op = 1
        while len(q) > 0:
            ans += 1
            if op % 2 == 1:
                x = q.pop()
                x -= 1
                if x != 0:
                    q.append(x)
            else:
                q.popleft()
            op = 1 - op
        print(ans)

    # 1 time
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
        input = """6
AARCCC"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
AAAAA"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
ARCARCARC"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """11
ARCAARCCARC"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """13
AAARCCCARCARC"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_51(self):
        print("test_input_51")
        input = """4
ARRC"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_52(self):
        print("test_input_52")
        input = """14
AAARCCCAAARCCC"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_53(self):
        print("test_input_53")
        input = """13
ARCAARCCAARCC"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()