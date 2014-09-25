#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# http://www.noah.org/python/pexpect/

# 一定の処理をした後に、ユーザに処理を渡す

import pexpect
child = pexpect.spawn ('ftp ftp.openbsd.org')
# timeoutで一定時間まつ
num = child.expect (['([nN]ame) .*: ', 'Login: .*'], timeout=5)
# 0個目にひっかかるはず
print "match: " + str(num)
# matchは正規表現オブジェクト_sre.SRE_Matchとして帰ってくる。
# ので、上記みたいに、()で囲っておくと、groupsで取り出せる
print child.match.groups()
child.sendline ('anonymous')

# 正規表現が使える
child.expect ('[pP]assword:')
child.sendline ('noah@example.com')
child.expect ('ftp> ')

child.sendline ('ls /pub/OpenBSD/')
child.expect ('ftp> ')

print child.before   # Print the result of the ls command.

print child.after

# ユーザに処理を渡す
child.interact()     # Give control of the child to the user.
