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
        n = int(input())
        dat = list(map(int, input().split()))
        mina = dat[0]
        minb = dat[1]
        # 好きに選べる数
        cnta = n - 1
        cntb = n - 1
        suma = mina
        sumb = minb
        res = (mina + minb) * n # 若干特殊
        for i in range(2, n):
            x = dat[i]
            if i % 2 == 0:
                cnta -= 1
                suma += x
                mina = min(mina, x)
            else:
                cntb -= 1
                sumb += x
                minb = min(minb, x)
            cost = suma + sumb + (mina * cnta) + (minb * cntb)
            res = min(cost, res)
        print(res)





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
        input = """3
2
13 88
3
2 3 1
5
4 3 2 1 4"""
        output = """202
13
19"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()