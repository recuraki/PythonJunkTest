import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n = int(input())
        dat = []
        for i in range(n):
            t, l, r = map(int, input().split())
            if t == 1: # [ ]
                pass
            elif t == 2: # [ )
                r -= 0.1
            elif t == 3: # ( ]
                l += 0.1
            elif t == 4: # ( )
                r -= 0.1
                l += 0.1
            else:
                assert False
            if l > r:
                continue # これは足さない
            x = (l, r)
            dat.append(x)
        n = len(dat)
        #print(dat)
        res = 0
        for i in range(n):
            l1, r1 = dat[i]
            for j in range(i+1, n):
                l2, r2 = dat[j]
                #print(l1, r1, l2, r2)
                if l1 <= l2 <= r1:
                    res += 1
                    continue
                if l2 <= l1 <= r2:
                    res += 1
                    continue
        print(res)

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
1 1 2
2 2 3
3 2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817"""
        output = """102"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()