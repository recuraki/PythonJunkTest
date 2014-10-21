#!/usr/local/bin/python

def deco(func):
    print("hoge")
    return("moge")

@deco
def test():
    print("hige")

    
