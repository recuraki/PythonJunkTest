import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    def do():
        strn = int(input())
        dat = []
        import collections
        pref = set()
        for _ in range(strn):
            s = input()
            dat.append(s)
            pref.add(s[:3])
            pref.add(s[-3:])
        #print(dat)
        #print(pref)
        pref2NodeId = dict()
        i = 0
        for x in pref:
            pref2NodeId[x] = i
            i += 1
        n = len(pref)
        g = [set() for _ in range(n)]
        grev = [set() for _ in range(n)]

        for s in dat:
            pp = pref2NodeId[s[:3]]
            if s[-3:] in pref2NodeId:
                ss = pref2NodeId[s[-3:]]
            else:
                pass
            #print(pp, ss)
            g[pp].add(ss)
            grev[ss].add(pp)


        #print(g)
        #rint(grev)
        q = collections.deque()
        res = [1] * n
        visited = [False] * n
        # 0:勝ち, 1: draw 2: 負け
        for i in range(n):
            if len(g[i]) == 0: # これを取ったら先がないので勝ち
                res[i] = 0
                visited[i] = True
                continue

        print(visited)
        #cnt = 0
        for i in range(n):
            if visited[i]: continue # 探索済みなら無視
            x = (i, 0) # 0 探索モード
            q.appendleft(x)
            while len(q) > 0:
                curnode, curmode = q.popleft()
                if curmode == 0:
                    visited[curnode] = True
                    #print("iki", curnode)
                    x = (curmode, 1)
                    q.appendleft(x) # 戻りを追加
                    for nextnode in g[curnode]:
                        # 探索済みなら処理しない
                        if visited[nextnode]: continue
                        # 未探索なら探索する
                        x = (nextnode, 0)
                        q.appendleft(x)
                elif curmode == 1:
                    #print("modri", curnode)
                    status = 2
                    for nextnode in g[curnode]:
                        # かち = 負けるしかないならそれ
                        if nextnode == 1:
                            status = min(status, 1)
                        if nextnode == 2: # 負けがあるなら絶対勝ち
                            status = 0
                            break
                else:
                    assert False

        for x in dat:
            ss = x[-3:]
            #print(pref2NodeId[ss], ss)
            if res[pref2NodeId[ss]] == 0:
                print("Takahashi")
            elif res[pref2NodeId[ss]] == 1:
                print("Draw")
            elif res[pref2NodeId[ss]] == 2:
                print("Aoki")
            else:
                assert False








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
abcd
bcda
ada"""
        output = """Aoki
Takahashi
Draw"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
ABC"""
        output = """Draw"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
eaaaabaa
eaaaacaa
daaaaaaa
eaaaadaa
daaaafaa"""
        output = """Takahashi
Takahashi
Takahashi
Aoki
Takahashi"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """5
abcd
bcde
cdef
defg
efgh"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()