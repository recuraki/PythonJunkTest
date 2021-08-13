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
        n, m = map(int, input().split())
        G = [[] for _ in range(n)]
        for i in range(m):
            a, b = map(int, input().split())
            a-=1
            b-=1
            G[a].append(b)

        import collections
        res = 0
        for s in range(n):
            visited = [False] * n
            q = collections.deque([])
            q.appendleft(s)
            cnt = 0
            while len(q) > 0:
                cur = q.popleft()
                if visited[cur] is True:
                    continue
                visited[cur] = True
                cnt += 1
                for next in G[cur]:
                    if visited[next]:
                        continue
                    q.append(next)
            res += cnt
        print(res)



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
        input = """3 3
1 2
2 3
3 2"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 0"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
1 2
2 3
3 4
4 1"""
        output = """16"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()