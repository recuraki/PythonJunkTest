import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        a = set()
        n = int(input())
        dat = []
        from collections import defaultdict
        cnt = defaultdict(int)
        for _ in range(n):
            x, y = input().split()
            dat.append( (x, y) )
            cnt[x] += 1
            cnt[y] += 1
        #print(cnt)
        for x, y in dat:
            #print(x,"/",y)
            if cnt[x] == 1: continue
            if cnt[y] == 1: continue
            if x == y and cnt[x] == 2: continue
            print("No")
            return

        print("Yes")


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
        input = """3
tanaka taro
tanaka jiro
suzuki hanako"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
aaa bbb
xxx aaa
bbb yyy"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
tanaka taro
tanaka taro"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """3
takahashi chokudai
aoki kensho
snu ke"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()