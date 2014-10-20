#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# http://www.noah.org/python/pexpect/

# 一定の処理をした後に、ユーザに処理を渡す

# ライブラリのインストール
import pexpect

# pexpectを開く。子プロセス相当としてftpを実行
child = pexpect.spawn ('ftp ftp.openbsd.org')

# timeoutで一定時間まつ
# expect()の第一引数は正規表現をリストとして羅列できる
# 第二引数はタイムアウト値であり、これをすぎるとタイムアウトの例外が発生する
num = child.expect (['([nN]ame) .*: ', 'Login: .*'], timeout=5)

# 戻り値としては何個目のパターンにマッチしたかが分かる。
# ftpコマンドの場合、0個目にひっかかるはず
print "match: " + str(num)

# expect()のあとはmatchに正規表現オブジェクト_sre.SRE_Matchとしてマッチが返ってくる
# ので、上記みたいに、()で囲っておくと、groupsで取り出せる
print child.match.groups()

# sendlineは文字列を送る
child.sendline ('anonymous')

# 以下は非常にシンプルな例
child.expect ('[pP]assword:')
child.sendline ('noah@example.com')
child.expect ('ftp> ')

# 以下は非常にシンプルな例
child.sendline ('ls /pub/OpenBSD/')
child.expect ('ftp> ')

# beforeはsendlineを入力してからexpectされるまでの文字列が入る
# afterはexpectしたあとのバッファを吐く
# このため、afterは終了時の処理として適切である
print child.before   # Print the result of the ls command.

print child.after

# ユーザに処理を渡す
# これはexpectがとっていた処理をユーザに委譲する
child.interact()     # Give control of the child to the user.
