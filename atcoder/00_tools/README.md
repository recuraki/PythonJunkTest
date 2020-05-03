# AtCoder Solved Language
あるIDに対して
```
abc080_a C++14 PyPy3
abc080_b PyPy3
abc082_b Python3
abc084_a C++14 PyPy3
```

のように問題番号:解いたことのある言語のリストをします．

# 使い方
```
-n: cacheをしません．標準では300秒以内のリクエストはcacheします．
-u <username>: usernameに対して取得しに行きます．自分だけなら適当にソースコードを書き換えてください
```

# シナリオ
> python3 atcodersolvelang.py -u recuraki | grep 'Py' | grep -v 'C++' | egrep "^abc[^ ]*_a "   

Python/PyPyで解いたことがあり，C++で解いたことのないABCのa問題を列挙します．(これがやりたくて作りました．)

# キャッシュ
キャッシュファイルはcache.<username>.jsonで作成されます．