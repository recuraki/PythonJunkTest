import string
import random
import secrets
"""
適当なパスワードを作成する generate(length)を提供する
標準では、発音・形状的に間違えやすい以下の文字を使用しません。
 oO01IilL9qQZz2dDgGnmNMbB8pPtT
 これが不要の場合、ignorechars=set()などで消してください。
使い方:
o = generatePassword()
o.useSpecial = False
o.addIgnore("@")
for i in range(10):
    print(o.generate(length=5+i))
"""
class generatePassword(object):
    def __init__(self):
        self.useUpper = True
        self.useLower = True
        self.useDigit = True
        self.useSpecial = True
        # 各文字を定義する
        self.charUpper = set(string.ascii_uppercase)
        self.charLower = set(string.ascii_lowercase)
        self.charDigit = set(string.digits)
        self.charSpecial = set("!#()&<>;@[]|")
        # フォント, 発音によって間違いやすい文字の一覧。
        self.ignorechars: set = set("oO01IilL9qQZz2dDgGnmNMbB8pPtT")

    def addIgnore(self, s: str):
        # 引数で与えられた文字列に含まれる文字をpasswordとして使わないようにする。
        for x in s: self.ignorechars.add(x)

    def doIgnore(self):
        # パスワード生成前に呼ぶ関数。使いたくない文字列を除去する
        for char in self.ignorechars:
            if char in self.charUpper: self.charUpper.remove(char)
            if char in self.charLower: self.charLower.remove(char)
            if char in self.charDigit: self.charDigit.remove(char)
            if char in self.charSpecial: self.charSpecial.remove(char)

    def generate(self, length=12):
        self.doIgnore() # 前処理としてignoreの文字を候補から消す
        order = [] # 使ってもよい文字のtype。Falseになっているtypeは使わない
        if self.useUpper: order.append(self.charUpper)
        if self.useLower: order.append(self.charLower)
        if self.useDigit: order.append(self.charDigit)
        if self.useSpecial: order.append(self.charSpecial)
        # 文字種別が1つもなければ(=全てFalseだと)エラー
        assert(len(order) > 0)
        # 4種類の文字を使うのに3文字のlength,などの場合をはじく
        assert(length >= len(order))
        random.shuffle(order) # 文字種別を適当な順番にシャッフルする[数字・特殊文字・大文字・小文字]や[数字・小文字・特殊文字・大文字]など
        numTypes = len(order) # 文字の種類の数
        charsTypes = [] # 各文字を選んだ数
        for i in range(numTypes):
            # ある種別の文字数を決める。1文字　～ 他の文字種類が最低1文字含まれる文字数
            t = (length - sum(charsTypes) - ( (numTypes-1) - i))
            # この時の文字が1 or maxである率を低くする。
            # その方が打ちやすいはず。このため、(rand + rand) / 2する。　と、1やmaxが含まれにくくなる
            charnums   = secrets.randbelow(t)
            charnums  += secrets.randbelow(t)
            charnums //= 2
            charnums += 1
            charsTypes.append(charnums)
        # randするので、文字数が足りなければ、最後の文字種別を増やす。
        charsTypes[-1] += length - sum(charsTypes)
        # この種類・順番にしたがってパスワードを生成
        res = ""
        for i in range(numTypes):
            res += ''.join([secrets.choice(list(order[i])) for _ in range(charsTypes[i])])
        return res



import sys
if __name__ == "__main__":
    o = generatePassword()
    o.useSpecial = False # useUpper, useLower, useDigitもあります。
    o.addIgnore("@") # さらに使いたくない文字があれば消してください
    # o.ignorechars = set() # 特に禁則文字がないならこれを入れる
    for i in range(10): # 10個くらい例を出します
        print(o.generate(length=10)) # lengthで作るパスワードの長さです