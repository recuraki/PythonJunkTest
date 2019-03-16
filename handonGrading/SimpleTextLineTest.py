#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from pprint import pprint
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)

class SimpleTextLineTest():
    """
    入力された文字列（複数行を想定）に対して、
    指定された複数行テキストを改行でパースし、
    「含まれるべき文字列」のANDと
    「含まれてはいけない文字列」のORに一致するか判別する。
    executeにて試験は実施される。
    resultにて結果は参照される。
    テストケースはr対して以下のように返却される。
    例：(True, 'p', 'as200', None, [1,2])
    (res, type, pattern, match)
    res: その文字列に対する結果
    type: p=positive-含まれるべき文字列, n=negative-含まれてはいけない文字列
    pattern: その評価文字列
    match: pの場合、マッチした文字列、nの場合、マッチ「してしまった」文字列
    pos: matchの範囲(start, end)
    """
    text = ""
    lines = []
    positive_texts = []
    negative_texts = []
    __result = []
    f_pass = False
    debug = False

    def __init__(self, text, Positive, Negative, argvFormat = {}, debug = False):
        """

        :param text: 対象となる複数文字列(0x0dでsplitされる)
        :param Positive: 含まれるべき文字列のリスト
        :param Negative: 含まれてはならない文字列のリスト
        :param debug: デバッグメッセージの有無(default: False)
        :param argvFormat: {pattern}を置換するpattern: strのリスト
        """
        self.text = text
        self.lines =  text.split("\n")
        self.positive_texts = Positive
        self.negative_texts = Negative
        self.argv = argvFormat
        self.debug = debug
        self.execute()

    def execute(self):
        """
        試験結果のを得る。
        Trueの場合、試験をパスしたこととなる
        Falseの場合、試験は失敗したことなる。
        試験の結果はraw_resultにて詳細の結果を得られる
        :return: True, False
        """
        self.__result = []
        self.f_pass = False
        r1 = self.exec_Positive()
        r2 = self.exec_Negative()
        self.f_pass = r1 and r2
        return self.f_pass

    def dp(self, s):
        if self.debug:
            print(s)

    def exec_Positive(self):
        """
        含まれるべき文字列の評価関数
        :return:
        """
        f_matchall = True
        # positive[]に対してfor
        for pat in self.positive_texts:
            offset = 0
            pat = pat.format(**self.argv)
            f_found = False
            if f_matchall == False:
                self.result.append((None, "p", pat, None, None))
                continue
            # 対象文字列すべてを操作
            for l in self.lines:
                # 見つけたら抜ける
                res = re.search(pat, l)
                if res:
                    f_found = True
                    break
                offset = offset + len(l) + 1
            # もし見つけずに最後まで来てしまったら
            if f_found == False:
                self.result.append((False, "p", pat, None, None))
                f_matchall = False
                # 評価を失敗とする
                continue

            pos = [offset + res.start(), offset + res.end()]
            self.result.append((True, "p", pat, None, pos))
        return f_matchall

    def exec_Negative(self):
        f_noall = True
        # negative[]に対してfor
        for pat in self.negative_texts:
            pat = pat.format(**self.argv)
            if f_noall == False:
                self.result.append((None, "n", pat, None, None))
                continue
            f_notfound = True
            mstr = ""
            # 行の累積文字数
            offset = 0
            # 対象文字列すべてを操作
            for l in self.lines:
                res = re.search(pat, l)
                # 「見つかった」場合だけ抜ける＝失敗
                if res:
                    f_notfound = False
                    mstr = l.strip()
                    break
                offset = offset + len(l) + 1
            # もしも、見つかってしまったのなら
            if f_notfound == False:
                pos = [offset + res.start(), offset + res.end()]
                self.result.append((False, "n", pat, mstr, pos))
                f_noall = False
                # 失敗を返す
                continue
            self.result.append((True, "n", pat, None, None))

        return f_noall

    def is_pass(self):
        return self.f_pass

    @property
    def result(self):
        # この結果は、execute後に詳細な情報を得るために用いられる
        return self.__result

    def decorateHTML(self):
        mapTagToHtml = {}
        mapTagToHtml["10posend"] = "</span>"
        mapTagToHtml["11posstart"] = "<span class=positivechar>"
        mapTagToHtml["20negend"] = "</span>"
        mapTagToHtml["21negstart"] = "<span class=negativechar>"
        decorateLine = {}
        for r in self.result:
            if r[1] == "p" and r[0] == True:
                lineStart, lineEnd =  r[4][0],r[4][1]
                decorateLine[lineStart] = decorateLine.get(lineStart, []) + ["11posstart"]
                decorateLine[lineEnd] = decorateLine.get(lineEnd, []) + ["10posend"]
            if r[1] == "n" and r[0] == False:
                lineStart, lineEnd =  r[4][0],r[4][1]
                decorateLine[lineStart] = decorateLine.get(lineStart, []) + ["21negstart"]
                decorateLine[lineEnd] = decorateLine.get(lineEnd, []) + ["20negend"]
        for k in decorateLine:
            decorateLine[k] = sorted(decorateLine[k])
        decorateLine[len(self.text)] = []
        left = 0
        html = ""
        for right, tags in sorted(decorateLine.items()):
            html = html + self.text[left:right]
            for tag in tags:
                html = html + mapTagToHtml.get(tag, "")
            left = right
        return html


str="""
neighbor as100 192.168.100.1
neighbor as200 192.168.100.2
neighbor as200 192.168.100.3
neighbor as300 192.168.100.4
"""

header="""
<html><head>
<style type="text/css">
<!--
.positivechar {background-color:#eeeeee; color:#44ff44;}
.negativechar {background-color:#ffffff; color:#ff0000;}
-->
</style>
</head><body>"""
footer="""
</body></html>"""

if __name__ == "__main__":
    p = ["as200", "as300", "bor.*100\.1"]
    n = ["as800" ,"as100", "as700"]
    s = SimpleTextLineTest(str, p, n, debug=True)
    pprint(s.result)
    res = s.decorateHTML()
    print(header)
    print(res)
    print(footer)