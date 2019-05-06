import MeCab
import logging
import sys
from pprint import pprint

t = MeCab.Tagger('mecabrc')

print(t.parse("電気も難しいよね。"))