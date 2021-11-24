import collections
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


    from pprint import pprint

    INF = 1 << 63
    def do():
        import collections
        s = input()
        c = collections.Counter(s)
        #print(c)
        delorder = []
        delset = set()

        for x in s[::-1]:
            if x in delset: continue
            delset.add(x)
            delorder.append(x)
        #print(delorder)
        d = collections.defaultdict(int)
        cnt = len(delset)
        seikai = collections.defaultdict(int)
        total = 0
        for i in range(len(delorder)):
            ch = delorder[i]
            chcnt = c[ch] / (len(delorder)-i)
            if chcnt.is_integer() is False:
                print(-1)
                return
            #print(ch, chcnt)
            total += chcnt
            seikai[ch] = chcnt
        total = int(total)
        base = s[:total]
        resbase = s[:total]
        #print(base)
        very = base
        for x in delorder[::-1]:
            base = base.replace(x, "")
            very += base
        #print(very)
        if very != s:
            print(-1)
            return
        print(resbase, "".join(delorder[::-1]))



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
abacabaaacaac
nowyouknowthat
polycarppoycarppoyarppyarppyrpprppp
isi
everywherevrywhrvryhrvrhrvhv
haaha
qweqeewew"""
        output = """abacaba bac
-1
polycarp lcoayrp
is si
everywhere ewyrhv
-1
-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()