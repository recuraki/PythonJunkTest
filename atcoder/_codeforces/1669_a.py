
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




    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        if 1900 <= n:
            ans = 1
        elif 1600 <= n <= 1899:
            ans = 2
        elif 1400 <= n <= 1599:
            ans = 3
        else:
            ans = 4
        print("Division", ans)

    # n questions
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
        input = """7
-789
1299
1300
1399
1400
1679
2300"""
        output = """Division 4
Division 4
Division 4
Division 4
Division 3
Division 2
Division 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()