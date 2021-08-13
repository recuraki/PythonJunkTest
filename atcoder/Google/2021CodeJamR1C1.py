import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(taskno):
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        enemycandidate = set()

        for x in dat: # 0 orig
            x -= 1
            enemycandidate.add(x)

        res = 0
        for i in range(k):
            for j in range(i+1, k):
                # i と jを選んだ時
                canwin = 0 # nこの中で勝つ確率
                for kkk in range(k): # 正解がkだとする
                    mostcloseEnemy = 10 ** 9
                    for enemy in enemycandidate:
                        #print("k", k, "dump", mostcloseEnemy, abs(enemy- k ))
                        mostcloseEnemy = min(mostcloseEnemy, abs(enemy - kkk) )
                        #print("ene", enemy, k , mostcloseEnemy)
                    # mostcloseEnemyが最も近い敵
                    youclosei = abs(kkk-i)
                    youclosej = abs(kkk-j)
                    youclose = min(youclosej, youclosei)
                    #print("most ene", mostcloseEnemy, "you", youclose)
                    if youclose < mostcloseEnemy:
                        canwin += 1
                #print("chose", i, j, "prob=", (canwin/k), canwin, n)
                res = max(res,  (canwin / k))


        print("Case #{0}: {1}".format(taskno, res))
    q = int(input())
    for qq in range(q):
        do(qq+1)


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
        input = """4
3 10
1 3 7
4 10
4 1 7 3
4 3
1 2 3 2
4 4
1 2 4 2"""
        output = """Case #1: 0.5
Case #2: 0.4
Case #3: 0.0
Case #4: 0.25"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()