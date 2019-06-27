import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    visited = [0] * (n + 1)
    ne = []
    for i in range(n+1):
        ne.append([])
    for i in range(n-1):
        a, b = map(int, input().split())
        ne[a].append(b)
        ne[b].append(a)
    print(ne)
    s2e = 0
    fsize = 0
    ssize = 0
    can = ne[1]
    import collections
    q = collections.deque(can)
    visited[1] = True
    def search(cur, v_s2e, v_fsize, v_ssize, turn):
        print("---")
        print("cur" + str(cur))
        print("q:" + str(q))
        if len(q) == 0:
            return v_s2e, v_fsize, v_ssize
        for i in range(len(ne[cur])):
            q.appendleft(ne[cur][len(ne[cur]) - i - 1])
        nestep = q.popleft()
        print("q[add]:" + str(q))
        print("step" + print(nestep))

        if visited[nestep]:
            return v_s2e, v_fsize, v_ssize

        if nestep == n:
            visited[nestep] = True
            turn = 1
            x, y, z = search(nestep, v_s2e,v_fsize,v_ssize + 1, turn)
        elif turn == 0:
            visited[nestep] = True
            x, y, z = search(nestep, v_s2e, v_fsize + 1, v_ssize, turn)
        elif turn == 1:
            visited[nestep] = True
            x, y, z = search(nestep, v_s2e,v_fsize + 1,v_ssize + 1, turn)
        else:
            print("!!!!!!!!!!!!")

        return x, y, z
    x, y, z = search(1, 0, 0, 0, 0)
    print("---")
    print(x)
    print(y)
    print(z)




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
        input = """7
3 6
1 2
3 1
7 4
5 7
1 4"""
        output = """Fennec"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 4
4 2
2 3"""
        output = """Snuke"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()