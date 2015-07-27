#!env python

import time

def difftime(f):
    def w(*args, **kwargs):
        import time
        s = time.time()
        r = f(*args, **kwargs)
        e = time.time()
        print("ran {0}(): {1}".format(f.__name__, e - s))
        return r
    return w

@difftime
def hoge():
    time.sleep(1)

hoge()
