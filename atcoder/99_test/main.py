
from pprint import pprint
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

import math
INF = 1 << 63
ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
def do():
    s = input()
    ans = 1 * s.count("v") + 2 * s.count("w")
    print(ans)


# 1 time
do()
