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
        nn2, nn3, nn4 = map(int, input().split())
        import collections, itertools
        l = range(5)
        finalres = 0
        for pat in itertools.permutations(l):
            n2, n3, n4 = nn2, nn3, nn4
            res = 0
            for proc in pat:
                if proc == 0:
                    # 4,4,2を頑張る
                    canmake = min(n4//2, n2)
                    res += canmake
                    n4 = n4 - canmake - canmake
                    n2 = n2 - canmake
                elif proc == 1:
                    # 4, 3, 3を頑張る
                    canmake = min(n3//2, n4)
                    res += canmake
                    n3 = n3 - canmake - canmake
                    n4 = n4 - canmake
                elif proc == 2:
                    # 3, 3, 2, 2を頑張る
                    canmake = min(n3//2, n2//2)
                    res += canmake
                    n3 = n3 - canmake - canmake
                    n2 = n2 - canmake - canmake
                elif proc == 3:
                    # 4, 2, 2, 2を頑張る
                    canmake = min(n4, n2//3)
                    res += canmake
                    n4 = n4 - canmake
                    n2 = n2 - canmake*3
                elif proc == 4:
                    # 2, 2, 2, 2, 2を頑張る
                    canmake = n2 // 5
                    res += canmake
                    n2 = n2 - canmake*5
                else:
                    assert False
            finalres = max(finalres, res)
        print(finalres)
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
        input = """5
3 4 1
7 0 0
0 0 7
0 0 0
1000000000000000 1000000000000000 1000000000000000"""
        output = """2
1
0
0
900000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()