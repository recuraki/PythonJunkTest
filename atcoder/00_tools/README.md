# AtCoder Solved Language
```
> python3 atcodersolvelang.py -u recuraki 
abc080_a C++14 PyPy3
abc080_b PyPy3
abc082_b Python3
abc084_a C++14 PyPy3
```

のように問題番号 と 解いたことのある言語のリストをします．

# シナリオ
> python3 atcodersolvelang.py -u recuraki | grep 'Py' | grep -v 'C++' | egrep "^abc[^ ]*_a "   
```
abc124_a COBOL-Fixed PyPy3
abc125_a COBOL-Fixed PyPy3
abc126_a PyPy3 Python3
abc127_a COBOL-Fixed PyPy3 Python3
```
Python/PyPyで解いたことがあり，C++で解いたことのないABCのa問題を列挙します．(これがやりたくて作りました．)

# 使い方
```
-n: cacheをしません．標準では300秒以内のリクエストはcacheします．
-u <username>: usernameに対して取得しに行きます．自分だけなら適当にソースコードを書き換えてください
```

# キャッシュ
キャッシュファイルはcache.<username>.jsonで作成されます．