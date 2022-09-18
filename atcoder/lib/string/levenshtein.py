

# https://naoya-2.hatenadiary.org/entry/20090329/1238307757
"""
編集距離 (レーベンシュタイン距離, Levenshtein Distance)
は二つの文字列の類似度 (異なり具合) を定量化するための数値です。
文字の挿入/削除/置換で一方を他方に変形するための最小手順回数を数えたものが編集距離です。
"""
def levenshtein_distance(a, b):
    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in range(len(a) + 1):
        m[i][0] = i

    for j in range(len(b) + 1):
        m[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)
    #print(m)
    return m[-1][-1]

assert levenshtein_distance("", "abc") == 3
assert levenshtein_distance("", "") == 0
assert levenshtein_distance("a", "b") == 1
assert levenshtein_distance("", "b") == 1
assert levenshtein_distance("abc", "dbe") == 2
