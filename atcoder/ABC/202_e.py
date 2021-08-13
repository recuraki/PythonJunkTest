import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        import sys
        read = sys.stdin.read
        n, *inbuf = map(int, read().split())
        indat = inbuf[:n-1]
        offset = n-1
        G = [[] for _ in range(n)]

        for i in range(n-1):
            x = indat[i] - 1
            G[i+1].append(x)
            G[x].append(i+1)
        q = []
        depth = [-1] * n
        q.append([0, 0, 0])
        curtime = -1
        query = inbuf[offset]
        offset += 1
        import collections
        trigger = collections.defaultdict(list)
        # トリガーは[i]で (q , d) つまり、その下で、 dの個がいた場合、qを足す
        # iを抜けるときに、このトリガーのindexは消す
        for qq in range(query):
            u, d = inbuf[offset], inbuf[offset + 1]
            #print(u,d)
            offset += 2
            u -= 1
            trigger[u].append( (qq, d) )

        depthChecker = [set() for _ in range(n)]

        res = [0] * query
        while len(q) != 0:
            curtime += 1
            curnode, curdepth, vcost = q.pop()
            if curnode >= 0:  # 行き掛け
                # in なのでdepth checkerを仕掛ける
                for qq, d in trigger[curnode]:
                    depthChecker[d].add(qq)
                depth[curnode] = curdepth
                for qq in depthChecker[curdepth]:
                    res[qq] += 1
                q.append([~curnode, curdepth, 0])
                for nextnode in G[curnode]:
                    if depth[nextnode] != -1:
                        continue
                    q.append([nextnode, curdepth + 1, 0])
                    #parent[nextnode] = curnode
            else:  # 帰りがけ
                curnode = ~curnode
                for qq, d in trigger[curnode]:
                    depthChecker[d].remove(qq)
        for q in range(query):
            print(res[q])
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
        input = """7
1 1 2 2 4 2
4
1 2
7 2
4 1
5 5"""
        output = """3
1
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()