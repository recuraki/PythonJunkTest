import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        from collections import defaultdict
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        data.sort()
        datb.sort()
        candidate = set()
        aa = data[0]
        for bb in datb:
            candidate.add(aa^bb)
        #print(candidate)
        res = []

        for x in candidate:
            cnt = defaultdict(int)
            for bb in datb: cnt[bb] += 1
            can = True
            #print(cnt)
            for aa in data:
                need = aa ^ x
                if cnt[need] <= 0:
                    can = False
                    break
                cnt[need] -= 1
            if can: res.append(x)

        print(len(res))
        res.sort()
        for x in res: print(x)

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
1 2 3
6 4 7"""
        output = """1
5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
0 1
0 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """24
14911005 70152939 282809711 965900047 168465665 337027481 520073861 20800623 934711525 944543101 522277111 580736275 468493313 912814743 99651737 439502451 365446123 198473587 285587229 253330309 591640417 761745547 247947767 750367481
805343020 412569406 424258892 329301584 123050452 1042573510 1073384116 495212986 158432830 145726540 623594202 836660574 380872916 722447664 230460104 718360386 620079272 109804454 60321058 38178640 475708360 207775930 393038502 310271010"""
        output = """8
107543995
129376201
139205201
160626723
312334911
323172429
481902037
493346727"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()