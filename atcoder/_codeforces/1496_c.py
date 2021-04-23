import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    q, *dat = map(int, sys.stdin.read().split())
    offset = 0
    for qq in range(q):
        n = int(dat[offset])
        offset += 1
        datx = []
        daty = []
        for i in range(2*n):
            a,b = dat[offset + 2*i], dat[offset + 2*i + 1]
            if a == 0:
                daty.append(abs(b))
            else:
                datx.append(abs(a))
        offset += 2 * n * 2
        #print(datx, daty)
        datx.sort()
        daty.sort()
        res = 0
        import math
        for i in range(n):
            x, y = datx[i], daty[i]
            z = math.sqrt(x**2 + y**2)
            #print(x,y,z)
            res += math.sqrt(x**2 + y**2)
        print(res)



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
2
0 1
1 0
0 -1
-2 0
4
1 0
3 0
-5 0
6 0
0 3
0 1
0 2
0 4
5
3 0
0 4
0 -3
4 0
2 0
1 0
-3 0
0 -10
0 -2
0 -10"""
        output = """3.650281539872885
18.061819283610362
32.052255376143336"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()