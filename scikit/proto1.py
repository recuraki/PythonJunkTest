import pandas as pd
import tokenlib
from gensim import corpora
from pathlib import Path
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

def make_dict(cache=True, dictfile="dict.txt"):
    """
    bowをどう実装するか悩んでいたときのもの
    :param cache:
    :param dictfile:
    :return:
    """
    logging.warning("make_dict()")
    if cache:
        # cache利用が有効の場合、存在をチェック
        curdir = Path()
        dictpath = curdir / dictfile
        if dictpath.exists():
            logging.warning("use Cache")
            # ディクショナリのロード
            dictionary = corpora.Dictionary.load_from_text(dictpath)
            return dictionary
    logging.warning("noexist cache")
    original_df = pd.read_csv('dataset.csv', encoding='utf-8')
    original_df['v1'].value_counts()
    msgs = original_df['v2']
    words = []
    for msg in msgs:
        words.append(t.do(msg))
    dictionary = corpora.Dictionary(words)
    # no_aboveは指定した【割合】以上の場合無視する
    # no_belowは指定して【数量】未満の場合無視する
    dictionary.filter_extremes(no_below=1, no_above=1.0)
    dictionary.save_as_text('dict.txt')
    return dictionary

# トークン化のライブラリロード
t = tokenlib.jpToken()

# csvのload
original_df = pd.read_csv('dataset.csv', encoding='utf-8')

# メッセージデータのわかち書き化を行う
# 特定品詞のみをとりだし、かつ、スペースで結合された文字列とする
# 疲れたね。遊んだね。
# -> ['疲れ', '遊ん']
# -> "疲れ 遊ん"
X = original_df['v2'].apply(lambda s: " ".join(t.do(s)))
X = pd.DataFrame(X)
y = original_df['v1'].apply(lambda s: 1 if s == 'spam' else 0)

# 学習データとテストデータの分離(train_sizeが割合。0.9なら9:1で分割)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9)

# 単語の出現頻度カウント/TF-IFD
vectorizer = TfidfVectorizer(norm='l2')
# 学習
vectorizer.fit(X_train['v2'])

# 学習した語彙数
print('Vocabulary size: {}'.format(len(vectorizer.vocabulary_)))

# ベクタデータ化
X_train_bow = vectorizer.transform(X_train['v2'])
X_test_bow = vectorizer.transform(X_test['v2'])

# モデル選択
model = BernoulliNB()
#model = MultinomialNB()


# 学習
model.fit(X_train_bow, y_train)
print('Train accuracy: {:.3f}'.format(model.score(X_train_bow, y_train)))
print('Test accuracy: {:.3f}'.format(model.score(X_test_bow, y_test)))

def do_test(s):
    """
    試験用コード
    :param s:
    :return:
    """
    vect = vectorizer.transform([" ".join(t.do(s))])
    predict = model.predict(vect)[0]
    predict_proba = model.predict_proba(vect).tolist()
    print(vect)
    print(predict)
    print(predict_proba)

do_test("今日はメンテが複数回あり、いくつかはトラブルがあったので疲れた。")
do_test("東京から神田駅はすぐつくと思う。")