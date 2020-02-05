import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)
    import sys
    import collections
    import bisect
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        t = collections.deque(list(t))
        d=dict()
        for i in range(26):
            d[chr(ord("a") + i)] = collections.deque([])
        for i in range(len(s)):
            d[s[i]].append(i)
        res = 1
        curpos = -1 # 現在読み込んだ位置
        isCan = True
        #print(t)
        #print(d)
        while len(t) > 0:
            char = t.popleft() # 次に補完すべき文字を得る
            if len(d[char]) == 0:
                isCan = False
                break
            r = bisect.bisect_left(d[char], curpos)
            #print("find r={0}".format(r))
            if r >= len(d[char]):
                #print("over", file=sys.stderr)
                res += 1
                curpos = d[char][0] + 1
                continue
            pos = d[char][r]
            curpos = pos+1

        if isCan:
            print(res)
        else:
            print("-1")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        self.maxDiff = 100000
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3
aabce
ace
abacaba
aax
ty
yyt"""
        output = """1
-1
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()