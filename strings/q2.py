#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 結果として想定される文字列をstrに代入
str="""
interface port 1/1
 description hogehoge
 switchport trunk add 201-700
interface port 1/2
 description hogehoge2
 shutdown
 switchport trunk add 201-700,801,900
interface port 1/3
 switchport access 2
 description hogehoge
"""

# まず、元の文字列を表示
print("Original:")
print("[" + str + "]")

# Try1: 「インターフェースの一覧が欲しい」
# ヒント: findallでその正規表現にマッチする結果がリストで返ってきます
"""
期待される出力
1/1
1/2
1/3
"""

print "try1"

# クエリ文字列はinterface port <num>/<num>です
query = ""

# ここでインタフェースにあたる文字列をfindallする
# re.finditerは(query文字列, 検索するパターン)です
res = re.finditer(query, str)

# finditerはforで回せる
for m in res:
    # それぞれについて１個目のグループを表示
    #print(m.group(1))
    pass


# try2: 「switch portの行を抜きだしてvlan番号をとろう」
# > tagかuntagは気にしなくていいです
"""
期待される結果
201-700
201-700,801,900
2
"""

print "try2"

# クエリ文字列を作ります
# switchport trunk add (文字列)<改行>
# switchport access (文字列)<改行>
# がとれればです
# ヒント: 「いずれかの文字列」は例えば(foo|bar)で検索できます
# ヒント: vlanを示すのは[0-9,]+な文字列でも良いですし、
#         spaceの後に文字列があって、改行まででも検索できます
query = ""

# ここでインタフェースにあたる文字列をfindallする
# re.finditerは(query文字列, 検索するパターン)です
res = re.finditer(query, str)

# finditerはforで回せる
for m in res:
    # ヒント: 何個目のグループを取るべきかを考えてみましょう
    #print()
    pass


# try3:I/F, vlan番号を表示しましょう
"""
想定される結果
1/1:201-700
1/2:201-700,801,900
1/3:2
"""

print "try3"

"""
ヒント
1: interface port 1/1
2:  description hogehoge
3:  shutdown
4:  switchport trunk add 201-700
を考えます。
1については上記の例の通り考えます。
すると、interface port (\d+/\d+)\n
で1行目を引っ掛けられます。
2-3が難しいです。ここは「何行あるかわからない」からです。
でも、何を抜きたいか考えると、
- 「インデントされている=そのI/Fの設定」もので、
- switchportでなければすべで除外
したいです。つまり、
 \s+.*\n
 > 空白が適当な数あって
 > 任意の文字があり(この場合の.は改行以外と解釈されます)
 > 改行まで
の「0個以上」にマッチさせます
4はもうやりました。
\s+switchport (trunk add|access) (.*)
で大丈夫です。
"""

res = re.finditer("", str)
# finditerはforで回せる
for m in res:
    # ヒント: 何個目のグループを取るべきかを考えてみましょう
    #print()
    pass

