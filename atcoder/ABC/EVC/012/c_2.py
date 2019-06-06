import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_s = []
    for i in range(n):
        dat_s.append(int(input()))

    # 0個選択したときのスコア(重複は意味がないのでset)
    scores = set([0])

    # 1～n問まで回す
    for i in range(n):
        # ここまでで可能性のあるスコアをbufferにいれて
        b = set(scores)
        while len(b) != 0:
            # いまのn問目のスコアをこのスコアに足していく
            scores.add(dat_s[i] + b.pop())

    # 可能性のあるスコアの中から10で割り切れるスコアは消す(=0にする)
    scores = map(lambda x: 0 if x % 10 == 0 else x, scores)
    print(max(scores))






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
        logging.info("test_input_1")
        input = """3
5
10
15"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()