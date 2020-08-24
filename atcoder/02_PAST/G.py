import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    qq = int(input())
    buf = collections.deque([])
    for _ in range(qq):
        indat = input().split()
        if indat[0] == "1":
            c, x = indat[1], int(indat[2])
            buf.append([c, x])
        elif indat[0] == "2":
            count = collections.defaultdict(int)
            d = int(indat[1])
            while d > 0 and len(buf) > 0:
                c, x = buf.popleft()
                if d == x: # ぎりぎりなら
                    count[c] += x
                    d = 0
                elif d < x: # 足りてるなら
                    count[c] += d
                    x -= d
                    buf.appendleft([c, x])
                    d = 0
                elif d > x: # 足りないなら
                    count[c] += x
                    d = d - x
            score = 0
            for k in count.keys():
                score += (count[k]**2)
            print(score)






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
1 a 5
2 3
1 t 8
1 c 10
2 21
2 4"""
        output = """9
168
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 x 5
1 y 8
2 7
1 z 8"""
        output = """29"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1 p 3
1 q 100000
2 100000"""
        output = """9999400018"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()