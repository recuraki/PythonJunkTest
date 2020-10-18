import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools

    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]

    def do():
        q = int(input())
        for _ in range(q):
            s = input()
            s = "A" + s + "B"
            c = countstrs(s)
            import collections
            q = []
            for x,y in c:
                q.append(y)
            q[0] -= 1
            q[-1] -= 1
            loop = 0
            while True:
                loop += 1
                if loop > 10:
                    break
                isChange = False
                nokoria = nokorib = 0
                newq = []
                cnta = 0
                for i in range(0, len(q), 2):
                    cnta += q[i]
                    cntb = q[i+1]
                    if cntb == 0:
                        continue
                    if cnta >= cntb:
                        cnta, cntb = cnta-cntb, 0
                        isChange = True
                    else:
                        cnta, cntb = 0, cntb - cnta
                        newq.append(cnta)
                        newq.append(cntb)
                        isChange = True

                if cnta > 0:
                    newq.append(cnta)
                    newq.append(0)

                q = newq
                if len(q) < 2:
                    break
                if isChange is True:
                    break
            sumb = 0
            suma = 0
            for i in range(0, len(q), 2):
                suma += q[i]
                sumb += q[i+1]
            print(suma + sumb%2)




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
        input = """4
AAA
BABA
AABBBABBBB
BAAABBAABBB"""
        output = """3
2
0
1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()