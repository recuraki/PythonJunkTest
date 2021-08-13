import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    import sys
    input = sys.stdin.readline


    def do():
        #print("----------------------------------")
        n = int(input())
        values0 = []
        values1 = []
        dp0 = [0] * n
        dp1 = [0] * n
        for _ in range(n):
            a, b = map(int, input().split())
            values0.append(a)
            values1.append(b)


        G = [[] for _ in range(n)]
        for i in range(n - 1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            G[a].append(b)
            G[b].append(a)

        q = []
        qdepth = []
        depth = [-1] * n
        parent = [-1] * n
        q.append(0)
        qdepth.append(0)
        curtime = -1

        #print("dpdebug", dp0, dp1)

        while len(q) != 0:
            curtime += 1
            curnode = q.pop()
            curdepth = qdepth.pop()
            if curnode >= 0:  # 行き掛け
                #print("in", curnode)
                #print("dpdebug", dp0, dp1)
                # in なのでdepth checkerを仕掛ける
                depth[curnode] = curdepth
                q.append(~curnode)
                qdepth.append(curdepth)
                for nextnode in G[curnode]:
                    if depth[nextnode] != -1:
                        continue
                    parent[nextnode] = curnode
                    q.append(nextnode)
                    qdepth.append(curdepth + 1)
                    # parent[nextnode] = curnode
            else:  # 帰りがけ
                curnode = ~curnode
                #print("out init", curnode, "parent" , parent[curnode])
                for child in G[curnode]:
                    if child == parent[curnode]: continue
                    #print("proc child", child)
                    #print("dpdebug", dp0, dp1)
                    # Proc only child
                    # dp0
                    curval = values0[curnode]
                    val0 = abs(curval - values0[child]) + dp0[child]
                    val1 = abs(curval - values1[child]) + dp1[child]
                    #print("dp0 curval=", curval, "val0,1", val0, val1)
                    #print("child low = ", values0[child], "high", values1[child])
                    dp0[curnode] += max(val0, val1)

                    curval = values1[curnode]
                    val0 = abs(curval - values0[child]) + dp0[child]
                    val1 = abs(curval - values1[child]) + dp1[child]
                    #print("dp1 curval=", curval, "val0,1", val0, val1)
                    #print("child low = ", values0[child], "high", values1[child])
                    dp1[curnode] += max(val0, val1)

            #print(">>>")
            #print(dp0)
            #print(dp1)
        print(max(dp0[0], dp1[0]))




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
        input = """3
2
1 6
3 8
1 2
3
1 3
4 6
7 9
1 2
2 3
6
3 14
12 20
12 19
2 12
10 17
3 17
3 2
6 5
1 5
2 6
4 6"""
        output = """7
8
62"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()