import itertools

"""
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
基本的に後ろからひっくり返していく
"""
print(list(itertools.permutations([1,2,3])))

"""
上記の性質を利用して
https://atcoder.jp/contests/abc150/tasks/abc150_c
等は手抜きで求められる
"""
