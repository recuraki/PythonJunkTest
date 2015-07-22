#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import Crypto.Cipher.AES
import binascii
from struct import *

"""
今回はAESを使うが、そもそもの対応は、
pydoc Crypto.Cipher
で確認できて、
`Crypto.Cipher.Blowfish`    Block     Blowfish
とかもある。

MODEについては
pydoc Crypto.Cipher.AESで確認して、
- For `MODE_ECB`, `MODE_CBC`, and `MODE_OFB`,
などがあることを確認する。

今回はCBC
"""


from Crypto import Random
iv = Random.new().read(AES.block_size)

# ECBの場合、キーは{16,24,32}文字
# CBCの場合、IVは16bytesとなる
aes = Crypto.Cipher.AES.new(iv,
                            Crypto.Cipher.AES.MODE_CBC)

# 対象は16文字
msg = "0" * 16

e_msg = aes.encrypt(msg)
print(repr(e_msg))
# 複数やっても同じ結果です
e_msg = aes.encrypt(msg)
print(repr(e_msg))

# 共通鍵暗号なので、同じオブジェクトで戻せる
d_msg = aes.decrypt(e_msg)
print(d_msg)
