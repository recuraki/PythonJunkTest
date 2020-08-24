import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    datx = []
    daty = []
    datp = []
    res = [0]
    from copy import deepcopy
    for i in range(n):
        x, y, p = map(int, input().split())
        datx.append(x)
        daty.append(y)
        datp.append(p)

    patlist = []
    for pat in range(2 ** n):
        l = [True] * n
        patlist.append([pat, l])

    for deadstation in range(n): # i個目の駅をなくす
        workpat = []
        curmin = 999999999999
        for pat, alive in patlist:
            # patパターンリスト
            # alive 駅iが生きているかのリスト
            print("pat", pat, alive)
            linex = [ [0, -1] ]
            liney = [ [0, -1] ]
            # 各パターンごとに向いている方向を決める
            for i in range(n):
                if alive[i] is False:
                    continue
                if (pat >> i & 1) == 1: # liney
                    liney.append([daty[i], i] )
                else:
                    linex.append([datx[i], i] )
            #print(linex, liney)

            resdeadcost = [999999999999] * n
            for i in range(n): # 駅iを廃止したとする
                if alive[i] is False: # 既にない駅は廃止する意味がない
                    continue
                icost = 0 # その場合のコスト
                for j in range(n): #各駅からのコスト計算
                    costforj = 9999999999
                    x, y, p = datx[j], daty[j], datp[j]

                    for targetx, indexnum in linex: # j->kへの距離計算(X軸)
                        if indexnum == i:
                            continue
                        costforj = min(costforj, abs(targetx -x) )

                    for targety, indexnum in liney: # j->kへの距離計算(X軸)
                        if indexnum == i:
                            continue
                        costforj = min(costforj, abs(targety - y) )

                    icost += costforj * p
                resdeadcost[i] = icost
            mincost = min(resdeadcost)
            print("mincost", mincost, resdeadcost)

            if curmin < mincost: # これまでのパターンで出てきた最小値なら価値がない
                continue
            for i in range(n):
                if resdeadcost[i] == mincost:
                    newalive = deepcopy(alive)
                    newalive[i] = False
                    #print("!!!", newalive)
                    workpat.append([pat, newalive, mincost])

        workpat2 = []
        rescost = 9999999999999999999
        for pat, newalive, cost in workpat:
            rescost = min(rescost, cost)
            if cost == mincost:
                workpat2.append([pat, newalive])

        res.append(rescost) # 結果は最小値
        patlist = workpat2 # 入れ替え

    #print(res)
    res.reverse()
    print("\n".join(list(map(str, res))))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_2(self):
        print("test_input_2")
        self.maxDiff = 100000000
        input = """5
3 5 400
5 3 700
5 5 1000
5 7 700
7 5 400"""
        output = """13800
1600
0
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()