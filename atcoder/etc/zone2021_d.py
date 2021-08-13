import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def main():
        def f(l):
            #print(l, maxval)
            finalres = 0
            for ll in l: #全てのパターンを操作
                candidate = []
                for tup in ll: # 各タプル
                    val = 0
                    for i in range(n): # 全部舐める
                        personmin = 10 ** 8
                        for x in tup:
                            personmin = min(personmin, dat[i][x])
                        val = max(val, personmin)
                    candidate.append(val)
                finalres = max(finalres, min(candidate))

            return finalres

        n = int(input())
        dat = []
        maxval = [0] * 5
        for i in range(n):
            a,b,c,d,e, = map(int, input().split())
            dat.append((a,b,c,d,e))

        dat.sort(reverse=True, key = lambda x: x[0])
        target = []
        target.append( ( [0,1], [2,3], [4] ) )
        target.append( ( [0,2], [1,3], [4] ) )
        target.append( ( [0,3], [1,2], [4] ) )
        target.append( ( [0,4], [1,2], [3] ) )
        target.append( ( [0,2], [1,4], [3] ) )
        target.append( ( [0,1], [2,4], [3] ) )
        target.append( ( [0,1], [3,4], [2] ) )
        target.append( ( [0,3], [1,4], [2] ) )
        target.append( ( [0,4], [1,3], [2] ) )
        target.append( ( [0,2], [3,4], [1] ) )
        target.append( ( [0,3], [2,4], [1] ) )
        target.append( ( [0,4], [2,3], [1] ) )
        target.append( ( [1,2], [3,4], [0] ) )
        target.append( ( [1,3], [2,4], [0] ) )
        target.append( ( [1,4], [2,3], [0] ) )
        target.append( ( [0,1,2], [3], [4] ) )
        target.append( ( [0,1,3], [2], [4] ) )
        target.append( ( [0,2,3], [1], [4] ) )
        target.append( ( [1,2,3], [0], [4] ) )
        target.append( ( [0,1,2], [4], [3] ) )
        target.append( ( [0,1,4], [2], [3] ) )
        target.append( ( [0,2,4], [1], [3] ) )
        target.append( ( [1,2,4], [0], [3] ) )
        target.append( ( [0,1,3], [4], [2] ) )
        target.append( ( [0,1,4], [3], [2] ) )
        target.append( ( [0,3,4], [1], [2] ) )
        target.append( ( [1,3,4], [0], [2] ) )
        target.append( ( [0,2,3], [4], [1] ) )
        target.append( ( [0,2,4], [3], [1] ) )
        target.append( ( [0,3,4], [2], [1] ) )
        target.append( ( [2,3,4], [0], [1] ) )
        target.append( ( [1,2,3], [4], [0] ) )
        target.append( ( [1,2,4], [3], [0] ) )
        target.append( ( [1,3,4], [2], [0] ) )
        target.append( ( [2,3,4], [1], [0] ) )
        target.append( ( [1,2,3,4], [0] ) )
        target.append( ( [0,2,3,4], [1] ) )
        target.append( ( [0,1,3,4], [2] ) )
        target.append( ( [0,1,2,4], [3] ) )
        target.append( ( [0,1,2,3], [4] ) )
        res = f(target)
        print(res)
    main()


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
3 9 6 4 6
6 9 3 1 1
8 8 9 3 7"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
6 13 6 19 11
4 4 12 11 18
20 7 19 2 5
15 5 12 20 7
8 7 6 18 5"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()