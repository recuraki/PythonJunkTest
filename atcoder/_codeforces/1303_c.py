import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        s = input()
        d = dict()
        f = True
        # STEP1: 入力文字列から隣り合う文字の関係を作る
        for i in range(len(s)):

            # 前後の文字を得る
            nkey = s[i + 1] if i != len(s) - 1 else None
            pkey = s[i - 1] if i != 0 else None

            l = d.get(s[i], [])

            # 前の文字がすでに隣接関係に登録されていないなら
            if pkey is not None and pkey not in l:
                # 文字を入れたいのにすでに両端が他の文字と指定されているなら不可能
                if len(l) >= 2:
                    f = False
                    break
                l.append(pkey)
                d[s[i]] = l

                l2 = d.get(pkey, [])
                if s[i] not in l2:
                    if len(l2) >= 2:
                        f = False
                        break
                    l2.append(s[i])
                    d[pkey] = l2

            if nkey is not None and nkey not in l:
                # 文字を入れたいのにすでに両端が他の文字と指定されているなら不可能
                if len(l) >= 2:
                    f = False
                    break
                l.append(nkey)
                d[s[i]] = l

                l2 = d.get(nkey, [])
                if s[i] not in l2:
                    # 文字を入れたいのにその左右がreserveされているなら
                    if len(l2) >= 2:
                        f = False
                        break
                    l2.append(s[i])
                    d[nkey] = l2

        # STEP1終わり。
        # codedocaという入力から以下の制約の辞書を作れる
        # {'c': ['o', 'a'], 'o': ['c', 'd'], 'd': ['o', 'e'], 'e': ['d'], 'a': ['c']}
        # print(d)

        # STEP2 隣接するキーボードを作る
        s = ""
        # 上記で作った文字ごとに順番に処理を行う
        for k in d.keys():
            if s == "":  # 空文字列の時
                if len(d[k]) == 0:
                    s += k
                elif len(d[k]) == 1:
                    s += k + d[k][0]
                elif len(d[k]) == 2:
                    s += d[k][0] + k + d[k][1]
            # その文字の位置がまだキーボードに存在しないなら
            elif s.find(k) == -1:
                ic1 = ic2 = -1
                # ヒントとなる制約文字列の位置を探し
                if len(d[k]) == 1:
                    ic1 = s.find(d[k][0])
                elif len(d[k]) == 2:
                    ic1 = s.find(d[k][0])
                    ic2 = s.find(d[k][1])

                # もし、2文字とも配置されているならその間に別の文字を挟まないといけないのでNG
                if ic1 != -1 and ic2 != -1:
                    f = False
                # ic1だけが配置されているなら
                elif ic1 != -1:
                    # 先頭なら
                    if ic1 == 0:
                        s = k + s # この文字を先頭に加え
                        if len(d[k]) == 2:  # さらにもう一文字未設置文字があるなら
                            s = d[k][1] + s # さらに先頭にその文字を加える
                    elif ic1 == len(s) - 1:  # 一番後ろなら↑の逆を行う
                        s = s + k
                        if len(d[k]) == 2:
                            s = s + d[k][1]

                elif ic2 != -1:  # ic2探しの旅
                    if ic2 == 0:  # 先頭がその文字なら
                        s = s[k][0] + k + s # その文字とさらに隣にいるべき文字を追加
                    elif ic2 == len(s) - 1:  # 一番後ろなら
                        s = s + k + s[k][0] # 同じように

            else:  # その文字がすでに配置されているならば
                ic = s.find(k)
                if ic == 0:  # その文字が先頭にあるなら
                    if len(d[k]) == 2 and s[1] == d[k][0]: # 先頭の隣が1個めの文字のとき
                        if d[k][1] in s: # 2つめの文字をおこうとする(もうあるなら置けないから失敗)
                            f = False
                        s = d[k][1] + s
                    elif len(d[k]) == 2 and s[1] == d[k][1]:# 先頭の隣が2個めの文字のとき
                        if d[k][0] in s:# 1つめの文字をおこうとする(もうあるなら置けないから失敗)
                            f = False
                        s = d[k][0] + s
                    elif len(d[k]) == 2: # 先頭の隣が1つめの文字でも2つめの文字でもないなら失敗
                        f = False
                    elif len(d[k]) == 1 and s[1] == d[k][0]: # 先頭の隣があるべき隣接文字の場合
                        pass #なにもしない(=もう配置されているんだから)
                    else: # それ以外の時、というのはあるべき文字でない場合なので失敗
                        f = False
                elif ic == (len(s) - 1):  # その文字が文末にあるなら
                    if len(d[k]) == 2 and s[len(s) - 2] == d[k][0]: # 隣が1個めの文字のとき
                        if d[k][1] in s:
                            f = False
                        s = s + d[k][1]
                    elif len(d[k]) == 2 and s[len(s) - 2] == d[k][1]: # 隣が2個めの文字のとき
                        if d[k][0] in s:
                            f = False
                        s = s + d[k][0]
                    elif len(d[k]) == 2: # 先頭の隣が1つめの文字でも2つめの文字でもないなら失敗
                        f = False
                    # 隣が1つめの文字でも2つめの文字でもないなら失敗
                    elif len(d[k]) == 1 and s[len(s) - 2] == d[k][0]:
                        pass  # 正常
                    else:
                        f = False
                        pass
                else:  # そうでないなら真ん中に絶対あるので
                    if s[ic - 1] not in d[k] or s[ic + 1] not in d[k]:  # 両端の文字が片方でも違うなら失敗
                        f = False
                    else:  # この場合は両方がいずれかの文字なのでok
                        pass

        # STEP2 終わり
        # STEP3 他の文字で存在しないものをキーボードに足していく
        if f:
            list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']
            for c in list_lower:
                if c not in s:
                    s = s + c
            print("YES")
            print(s)
        else:
            print("NO")




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
ababa
codedoca
abcda
zxzytyz
abcdefghijklmnopqrstuvwxyza"""
        output = """YES
bacdefghijklmnopqrstuvwxyz
YES
edocabfghijklmnpqrstuvwxyz
NO
YES
xzytabcdefghijklmnopqrsuvw
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()