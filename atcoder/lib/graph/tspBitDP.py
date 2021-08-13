import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def do():
        INF = 10**18
        numv, nume = map(int, input().split())
        # [s][t]のグラフ。-1が未達。
        e = [[-1] * numv for _ in range(numv)]
        for _ in range(nume):
            s, t, d = map(int, input().split())
            e[s][t] = d

        dp = [[INF] * numv for _ in range(2**numv)]

        # TSPで戻ってくる制約の場合、少し工夫が必要。
        # というのも、訪問の集合|pat|に対して、sのビットを立ててしまうと戻ってこられなくなる。
        # このため、「戻ってくる」という制約の場合はグラフが必ずハミルトン経路を持つので
        # dp[0][0] = 0とする。本来これはdp[1][0]のはずなのだが
        # ※なぜなら、[pat][curnode]に対してcurnode=0なのだから、patは1<<curnode=1<<0=1でなければ変だ
        # あえて、[0][0]とすることで、再度node=0に戻ってくることを意味する。
        dp[0][0] = 0
        # つまり、戻ってくる必要のない場合はこう初期化するべきだ。(この場合、node0 startなら[1][0] = 0とされる
        #for i in range(numv):
        #    dp[1<<i][i] = 0

        for pat in range(0, 2**numv): # 今の状態
            for curnode in range(numv): # 計算のもととなるノード
                if pat != 0 and (pat & (1 << curnode)) == 0:
                    # 今の状態でそもそもこのノードにいないなら処理はNG
                    # ただし、戻ってくるTSPの場合、pat == 0の時はこの判定をしてはいけない。(のでpat!=0 and)
                    continue
                for nextnode in range(numv):
                    if nextnode == curnode:
                        continue # 同一のノードに行こうとするのはダメ
                        # dp[i][i] = 0にしておけば更新しても良いが。
                    if (pat & (1<<nextnode) != 0):
                        continue # 今の状態(pat)で訪問済み(=nextnodeが立っている)なら処理は進めない
                    if e[curnode][nextnode] == -1:
                        continue # このパスが存在しないなら実行はしない。
                    nextpat = pat | (1 << nextnode)
                    dp[nextpat][nextnode] = min(dp[nextpat][nextnode], dp[pat][curnode] + e[curnode][nextnode])

        pprint(dp)
        # これは戻ってくる場合。
        if dp[2**numv - 1][0] == INF:
            print("-1")
            return
        print(dp[2**numv - 1][0])
        # 戻ってこない場合、min(dp[2**numv-1]が答え

    do()




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = 100000
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_10(self):
        print("test_input_10")
        input = """4 3
1 2 1
2 3 1
3 0 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """4 6
0 1 2
1 2 3
1 3 9
2 0 1
2 3 6
3 2 4"""
        output = """16"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
0 1 1
1 2 1
0 2 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """15 210
0 1 428
1 0 336
0 2 604
2 0 596
0 3 384
3 0 583
0 4 92
4 0 540
0 5 523
5 0 863
0 6 311
6 0 438
0 7 596
7 0 159
0 8 477
8 0 117
0 9 516
9 0 979
0 10 376
10 0 634
0 11 188
11 0 197
0 12 637
12 0 510
0 13 290
13 0 762
0 14 923
14 0 66
1 2 154
2 1 207
1 3 162
3 1 837
1 4 575
4 1 957
1 5 493
5 1 131
1 6 261
6 1 443
1 7 168
7 1 255
1 8 16
8 1 997
1 9 978
9 1 189
1 10 656
10 1 144
1 11 928
11 1 435
1 12 941
12 1 671
1 13 973
13 1 296
1 14 484
14 1 831
2 3 611
3 2 894
2 4 226
4 2 998
2 5 707
5 2 351
2 6 851
6 2 731
2 7 957
7 2 722
2 8 797
8 2 131
2 9 684
9 2 317
2 10 955
10 2 698
2 11 158
11 2 399
2 12 313
12 2 207
2 13 909
13 2 584
2 14 974
14 2 30
3 4 178
4 3 483
3 5 993
5 3 940
3 6 365
6 3 200
3 7 366
7 3 849
3 8 112
8 3 445
3 9 922
9 3 990
3 10 422
10 3 535
3 11 331
11 3 956
3 12 711
12 3 776
3 13 302
13 3 550
3 14 456
14 3 948
4 5 93
5 4 593
4 6 948
6 4 504
4 7 174
7 4 318
4 8 998
8 4 92
4 9 16
9 4 106
4 10 863
10 4 691
4 11 959
11 4 949
4 12 338
12 4 711
4 13 941
13 4 290
4 14 90
14 4 651
5 6 570
6 5 76
5 7 736
7 5 258
5 8 759
8 5 519
5 9 684
9 5 946
5 10 892
10 5 93
5 11 339
11 5 747
5 12 5
12 5 849
5 13 550
13 5 524
5 14 501
14 5 230
6 7 919
7 6 670
6 8 263
8 6 520
6 9 696
9 6 454
6 10 192
10 6 61
6 11 515
11 6 956
6 12 244
12 6 427
6 13 416
13 6 568
6 14 369
14 6 270
7 8 336
8 7 981
7 9 388
9 7 950
7 10 75
10 7 677
7 11 333
11 7 323
7 12 491
12 7 892
7 13 773
13 7 898
7 14 661
14 7 405
8 9 940
9 8 374
8 10 142
10 8 199
8 11 62
11 8 635
8 12 206
12 8 129
8 13 643
13 8 4
8 14 450
14 8 297
9 10 675
10 9 356
9 11 237
11 9 904
9 12 782
12 9 403
9 13 399
13 9 731
9 14 841
14 9 261
10 11 117
11 10 958
10 12 505
12 10 401
10 13 906
13 10 433
10 14 584
14 10 531
11 12 879
12 11 556
11 13 166
13 11 331
11 14 459
14 11 343
12 13 639
13 12 780
12 14 934
14 12 805
13 14 370
14 13 280
"""
        output = """2029"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()