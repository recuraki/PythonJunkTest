import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
まず、a,bの比較を行い、a < bならそのままb < aなら"aとb" "cとd" をswapする
a < b < c < d の場合は「追い越し」は発生しない
a < b < d < c の場合は「追い越し」が発生する
追い越しは区間oooがなければできない(真ん中のoがb<=の区間か、<=dの区間にないといけない)
移動は a -> max(c,d)に"xx"がなければ移動できる
"""

def resolve():
    n,a,b,c,d, = map(int, input().split())
    s = input()
    s = "_" + s

    if a > b:
        a,b,c,d = b,a,d,c

    #print("{0},{1},{2},{3}".format(str(a), str(b), str(c), str(d)))

    # print(s)
    """
      012345678
     "#####...#####".find("...")
    5
    >>> "#####...#####"[:5]
    '#####'
    >>> "#####...#####"[5+3:]
    '#####'
    >>> "0123456789"[1:7]
    '123456'
    """

    if c < d:
        # 追い越しが不要の場合
        #print("c<d")
        # print(s)
        #print(s[a:d+1])
        if s[a:d+1].find("##") == -1: # 障害がないなら
            print("Yes")
        else:
            print("No")

    else:
        # 追い越しが必要の場合
        #print(s)
        #print("takeover")
        #print(s[b-1:d+2])
        if s[b-1:d+2].find("...") != -1:
            #print(s[a:c+1])
            if s[a:c + 1].find("##") == -1: # 障害がないなら
                print("Yes")
            else:
                print("No")
        else:
            # 追い越し区間がないなら抜けない
            print("No")


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
        input = """7 1 3 6 7
.#..#.."""
        input = """13 6 4 10 9
###.#..#..###"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """7 1 3 7 6
.#..#.."""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """15 1 3 15 13
...#.#...#.#..."""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()