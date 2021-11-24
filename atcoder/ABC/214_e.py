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
        n = int(input())
        dat = []
        used = set()
        unusemin = 0
        for _ in range(n):
            l, r = map(int, input().split())
            l -= 1
            r -= 1
            dat.append((l, r))
        dat.sort()
        #print(dat)
        for l, r in dat:
            # もし、未使用がとても小さいなら、とりあえずlをいれて次へ
            if unusemin < l:
                unusemin = l
                unusemin += 1
                continue
            # 使えないならだめ
            if unusemin > r:
                print("No")
                return
            # 使えるなら
            unusemin += 1
        print("Yes")

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
        input = """2
3
1 2
2 3
3 3
5
1 2
2 3
3 3
1 3
999999999 1000000000"""
        output = """Yes
No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()