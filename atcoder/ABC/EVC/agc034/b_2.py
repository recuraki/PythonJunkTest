import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    """
    B,"s/BC/X"したうえで、
    置換できないB,Cで区切って、(re.finditer(r"[AX+"])
    各区間でAをすべて右側に寄せるAの移動回数の和 例: AXAXAXA -> XXXAAAA にするには6回
    """
    import re
    s = input()
    s = s.replace("BC", "X")
    m = re.search(r"[AX]+", s)
    res = 0
    for m in re.finditer(r"([AX]+)", s): # それぞれの[AX]+のパターンについてloop
        count = 0 #
        # 時間なくて、index間違えたくないので、逆順にした
        # (AXAXAXA -> XXXAAAA にするんじゃなくて AXAXAXA -> AAAAXXXにする回数)
        t = ''.join(list(reversed(str(m.groups()[0]))))
        for i in range(len(t)):
            if t[i] == "A":
                # Aが見つかったらXの一番右端に持ってくるのに必要な回数をカウント。例えば、
                # AAAXXXAA で4つめのAを探索しているのなら
                # AAAAXXXA にするのに必要な回数は3 と数えたい
                # Aのindex 6 - (既に見つかっているAの数) 3 = 3 で求められる
                res += (i - count)
                count += 1
    print(res)






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
        input = """ABCABC"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """C"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """ABCACCBABCBCAABCB"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()