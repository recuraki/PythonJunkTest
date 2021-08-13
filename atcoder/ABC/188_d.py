import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n, ccc = map(int, input().split())
        dat = []
        dset = set()
        mval = 0
        for i in range(n):
            a,b,c = map(int, input().split())
            dat.append([a,b,c])
            dset.add(a)
            dset.add(b)
            mval = max(mval, b)

        dset.add(mval + 1)
        dsetall = list(dset)
        dsetall.sort()
        zatsu = dict()
        zatsuReverse = dict()
        for i in range(len(dsetall)):
            zatsu[dsetall[i]] = i
            zatsuReverse[i] = dsetall[i]
        imos = [0] * (8 * 10**5 + 10)
        buf = []
        for i in range(n):
            a,b,c = dat[i]
            a = zatsu[a]
            b = zatsu[b]
            imos[2*a]+= c
            imos[2*b+1]-= c
            buf.append([a,b,c])
        res = 0
        imosval = 0
        beforeday = 0
        for day in range(len(zatsu)):
            today = zatsuReverse[day]
            res += min(imosval,ccc) * (today-beforeday-1)
            morning = 2*day
            night = 2*day + 1
            imosval += imos[morning]
            curcost = min(imosval, ccc)
            res += curcost
            imosval += imos[night]
            beforeday = today
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
        input = """2 6
1 2 4
2 2 4"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """163089627821228"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """88206004785464"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()