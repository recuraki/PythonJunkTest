import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class rollingHash61():
        MOD = (1 << 61) - 1
        BASE = 20200213
        MASK30 = (1 << 30) - 1
        MASK31 = (1 << 31) - 1
        hashTable = []
        pow = []
        slen = -1
        sdat = []

        def __init__(self, s: str):
            self.sdat = list(map(lambda x: ord(x), s))
            self.slen = len(s)
            self.hashTable = [0] * (self.slen + 1)
            self.pow = [1] * (self.slen + 1)
            for i in range(self.slen):
                self.hashTable[i + 1] = self.multi(self.hashTable[i], self.BASE)
                self.hashTable[i + 1] += self.xorshift(self.sdat[i] + 1)
                self.pow[i + 1] = self.multi(self.pow[i], self.BASE)
                self.hashTable[i + 1] = (self.hashTable[i + 1] - self.MOD) if (self.hashTable[i + 1] >= self.MOD) else \
                self.hashTable[i + 1]

        def hash(self, l, r):
            # calc hash [l, r)  r = OPEN
            res = self.MOD + self.hashTable[r] - self.multi(self.hashTable[l], self.pow[r - l])
            return res if (res < self.MOD) else (res - self.MOD)

        def mod(self, x):
            res = (x >> 61) + (x & self.MOD)
            return res - self.MOD if res >= self.MOD else res

        def multi(self, x, y):
            xu, xd = x >> 31, x & self.MASK31
            yu, yd = y >> 31, y & self.MASK31
            m = xd * yu + xu * yd
            mu = m >> 30
            md = m & self.MASK30
            return self.mod(xu * yu * 2 + mu + (md << 31) + xd * yd)

        def xorshift(self, x):
            return x ^ (x << 13) ^ (x >> 17) ^ (x << 5)

    from pprint import pprint
    def do():
        n = int(input())
        s =  input()
        origRH = rollingHash61(s)
        origH = origRH.hash(0, n)
        #print(origH)
        # |s| <= 200000
        # s =    300000 = 3 * 100000
        rs = "110" * 100000
        RH = rollingHash61(rs)
        cnt3 = 0
        i = 0
        while True:
            if i + n > 300000:
                break
            if RH.hash(i, i + n) == origH:
                cnt3 += 1
            i+=1

        rs = "110" * 200000
        RH = rollingHash61(rs)
        cnt31 = 0
        i = 0
        while True:
            if i + n > 600000:
                break
            if RH.hash(i, i + n) == origH:
                cnt31 += 1
            i+=1


        #print(cnt3)
        #print(cnt31)
        fuerudiff = cnt31 - cnt3
        print(cnt3 + fuerudiff*99999)

    def do2():
        n = 3
        s = "110"
        origRH = rollingHash61(s)
        origH = origRH.hash(0, n)
        rs = "110" * 100
        RH = rollingHash61(rs)
        cnt3 = 0
        i = 0
        while True:
            if i + n > (n*100):
                break
            if RH.hash(i, i + n) == origH:
                cnt3 += 1
            i += 1
        print(cnt3)


    do()
    #do2()





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
1011"""
        output = """9999999999"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """22
1011011011011011011011"""
        output = """9999999993"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_12")
        input = """1
1"""
        output = """9999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()