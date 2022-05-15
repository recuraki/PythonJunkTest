import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():




    def do():
        n = int(input())
        last = 1
        l = []
        while n > 0:
            if last == 1:
                if n >= 2:
                    l.append(2)
                    n -= 2
                else:
                    break
                last = 2
            else:
                l.append(1)
                n -= 1
                last = 1
        if n > 0:
            n -= 1
            l = [1] + l
        #print(l, sum(l), n)
        print("".join(list(map(str, l))))

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
        input = """5
1
2
3
4
5"""
        output = """1
2
21
121
212"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()