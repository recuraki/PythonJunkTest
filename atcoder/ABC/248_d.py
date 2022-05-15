import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import bisect

    N = int(input())
    A_list = list(map(int, input().split()))
    Q = int(input())
    q_list = []
    for i in range(Q):
        tmp = list(map(int, input().split()))
        q_list.append(tmp)

    # [Aiの値, i(インデックス)] のリストを作成
    A_list_2 = []
    for i in range(len(A_list)):
        A_list_2.append([A_list[i], i + 1])

    # Aiの値順にソート
    A_list_2.sort(key=lambda x: x[0])

    # Aiの値ベースでbisectするためのkey
    keys1 = [r[0] for r in A_list_2]

    # インデックスの値ベースでbisectするためのkey
    keys2 = [r[1] for r in A_list_2]

    for q in q_list:
        L = q[0]
        R = q[1]
        X = q[2]

        # Xが一致する範囲を特定
        left_1 = bisect.bisect_left(keys1, X)
        right_1 = bisect.bisect_right(keys1, X)

        # 特定した範囲内でインデックスがL〜Rのものを特定
        left_2 = bisect.bisect_left(keys2, L, lo=left_1, hi=right_1)
        right_2 = bisect.bisect_right(keys2, R, lo=left_1, hi=right_1)

        # 差を答えとする
        print(right_2 - left_2)


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
3 1 4 1 5
4
1 5 1
2 4 3
1 5 2
1 3 3"""
        output = """2
0
0
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()