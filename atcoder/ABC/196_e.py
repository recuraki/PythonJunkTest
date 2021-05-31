import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def main():
        import sys
        read = sys.stdin.read
        n, *indata = map(int, read().split())
        dat = []
        offset = 0
        for i in range(n):
            a, t = indata[offset + 2*i],indata[offset + 2*i+1]
            dat.append( (a, t) )
        offset = 2 * n
        q = indata[offset]
        datx = indata[offset+1: ]
        def do(x):
            for a, t in dat:
                if t == 1:
                    x += a
                elif t == 2:
                    x = max(x, a)
                elif t == 3:
                    x = min(x, a)
            return x


        maxval = do(10**18)
        minval = do(-(10**18))
        l = -10**18
        h =  10**18
        while l <= h:
            mid = (l + h) // 2
            #print("try", l, h, mid, mid, mid + 1, do(mid), do(mid+1))
            if do(mid) < maxval:  # 買うことができるなら
                l = mid + 1  # 買えるのでそれ以上の数
                #print("set l", l)
            else:  # 買えないなら
                h = mid - 1  # 買えないのでそれ以下の数をトライ
                #print("set h", h)
        if do(l-1) == maxval:
            boarderl = l-2
        elif do(l) == maxval:
            boarderl = l-1
        elif do(l+1) == maxval:
            boarderl = l
        elif do(l+2) == maxval:
            boarderl = l+1
        l = -10**18
        h =  10**18
        while l <= h:
            mid = (l + h) // 2
            #print("try", l, h, mid, mid, mid + 1, do(mid), do(mid+1))
            if do(mid) <= minval:  # 買うことができるなら
                l = mid + 1  # 買えるのでそれ以上の数
                #print("set l", l)
            else:  # 買えないなら
                h = mid - 1  # 買えないのでそれ以下の数をトライ
                #print("set h", h)
        if do(l+1) == minval:
            boarderr = l+2
        elif do(l) == minval:
            boarderr = l + 1
        elif do(l-1) == minval:
            boarderr = l
        elif do(l-2) == minval:
            boarderr = l-1

        for x in datx:
            if x < boarderr:
                print(minval)
                continue
            elif x > boarderl:
                print(maxval)
                continue
            else:
                offset = x - (boarderr - 1)
                print(minval + offset)
                continue


    main()
    # ★★★★★★★★commit前に10**9を考える たぶん、10** 12

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
-10 2
10 1
10 3
5
-15 -10 -5 0 5"""
        output = """0
0
5
10
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()