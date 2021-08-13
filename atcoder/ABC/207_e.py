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
        dat = list(map(int, input().split()))
        modtable = [[0] *(n+1) for _ in range(n + 10)]
        counttable = [[0] *(n+1) for _ in range(n + 10)]

        import itertools
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))
        sdat = createSDAT(dat)
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
        print(sdat)

        for mod in range(1, n+1):
            for i in range(n):
                modtable[mod][i] = sdat[i+1] % mod

        for i in range(1, n+1):
            print("mod", i, modtable[i])

        for i in range(0, n):
            counttable[1][i] = 1

        import collections
        for mod in range(1, n+1): # modごとに見る
            targetMap = collections.defaultdict(int)
            for i in range(n): # 進める
                x = modtable[mod][i]

                # 1つで解決できる場合がある
                if dat[i] % mod == 0:
                    if counttable[mod][i] > 0:
                        print(mod,i)
                        counttable[mod + 1][i + 1] += 1
                counttable[mod+1][i+1] += counttable[mod][i] + targetMap[x]

                # 探したくなる数
                moreneed = mod - x
                target = (x - moreneed) % mod
                targetMap[target] += counttable[mod][i]


        print("---")
        for i in range(1, n+2):
            print("mod", i, counttable[i])


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
1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
8 6 3 3 3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
791754273866483 706434917156797 714489398264550 918142301070506 559125109706263 694445720452148 648739025948445 869006293795825 718343486637033 934236559762733"""
        output = """15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()