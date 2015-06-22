#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# pexpectのサンプル。
"""
一定の処理をした後に、ユーザに処理を渡す
"""

# 参考にしたページ
# http://www.noah.org/python/pexpect/

# ライブラリのインストール
import pexpect

# pexpectを開く。子プロセス相当としてftpを実行する。
child = pexpect.spawn ('ftp ftp.openbsd.org')

# 基本となるのはexpectで子プロからの標準入力を待つ
# 第一引数は正規表現をリストとして羅列できる
# timeoutで一定時間まつ
# これをすぎるとタイムアウトの例外が発生する
num = child.expect (['([nN]ame) .*: ', 'Login: .*'], timeout=5)

# 戻り値としては何個目のパターンにマッチしたかが分かる。
# ftpコマンドの場合、0個目にひっかかる
# この例だとLoginに引っかかった場合は1が返るということ
print "match: " + str(num)

# expect()を実行すると、matchに正規表現オブジェクト_sre.SRE_Matchが入る
# つまり、上記みたいに、()で囲っておくと、groupsで取り出せる
# 例えば、"Welcome recuraki, this..."みたいなのをexpectで、
# Welcome ([^ ]*), this でひっかけると、groups[0]にrecurakiが入る
print child.match.groups()

# sendlineは文字列を送る
child.sendline ('anonymous')

# パスワードを入力
child.expect ('[pP]assword:')
child.sendline ('noah@example.com')

# コマンドを実行
child.expect ('ftp> ')
child.sendline ('ls /pub/OpenBSD/')

# beforeはsendlineを入力してからexpectされるまでの文字列が入る
# afterはexpectしたあとのバッファを吐く
# このため、afterは終了時の処理として適切である
child.expect ('ftp> ')
print child.before   # Print the result of the ls command.

print child.after

# ユーザに処理を渡す
# これはexpectがとっていた処理をユーザに委譲する
# つまり、子プロが完全に常駐したアプリに化けるという認識でok
child.interact()

