import MeCab
import logging
import sys
from pprint import pprint

t = MeCab.Tagger('mecabrc')

def test(s):
    print("-----")
    node = t.parseToNode(s)
    while node:
        if jpfilter(node):
            print("{0}:{1}".format(node.surface, node.feature))
        node = node.next

def jpfilter(node: MeCab.Node):
    """
    今回利用する品詞はTrueを返す
    また、ひらがなで1文字などはstopwordとして考えられるので除去
    記号も除去する。しかし、？は有意な気もするのでとっておく
    :param node:
    :return:
    """
    hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん"
    if str(node.feature).startswith("助動詞"):
        return False
    if str(node.feature).startswith("助詞"):
        return False
    if str(node.feature).startswith("記号"):
        if node.surface != "？":
            return False
    if len(node.surface) < 2:
        if all([c in hiragana for c in node.surface]):
            return False
    return True

class jpToken():
    t = MeCab.Tagger('mecabrc')
    def __init__(self):
        pass

    def do(self, s):
        print("----")
        print(s)
        node: MeCab.Node
        res = list()
        node = self.t.parseToNode(s)
        while node:
            if jpfilter(node):
                res.append(node.surface)
            node = node.next
        pprint (res)
        return (res)


if __name__ == "__main__":
    t = jpToken()
    print(t.do("明日にしてもいいかな"))
    print(t.do("メソッドは以下の通り。 文字コードとか、不要な情報とかを除去してリスト化している。"))
    print(t.do("了解です"))
    print(t.do("そうだね"))
