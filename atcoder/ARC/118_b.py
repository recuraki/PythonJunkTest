import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from decimal import Decimal
    from fractions import Fraction
    k, n, m = map(int, input().split())
    # 何倍するのが合計mを目指せる倍数か？
    delta = Fraction(m, n)
    dat = list(map(Fraction, input().split()))
    buf =[]
    res = []
    shosu = []
    for i in range(k): # 全ての人数に対して
        x = dat[i]
        buf.append(x * delta) # m人の村に合わせる
        res.append(int(x * delta)) # 人数なので、整数(なので足りなくなる可能性がほとんど)
        shosu.append( (i, x * delta - int(x*delta) ) ) # ここで、小数部分だけ、indexつきで取り出す
    shosu.sort(reverse= True, key=lambda x: x[1]) # 小数部分だけ大きい順に並べる
    temporaryTotal = sum(res)
    needPerson = m - temporaryTotal # 切り捨てている状態で、m人の村に何人足りないかを数える
    for i in range(needPerson): # 小数を切り捨てているので"needPerson"分補充。これは小数部分が大きい順に追加
        ind, _ = shosu[i]
        res[ind] += 1
    print(" ".join(list(map(str, res))))

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
        input = """3 7 20
1 2 4"""
        output = """3 6 11"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 100
1 1 1"""
        output = """34 33 33"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 10006 10
10000 3 2 1 0 0"""
        output = """10 0 0 0 0 0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7 78314 1000
53515 10620 7271 3817 1910 956 225"""
        output = """683 136 93 49 24 12 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()