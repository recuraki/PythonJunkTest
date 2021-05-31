import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    def do():

        import sys
        read = sys.stdin.read
        n, *indata = map(int, read().split())

        buf = []
        dat = []
        offset = 0
        for i in range(n):
            x, y = indata[offset], indata[offset + 1]
            dat.append( (x, y, i) )
            offset += 2

        candidate = []
        dat.sort()

        buf.append( dat[0] )
        buf.append( dat[1] )
        buf.append( dat[-1] )
        buf.append( dat[-2] )

        dat.sort(key = lambda x: x[1])

        buf.append( dat[0] )
        buf.append( dat[1] )
        buf.append( dat[-1] )
        buf.append( dat[-2] )

        #print(dat)

        ss = []
        used = set()

        for i in range(len(buf)):
            for j in range(i + 1, len(buf)):
                indi = buf[i][2]
                indj = buf[j][2]
                if indi == indj:
                    continue
                indi, indj = min(indi, indj),max(indi, indj)
                hash = indi * 10**9 + indj
                if hash in used:
                    continue
                used.add(hash)
                diff = max(abs(buf[i][0] - buf[j][0] ), abs(buf[i][1] - buf[j][1] ))
                ss.append(diff)
        res = list(ss)
        res.sort(reverse=True)
        print(res[1])
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
0 0
1 2
4 0"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
0 0
0 0
1 0
0 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20
407 361
167 433
756 388
-551 -47
306 -471
36 928
338 -355
911 852
288 70
-961 -769
-668 -386
-690 -378
182 -609
-677 401
-458 -112
184 -131
-243 888
-163 471
-11 997
119 544"""
        output = """1766"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """4
0 0
0 0
0 0
0 0"""
        output = """0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()