import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint



    INF = 1 << 63
    def do():
        import math
        from math import gcd
        res = -1
        def lcm(x, y):
            return (x * y) // math.gcd(x, y)

        n = int(input())
        dat = []
        for i in range(n):
            a, b = map(int, input().split())
            dat.append( (a,b) )


        dat.sort(reverse=True)
        #print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append( (vala, valb) )
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 > pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append( (vala, valb) )
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append( (vala, valb) )
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=False)
        #print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append( (vala, valb) )
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 > pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append( (vala, valb) )
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append( (vala, valb) )
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=True)
        # print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append((vala, valb))
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 >= pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append((vala, valb))
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append((vala, valb))
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=False)
        # print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append((vala, valb))
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 >= pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append((vala, valb))
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append((vala, valb))
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))
        #################################
        dat.sort(reverse=True, key=lambda x: x[1])
        #print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append( (vala, valb) )
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 > pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append( (vala, valb) )
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append( (vala, valb) )
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=False, key=lambda x: x[1])
        #print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append( (vala, valb) )
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 > pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append( (vala, valb) )
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append( (vala, valb) )
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=True, key=lambda x: x[1])
        # print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append((vala, valb))
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 >= pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append((vala, valb))
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append((vala, valb))
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))

        dat.sort(reverse=False, key=lambda x: x[1])
        # print(dat)
        vala, valb = dat[0]
        candidate = []
        candidate.append((vala, valb))
        for a, b in dat:
            newcandicate = []
            curmax = -1
            for vala, valb in candidate:
                pat1 = lcm(gcd(vala, a), gcd(valb, b))
                pat2 = lcm(gcd(vala, b), gcd(valb, a))
                if pat1 >= pat2:
                    vala, valb = gcd(vala, a), gcd(valb, b)
                else:
                    vala, valb = gcd(vala, b), gcd(valb, a)
                if lcm(vala, valb) == curmax:
                    newcandicate.append((vala, valb))
                    continue
                if lcm(vala, valb) < curmax:
                    continue
                if lcm(vala, valb) > curmax:
                    newcandicate = []
                    curmax = lcm(vala, valb)
                    newcandicate.append((vala, valb))
                    continue
            candidate = newcandicate
        res = max(res, lcm(vala, valb))



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

    def test_input_11(self):
        print("test_input_11")
        input = """2
1 10
2 10"""
        output = """"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """2
2 15
10 6"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
148834018 644854700
947642099 255192490
35137537 134714230
944287156 528403260
68656286 200621680"""
        output = """238630"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20
557057460 31783488
843507940 794587200
640711140 620259584
1901220 499867584
190122000 41414848
349507610 620259584
890404700 609665088
392918800 211889920
507308870 722352000
156850650 498904448
806117280 862969856
193607570 992030080
660673950 422816704
622015810 563434560
207866720 316871744
63057130 117502592
482593010 366954816
605221700 705015552
702500790 900532160
171743540 353470912"""
        output = """152594452160"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()