# -*- coding: utf-8 -*-
 
from api import api_add
 
class TestAdd:
 
    @classmethod
    def setup_class(clazz):
        pass
 
    @classmethod
    def teardown_class(clazz):
        pass
 
    def setup(self):
        pass
 
    def teardown(self):
        pass
 
    def test_add_nums_ok(self):
        actual = api_add(1, 10)
        assert actual == 11

    def test_add_nums_minus(self):
        actual = api_add(10, -5)
        assert actual == 5

    def test_add_nums_minus2(self):
        actual = api_add(-5, 10)
        assert actual == 5

    def test_add_nums_str(self):
        actual = api_add(1, 10)
        assert actual == 11
