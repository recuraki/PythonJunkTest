import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 閉路はない
    n = int(input())

    from collections import deque
    d1 = [deque([]) for _ in range(n)]
    d2 = [deque([]) for _ in range(n)]
    d3 = [deque([]) for _ in range(n)]
    for i in range(n-1):
        a,b = map(int, input().split())
        a,b = a-1, b-1
        d1[a].append(b)
        d1[b].append(a)

    # 距離2を作る
    for i in range(n):
        for j in range(len(d1[i])):
            # その距離1のエッジ
            en = d1[i][j]
            for k in range(len(d1[en])):
                # 距離2 の エッジ
                d2e = d1[en][k]
                # 自分自身ではなく、自分のテーブルにないなら
                if d2e != i and d2e not in d1[i]:
                    if d2e not in d2[i]:
                        d2[i].append(d2e)
                    if i not in d2[d2e]:
                        d2[d2e].append(i)
    #print(d2)

    # 距離3を作る
    for i in range(n):
        for j in range(len(d2[i])):
            # その距離2のエッジ
            en = d2[i][j]
            for k in range(len(d1[en])):
                # 距離2 の エッジの距離1のエッジ = 3 候補
                d3e = d1[en][k]
                # 自分自身ではなく、自分のテーブルにないなら
                if d3e != i and d3e not in d1[i] and d3e not in d2[i]:
                    if d3e not in d3[i]:
                        d3[i].append(d3e)
                    if i not in d3[d3e]:
                        d3[d3e].append(i)

    #print(d3)
    count = []
    m0can = deque([])
    m1can = deque([])
    m2can = deque([])
    for i in range(n):
        count.append( (len(d3[i]), i) )
        if (i+1) % 3 == 0:
            m0can.append(i+1)
        elif (i+1) % 3 == 1:
            m1can.append(i+1)
        elif (i+1) % 3 == 2:
            m2can.append(i+1)

    count.sort(reverse=True)
    count = deque(count)
    #print(count)

    res = [-1] * n
    usedmax = n + 1 # 掛け算の捨てよう
    used = [False] * (n+1)
    while(len(m0can) > 0):
        if len(count) != 0:
            e = count.popleft()
            nv = m0can.popleft()
            res[e[1]] = nv
            used[nv] = True

    mode = 1

    canComplete = True
    for i in range(n):
        #print("loop", i)
        if res[i] != -1: # 決定しているなら
            continue
        l3 = len(d3[i])
        if l3== 0: # 何でもいい子は後回し
            #print("this node not needs", i)
            continue
        enforce = -1
        for j in range(l3):
            #print("search enf" ,j , res[d3[i][j]] )
            if res[d3[i][j]] == -1: # 未使用なら関係ない
                #print("nous")
                continue
            elif enforce == -1: # まだ色の指定がないならその色で
                #print("deside")
                enforce = res[d3[i][j]] % 3
            elif enforce != res[d3[i][j]] % 3:
                canComplete = False
                break
        #print("this must enforce", enforce)
        if enforce == 0: # mod0の希望なら何でもいいので今の色
            if mode == 1 and len(m1can) != 0:
                nv = m1can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 2
            elif len(m2can) != 0:
                nv = m2can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 1
            else: # m3を指定してもいいか？
                canComplete = False
                break
        elif enforce == 1: # mod1が来ているならmod2ないといけない
            if len(m2can) != 0:
                nv = m2can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 1
        elif enforce == 2: # mod1が来ているならmod2ないといけない
            if len(m1can) != 0:
                nv = m1can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 2
        elif enforce == -1: # 希望なし
            #print("enf-1")
            if mode == 1 and len(m1can) != 0:
                nv = m1can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 2
            elif mode == 2 and len(m2can) != 0:
                nv = m2can.popleft()
                res[i] = nv
                used[nv] = True
                mode = 1

    candidate = 1
    """
    print(res)
    print(used)
    print(m0can)
    print(m1can)
    print(m2can)
    """
    for i in range(n):
        if res[i] == -1:
            while used[candidate] is True:
                candidate += 1
            res[i] = candidate
            used[candidate] = True

    if canComplete is False or n==1 or n==2 or n==3:
        print(-1)
    else:
        print(" ".join(list(map(str, res))))


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
1 2
1 3
3 4
3 5"""
        output = """1 2 5 4 3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7
1 2
1 3
2 4
4 5
5 6
5 7"""
        output = """1 2 5 4 3"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """2
1 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input_22(self):
        print("test_input_21")
        input = """3
1 2
2 3"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()