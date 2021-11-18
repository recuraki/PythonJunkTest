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
    from pprint import pprint

    INF = 1 << 63
    l = list()
    def f():
        nn = 10
        ss = set()
        for n in range(nn+1):
            for a in range(10):
                for b in range(10):
                    for pat in range(2 ** n):
                        x = 0
                        for i in range(n):
                            x *= 10
                            if (pat >> i) & 1 == 1:
                                x += b
                            else:
                                x += a
                        ss.add(x)
        for x in ss: l.append(x)
        l.sort()


    def do():
        from bisect import bisect_left
        n, k = map(int, input().split())
        s = str(n)
        sl = len(str(n))
        if s.count(s[0]) == sl:
            print(s)
            return
        if k == 1:
            for i in range(1,10):
                if int(str(i)*sl) >= n:
                    print(str(i)*sl)
                    return
        # k == 2
        ind = bisect_left(l, n)
        print(l[ind])


    f()
    #print(len(l))
    #for x in l:
    #    if  100000 <= x <= 200000:
    #        print(x)
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
        input = """4
1 1
221 2
177890 2
998244353 1"""
        output = """1
221
181111
999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()