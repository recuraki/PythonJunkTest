# -*- coding: utf-8 -*-
 
from nose.tools import with_setup, raises
from myfunc import add
 
# assert 文で評価する
def test_add_nums():
    actual = add(1, 10)
    assert actual == 11
 
 
# テストケース実行前に実行する関数
def setup_func():
    # 好きなことをする
    pass
 
# テストケース実行後に実行する関数
def teardown_func():
    # 好きなことをする
    pass
 
# @with_setup でテストケース実行前/後に実行する関数を指定する
@with_setup(setup_func, teardown_func)
def test_addNumbers():
    actual = add(-1, 1)
    assert actual == 0
 
 
# @raises で例外が投げられるかをテストする
@raises(RuntimeError)
def test_invalid_arg1():
    actual = add(None, 1)
 
# 未実装の機能へのテストケース
# エラーになるはず。
@raises(RuntimeError)
def test_invalid_args2():
    # 入力値チェックで RuntimeError を投げることを機能仕様としたいが、
    # まだ未実装なので + 演算で TypeError が発生する
    actual = add(1, None)
