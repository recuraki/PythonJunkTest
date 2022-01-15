import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n, m = map(int, input().split())
        e = [list() for _ in range(n)]
        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            e[a].append(b)
            e[b].append(a)

        res = []
        used = [False] * n
        for i in range(n):
            if used[i]:
                continue
            if len(e[i]) == 0:
                used[i] = True
                res.append(i)
                continue
            if len(e[i]) == 2:
                continue
            if len(e[i]) > 2:
                print("No")
                return
            # 1
            res.append(i)
            used[i] = True
            p = i
            cur = e[i][0]
            while True:
                res.append(cur)
                used[cur] = True
                if len(e[cur]) == 1:
                    break
                if len(e[cur]) != 2:
                    break
                if e[cur][0] == p:
                    p = cur
                    cur = e[cur][1]
                else:
                    p = cur
                    cur = e[cur][0]
        if len(res) != n:
            print("No")
            return
        print("Yes")
        #print(res)


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
        input = """4 2
1 3
2 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 4
2 4
3 4"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()